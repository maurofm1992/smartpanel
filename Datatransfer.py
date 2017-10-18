#!/usr/bin/env python

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from pprint import pprint
from flask import Flask,jsonify,json

client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                  "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                  url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
client.connect()

end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
params = {'include_docs': 'true'}

response = client.r_session.get(end_point,params=params)
#print ("{0}\n".format(response.json()))

print (pprint (response.json()))
table22 =response.json()['rows'][0]['doc']['current']

# hel = table22.get('current')
print (table22)
# print ((hel))






