# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:30:25 2019

@author: bobtr
"""

import bs4 as bs
import urllib.request 

save_path = 'C:/Users/.../PythonDailyNews'


sauce = urllib.request.urlopen('https://www.wsj.com/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav  
body = soup.body
text = soup.text


for paragraph in body.find_all("h3"):
   print(paragraph.text)
    
   filename = "C:/Users/.../wsjP1news.txt"
   f = open(filename, "a") 
   body = soup.body
   text = soup.text
   f.write('\n') 
   #f.write('News generated by python and spyder3'), 
   #f.write("\a")
   #f.write('Headlines from WSJ, NYT and ForexLive')
   f.write("")
   f.write(paragraph.text)
   f.close()
