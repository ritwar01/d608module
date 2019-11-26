# -*- coding: utf-8 -*-
"""
@author: Ravi Itwaru
"""
import bs4 as bs
import csv
import urllib.request

## This data source will be used to get ridership data for my final project dash app
## Ridership data for year 2018 will be used in the app
sauce = urllib.request.urlopen('http://web.mta.info/nyct/facts/ridership/ridership_sub.htm').read()
## Parse data source for html data
soup = bs.BeautifulSoup(sauce, 'html.parser')
## Get all tags that has type <tr>
trtag = soup.find_all('tr')   # get all tags of type <p>

## Create a list that will store data retrieved
## This list will be used to create a csv file which is why the first element is the csv file headers.
csvfl = [['Station (alphabetical by borough)', '2013', '2014', '2015', '2016', '2017', '2018',
      '2017-2018 Change','2017-2018 Change', '2018 Rank', 'LINE']]

## Here we search the html data for the ridership data and the subway lines associated with them which were a bit diffcult to find since they are in the <alt> tags and not the table tags
h = 1
for tag in trtag:
    ## search for <img> tags   
    imgtags = tag.find_all('img')    
    tdtags = tag.find_all('td')
    #print(len(instrument))
    if imgtags:
        
        i = 0
        subwayline = ""
        while i < len(imgtags):
            #print(instrument[i]['alt'])            
            subwayline += imgtags[i]['alt']   
            
            i +=1
        subwayline = subwayline.replace(" subway", "-")[:-1]
        ridershipstat = [i.text for i in tdtags]
        csvfl.append(ridershipstat)
        #print(s[:-1])
        csvfl[h].append(subwayline)
        #print(a)
        h +=1
    else:   
        print("no <img> tags found")

## The data scraped is is then loaded into a csv file which was published to git hub and used in the actual app for the final project.
## The reason for storing the data is so we don't continuously have to scrape the website when the final project app runs. The data is static and not changing anytime soon.
## The site being scraped is http://web.mta.info/nyct/facts/ridership/ridership_sub.htm
with open('ridershipstat_2018.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvfl)