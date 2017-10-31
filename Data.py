from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask,jsonify,json

client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                  "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                  url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
client.connect()

end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status" + "/_all_docs?")

params = {'include_docs': 'true'}
response = client.r_session.get(end_point,params=params)
response_status = client.r_session.get(end_point_status,params=params)

table22 =response.json()['rows'][0]['doc']['current'],5,6

class MofoData:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      MofoData.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % MofoData.empCount)


   def getTimeLast(self):
       i=0
       table = []
       while (i<7):

           table.append(response.json()['rows'][-i]['doc']['current'])
           # table[i] = (response.json
           # table.insert(i,response.json()['rows'][i]['doc']['current'])
           i = i+1
       return table


   def getDataByMinute(self):
       i=0
       table = []
       while (i<7):

           table.append(response.json()['rows'][-i]['doc']['Power'])
           # table[i] = (response.json
           # table.insert(i,response.json()['rows'][i]['doc']['current'])
           i = i+1
       return table
   def getStatusCircuit (self):
       if(response_status.json()['rows'][-1]['doc']['status'] == 1):
           response_status.json()['rows'][-1].delete()

           return "1"
       else:

           response_status.json()['rows'][-1].delete()
           return "0"
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
