"""
Example of choropleth using geojson files.
Based on by Mike Bostock's unemployment choropleth http://bl.ocks.org/mbostock/4060606
"""

import geoplotlib
from geoplotlib.utils import BoundingBox
from geoplotlib.colors import ColorMap
import json, math
import sqlite3, csv, sys
from PyQt4 import Qt
from PyQt4.uic import loadUi
conn = sqlite3.connect('wages.db')
cur = conn.cursor()

class Main(Qt.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loadUi("gui.ui", self)
        self.grade.addItems(['wg1', 'wg2', 'wg3', 'wg4', 'wg5', 'wg6', 'wg7', 'wg8', 'wg9', 'wg10', 'wg11', 'wg12', 'wg13', 'wg14', 'wg15', 'wl1', 'wl2', 'wl3', 'wl4', 'wl5', 'wl6', 'wl7', 'wl8', 'wl9', 'wl10', 'wl11', 'wl12', 'wl13', 'wl14', 'wl15', 'ws1', 'ws2', 'ws3', 'ws4', 'ws5', 'ws6', 'ws7', 'ws8', 'ws9', 'ws10', 'ws11', 'ws12', 'ws13', 'ws14', 'ws15'])

        self.year.addItems([str(year) for year in range(1996, 2017)])
        self.grade_push.clicked.connect(self.start_map)

    def start_map(self):
        Map(self.year.currentText(), self.grade.currentText())

class Map():
    def __init__(self, year, grade):
        self.scale = 18
        self.start = 18
        self.year = year
        self.grade = grade

        cur.execute('select date, state, county, {} from counties where date like "%{}%"'.format(self.grade, self.year))
        print("connected")
        self.counties = cur.fetchall()

        with open('GEOIDs.txt', 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
            self.test = []
        for i in self.counties:
            for x in csv_list:

                if i[1] == x[0] and (i[2] in x[3]):
                    geoid = x[1] + x[2]
                    try:
                        self.test.append([geoid, float(i[3])])
                    except TypeError:
                        self.test.append([geoid, 0])

                self.test.sort(key=lambda j: float(j[1]))

        self.ranger(self.test)
        self.unemployment = {t[0]: t[1] for t in self.test}
        print('starting map')
        self.cmap = ColorMap('plasma', alpha=255, levels=10)
        geoplotlib.geojson('data/gz_2010_us_050_00_20m.json', fill=True, color=self.get_color, f_tooltip=(
        lambda properties: properties['NAME'] + ' ' + str(
            self.unemployment.get(str(properties['STATE']) + properties['COUNTY']))))
        geoplotlib.geojson('data/gz_2010_us_050_00_20m.json', fill=False, color=[255, 255, 255, 64])
        geoplotlib.set_bbox(BoundingBox.USA)
        geoplotlib.show()


    # find the unemployment rate for the selected county, and convert it to color
    def get_color(self, properties):
        key = str(properties['STATE']) + properties['COUNTY']
        if key in self.unemployment:
            return self.cmap.to_color(self.unemployment.get(key) - self.start, self.scale, 'lin')
        else:
            print(key)
            return [0, 0, 0, 0]

    def find_min(self, sorted_list):
        sorted_list.sort(key=lambda j: float(j[1]))
        for el in sorted_list:
            if float(el[1]) != 0:
                return el[1]

    def ranger(self, p_list):
        p_list.sort(key=lambda j: float(j[1]))
        low = math.floor(self.find_min(p_list))
        high = math.ceil(p_list[-1][1])
        self.start = low
        self.scale = high - low
        return






def main():

    app = Qt.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

conn.close()