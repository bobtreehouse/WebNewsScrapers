# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:30:25 2019

@author: bobtr
"""

import bs4 as bs
import urllib.request 

save_path = 'C:/Users/bobtr/OneDrive/Desktop/Clocks/PythonDailyNews'


sauce = urllib.request.urlopen('https://finance.yahoo.com/').read()
sauce2 = urllib.request.urlopen('https://www.wsj.com/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
soup2 = bs.BeautifulSoup(sauce2, 'lxml')

nav = soup.nav  
nav2 = soup2.nav
body = soup.body
body2 = soup2.body
text = soup.text


for paragraph in body.find_all("h3"):
   print(paragraph.text)
   
for paragraph in body2.find_all("h3"):
   print(paragraph.text)
    
   filename = "C:/Users/.../PythonDailyNews/YHOOnews.txt"
   f = open(filename, "a") 
   body = soup.body
   body2 = soup2.body
   text = soup.text
   f.write('\n') 
   #f.write('News generated by python'), 
   #f.write("\a")
   #f.write('Headlines from Yahoo Finance & WSJ')
   f.write("")
   f.write(paragraph.text)
   f.close()
