#!/usr/bin/env python

import serial
import string

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix", "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff", url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
client.connect()
sume =2
##test = serial.Serial("/dev/ttyACM0",9600)
###test.open()
##x = 0
##sume=0
##while x < 30:
##    line = test.readline()
##    test.write(line)
##
##    sume = sume + int(line)
##    print(line)
##    x = x + 1
sume=sume/30
sume1 = sume/15
sume2 = sume/5
databaseName = "coolstuff"

myDatabase = client.create_database(databaseName)

if myDatabase.exists():
   print ("'{0}' successfully created.\n".format(databaseName))

sampleData = [
   [sume, "one", "boiling"],
   [sume2, "two", "hot"],
   [sume1, "three", "warm"],
   [4, "four", "cold"],
   [5, "five", "freezing"]
 ]

# Create documents using the sample data.
# Go through each row in the array
for document in sampleData:
 # Retrieve the fields in each row.
 number = document[0]
 name = document[1]
 description = document[2]

 # Create a JSON document that represents
 # all the data in the row.
 jsonDocument = {
     "current": number,
     "nameField": name,
     "descriptionField": description
 }

 # Create a document using the Database API.
 newDocument = myDatabase.create_document(jsonDocument)

 # Check that the document exists in the database.
 if newDocument.exists():
     print ("Document '{0}' successfully created.".format(number))

#test.close()
