from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask,jsonify,json

client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                  "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                  url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
client.connect()

end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs")
params = {'include_docs': 'true'}

response = client.r_session.get(end_point,params=params)
print "{0}\n".format(response.json())

#for item in response:


# maurrr =['initial','1']
# x=0
# print format(response.json())
# for item in response:
#     if item[0]== '220':
#
#         maurrr[x]= item
#         x = x + 1
#
#     print item
#     if item == '"current":220':
#         print "Hello lslslslsllss"
# print maurrr



