"""
Example of choropleth using geojson files.
Based on by Mike Bostock's unemployment choropleth http://bl.ocks.org/mbostock/4060606
"""

import geoplotlib
from geoplotlib.utils import BoundingBox
from geoplotlib.colors import ColorMap
import json, math
import sqlite3, csv

scale = 18
start = 18
conn = sqlite3.connect('wages.db')
cur = conn.cursor()
year = '2016'
grade = 'wg12'

cur.execute('select date, state, county, {} from counties where date like "%{}%"'.format(grade, year))
counties = cur.fetchall()

with open('GEOIDs.txt', 'r') as f:
    reader = csv.reader(f)
    csv_list = list(reader)
test = []
for i in counties:
    for x in csv_list:

        if i[1] == x[0] and (i[2] in x[3]):
            geoid = x[1] + x[2]
            try:
                test.append([geoid, float(i[3])])
            except TypeError:
                test.append([geoid, 0])


test.sort(key=lambda j: float(j[1]))


print(test[-1])  # min 18.65  max  35.79 18-36 range is 18
print(len(counties))
print(counties[0])


# find the unemployment rate for the selected county, and convert it to color
def get_color(properties):
    global start, scale
    key = str(properties['STATE']) + properties['COUNTY']
    if key in unemployment:
        return cmap.to_color(unemployment.get(key) - start, scale, 'lin')
    else:
        print(key)
        return [0, 0, 0, 0]

def find_min(sorted_list):
    sorted_list.sort(key=lambda j: float(j[1]))
    for el in sorted_list:
        if float(el[1]) != 0:
            return el[1]


def ranger(p_list):
    p_list.sort(key=lambda j: float(j[1]))
    low = math.floor(find_min(p_list))
    high = math.ceil(p_list[-1][1])
    global scale, start
    start = low
    scale = high - low
    return
ranger(test)
unemployment = {t[0]:t[1] for t in test}
# with open('data/unemployment.json') as fin:
#     unemployment = json.load(fin)

cmap = ColorMap('inferno', alpha=255, levels=10)
geoplotlib.geojson('data/gz_2010_us_050_00_20m.json', fill=True, color=get_color, f_tooltip=(lambda properties: properties['NAME']))
geoplotlib.geojson('data/gz_2010_us_050_00_20m.json', fill=False, color=[255, 255, 255, 64])
geoplotlib.set_bbox(BoundingBox.USA)
geoplotlib.show()
