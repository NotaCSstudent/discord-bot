from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
import csv
import random

pd.options.mode.chained_assignment = None  # default='warn'

LeetCode_Problems = pd.read_csv('Problems.csv') 

LeetCode_Problems['title']

#print(len(LeetCode_List))
t = random.uniform(0,len(LeetCode_Problems['title']))
t = int(t)

for i in range(len(LeetCode_Problems['title'])):
    if " " in LeetCode_Problems['title'][i]:
       LeetCode_Problems['title'][i] = LeetCode_Problems['title'][i].replace(" ","-")


x = LeetCode_Problems['title'][t]
LeetCode_Problem = 'https://leetcode.com/problems/{}/'.format(x)

#print(LeetCode_Problem)

LeetCode = 'https://leetcode.com/problems/{}/'.format(LeetCode_Problems['title'][0])

print(LeetCode)


#print(LeetCode_Soup)
