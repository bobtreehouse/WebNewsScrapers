# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:30:25 2019

@author: bobtr
"""

import bs4 as bs
import urllib.request 

save_path = 'C:/Users/.../PythonDailyNews/'


sauce = urllib.request.urlopen('https://www.nytimes.com/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav
body = soup.body
main = soup.main#site-content
div = soup.div

#print(nav)(remove hash in front of this line to print the entire nav content)

#for paragraph in body.find_all('h3'):
 #   print(paragraph.text)
    
#for paragraph in body.find_all('a.wsj-headline-link'):
 #   print(paragraph.text)
    
for paragraph in body.find_all('h2'):
   print(paragraph.text)
    
   filename = 'C:/Users/.../PythonDailyNews/NYTnews.txt'
   f = open(filename, "a") 
   body = soup.body
   text = soup.text   
   for paragraph in body.find_all('h2'):
       f.write(paragraph.text)
       f.write('\n')
       #f.write("")   
   f.close()



