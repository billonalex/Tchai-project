# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:01:51 2020

@author: Alexandre
"""

import requests
import json


print(requests.post('http://127.0.0.1:5000/personnes/TESTNOM/testprenom').text)
print(requests.get('http://127.0.0.1:5000/personnes').text)
print(requests.get('http://127.0.0.1:5000/personnes/1').text)