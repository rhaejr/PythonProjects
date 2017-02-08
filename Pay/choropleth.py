"""
Example of choropleth using geojson files.
Based on by Mike Bostock's unemployment choropleth http://bl.ocks.org/mbostock/4060606
"""

import geoplotlib
from geoplotlib.utils import BoundingBox
from geoplotlib.colors import ColorMap
import json
import sqlite3, csv


conn = sqlite3.connect('wages.db')
cur = conn.cursor()

cur.execute('select date, state, county, wg10 from counties where date like "%2016%"')
counties = cur.fetchall()

with open('GEOIDs.txt', 'r') as f:
    reader = csv.reader(f)
    csv_list = list(reader)
test = []
for i in counties:
    for x in csv_list:
        if i[1] == x[0] and i[2] == x[3]:
            geoid = str(x[1]) + str(x[2])
            test.append([geoid, i[3]])
print(test)
print(len(counties))
print(counties[0])


# find the unemployment rate for the selected county, and convert it to color
def get_color(properties):
    key = str(int(properties['STATE'])) + properties['COUNTY']
    if key in unemployment:
        return cmap.to_color(unemployment.get(key), .15, 'lin')
    else:
        return [0, 0, 0, 0]


with open('data/unemployment.json') as fin:
    unemployment = json.load(fin)

cmap = ColorMap('Blues', alpha=255, levels=10)
geoplotlib.geojson('data/gz_2010_us_050_00_20m.json', fill=True, color=get_color, f_tooltip=lambda properties: properties['NAME'])
geoplotlib.geojson('data/gz_2010_us_050_00_20m.json', fill=False, color=[255, 255, 255, 64])
geoplotlib.set_bbox(BoundingBox.USA)
geoplotlib.show()
