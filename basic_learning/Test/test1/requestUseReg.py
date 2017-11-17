#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re

class RequestReg(object):
    def __init__(self):
        pass

    def getInfo(self):
        url = 'https://github.com/timeline.json'
        response1 = requests.get(url)
        header = response1.headers

        info = []
        for headerItem in header:
            temp = []
            temp.append(headerItem)
            if len(header.get(headerItem)) < 40:
                temp.append(header.get(headerItem))
            else:
                temp.append('too long')
            info.append(tuple(temp))
        info = tuple(info)
        return info