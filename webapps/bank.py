#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

import redis

r = redis.Redis(host="redis")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bank/<name>')
def super_marketing(name):
    result = "bank for %s" % name
    r.sadd('bank',name) 
    return result 

@app.route('/get')
def get_keys():
    res = ""
    for bank in r.smembers('bank'):
        res = res + ' ' + bank
    return res

if __name__ == "__main__":
    app.run('0.0.0.0')
