# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:45:02 2020

@author: Alexandre
"""


from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'