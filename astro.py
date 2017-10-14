# Astro.py
# Margaret Gorguissian
# 8/10/2017
# Access birthcharts

import urllib2
import json
from bs4 import BeautifulSoup, re


def getbirthchart(month, day, year, hour, minute, ampm, town, country, state= None):
    url = 'http://alabe.com/cgi-bin/chart/astrobot.cgi?INPUT1=&INPUT2=&MONTH=%d&DAY=%d&YEAR=%d&HOUR=%d&MINUTE=%d&AMPM=%s&TOWN=%s&COUNTRY=%s&STATE=%s&INPUT9=&Submit=Submit' % (month, day, year, hour, minute, ampm, town, country, state)
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    chart = soup.find_all(string=re.compile("Degree"))
    chartlist = []
    for line in chart:
        planet = line.split(None, 1)[0]
        sign = line.rsplit(None, 1)[-1]
        chartlist.append((planet, sign))
    print chartlist

#getbirthchart(12, 24, 1996, 04, 20, 'PM', 'Washington', 'USA', 'DC')
#getbirthchart(07, 14, 1959, 07, 00, 'PM', 'Tokyo', 'Japan')
