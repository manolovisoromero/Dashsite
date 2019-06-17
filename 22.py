# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:42:14 2019

@author: manolo
"""

    # -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:35:32 2019

@author: Manol
"""


site = "https://www.sec.gov/Archives/edgar/data/1385849/000138584919000045/efr-2019033110xq.htm"
site3 = "https://www.sec.gov/Archives/edgar/data/1375205/000155837019003989/urg-20190331x10q.htm"

sites = []
sites.append(site)
sites.append(site3)

keywords = ["Inventories, net","Cash and cash equivalents","Operating activities totaal","Investing activities totaal","Change in cash, cash equivalents and restricted cash during the period"]

"""Onder Assets:
 Cash and Cash equivalents (15,310)
 Inventories, net (19,138)

Condensed consolidation of cash flows:
 Operating activities totaal (-11,553)
 Investing activities totaal (9,950)
 Change in cash, cash equivalents and restricted cash during the period (908)
 """

import urllib.request
from lxml import html

def __scraper__(site, str, pos):
    with urllib.request.urlopen(site) as response:
        htmlSource = response.read()
    tree = html.fromstring(htmlSource)
    path = "//*[contains(text(),'" + str + "')]/../../../td["  + pos + "]/*/font/text()"
    path2 = "//tbody/tr/td//*/font[contains(text(),'Assets')]/../../../..//*[contains(text(),'Cash and cash equivalents')]/../../../td[3]/*/font/text()"

    cace = tree.xpath(path2)
    print(cace)


    
for i in range(len(sites)):
    for str in keywords:
        __scraper__(sites[i],str,"2")