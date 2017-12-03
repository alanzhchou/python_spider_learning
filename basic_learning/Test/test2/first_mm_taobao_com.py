#/usr/bin/env python3
#-*- coding: utf-8 -*-
import requests

url = "https://mm.taobao.com/search_tstar_model.htm"

result = requests.get(url)

print(result.text)