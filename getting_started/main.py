#!/usr/bin/env python3
# encoding: utf-8
# main.py in sanic-demos
# Created by maverick on 2018-12-29, 20:28
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: main.py
@time: 2018-12-29 20:28
"""

from sanic import Sanic
from sanic.response import json
from sanic.request import Request

app: Sanic = Sanic()

@app.route("/")
async def test(request: Request):   # annotation
    return json({"Hello": "World"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8888)