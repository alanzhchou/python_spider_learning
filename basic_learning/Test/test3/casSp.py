#/usr/bin/env python3
#-*- coding: utf-8 -*-

# __author__: ZH-AlanChou
# __time__: 2017/12/10
# __version__: 1.0
import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

casCookie = dict(cas_temp='J4CCWHcjYrsJdKQ7iHO7cagRigE91IRJaTBsyfGVLi0=',TGC='eyJhbGciOiJIUzUxMiJ9.WlhsS05tRllRV2xQYVVwRlVsVlphVXhEU21oaVIyTnBUMmxLYTJGWVNXbE1RMHBzWW0xTmFVOXBTa0pOVkVrMFVUQktSRXhWYUZSTmFsVXlTVzR3TGk1NFpsb3dXbFV4T0dVd2EwUkNielo1VkU5QmVFWjNMbmxIUm5jeU5GcHJPV0ZaWTFWdGEwdGFZVkUxU0V0R1EzQjJhelpTYzBOVWEwRXlWVzlYWnpOT1ptNWxkV0pJUnpsWE4ycGtXVzFwUVVSRFNtNXFTVlJyYVRsRWFrdzVkRmRSTVdKblluZzJUSGh1UmsxMlYyeG9aWGhhZUMweWVVUjVWRUpCYWt4UVoycElNVzlIY1RGblFreHlTMkZNWVZnMVpFeFlieTEzT1VweGFYZHhRMEZLTUMxU05HOWtRbXgxVWxwRUxTMDFReTFmTlZaRlIwVllaRGhwVW1RM1lrRTFWM05LYlc1bU9HWlJZMlJYVmpsWVNrNXhUMDVQZGxwVldHNUVlR2wwY1ZBMlNWVjZlRmhWVDFJd1IwRXVZbWRsVDNSVlNrTTRUak5EYzFaYWFUWnhVV1ZWVVE9PQ.2gjTI5yorupWEspbZ78TbOOfKCZz6vSQGEG2ucGTedvbQgima6X4u6lWVbU9TZZ4nU0Adye1EmlY5OD1kntNsw',JSESSIONID='915F19CC57C258F75578321575340165', pgv_pvi='8415312896', Hm_lvt_6a98cecfe3e66904991232e6b5573cd9='1511448499,1512071090,1512142458,1512470165',UM_distinctid='15d7abbc43533-0bcbebb628f27f8-12646f4a-1fa400-15d7abbc436271')
sakaiCookie = dict(pgv_pvi='8415312896',Hm_lvt_6a98cecfe3e66904991232e6b5573cd9='1511448499,1512071090,1512142458,1512470165',UM_distinctid='15d7abbc43533-0bcbebb628f27f8-12646f4a-1fa400-15d7abbc436271',JSESSIONID='7e91d7ec-7c8c-4973-9984-dd3966da2b9b.server2')

url = 'http://sakai.sustc.edu.cn/portal/site/%7E11510629/page/'
session = requests.session()
req = session.get(url,headers=header,cookies=sakaiCookie)

soup = BeautifulSoup(req.text,"lxml")
print(soup.find('a',attrs={'id':'loginUser'}).text)