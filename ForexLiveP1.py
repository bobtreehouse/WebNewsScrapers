#-*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:22:57 2019

@author: bobtr
"""

import bs4 as bs
import urllib.request 

save_path = 'C:/Users/bobtr/OneDrive/Desktop/Clocks/PythonDailyNews'


sauce = urllib.request.urlopen('https://www.forexlive.com/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav    
body = soup.body

for paragraph in body.find_all("div",{"class":"teaser-text"}):
    print(paragraph.text)

    filename = "C:/Users/bobtr/OneDrive/Desktop/Clocks/PythonDailyNews/forexdailynews.txt"
    f = open(filename, "a") 
    body = soup.body
    text = soup.text
    #f.write('\n') 
    #f.write('thanks for reading\n')
    #f.write('-end\n')
    #f.write('Headlines from WSJ, NYT and ForexLive')
    #f.write("\n")
    f.write("")
    f.write(paragraph.text)
    f.close()
 