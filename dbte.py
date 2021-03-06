#!/usr/bin/env python

import serial
import string

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from functions import *
from Data import *
from gpio_test import turnOff, turnOn
import datetime
import smbus
import time
db_id_1 = 1
db_id_2 = 1
db_id_3 = 1
db_id_4 = 1
db_id_5 = 1

#begin serial communication with arduino
test = serial.Serial("/dev/ttyACM0",9600)

def getStatusCircuit (resp, pinnum):
       print(resp.json()['rows'][-1]['doc']['status'])

       if(resp.json()['rows'][-1]['doc']['status'] == 1):
           turnOn(pinnum)
       else:
           turnOff(pinnum)

while(True):
    client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                      "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                      url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
    
    y=1
    while(y<5):
       stupi= 4           
       if y==1:
          stupi=4
       elif y==2:
          stupi = 17
       elif y==3:
          stupi = 27
       elif y==4:
          stupi = 22
       client.connect()

##       stupi= 4

       end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status" +str(y)+ "/_all_docs?")
       params = {'include_docs': 'true'}

       response_status = client.r_session.get(end_point_status,params=params)
       
       getStatusCircuit(response_status, stupi)
##       client.disconnect()
       y= y+1


##    #pass a response endpoint and check to see if the value is  0 or 1
##
##    print("Before GET Status Circuit")
##    getStatusCircuit(response_status, 4)
##    getStatusCircuit(response_status2, 17)
##    getStatusCircuit(response_status3, 27)
##    getStatusCircuit(response_status4, 22)
##    getStatusCircuit(response_status5, 4)
    def calculate_power():
        volts = getVolts()
        line = test.readline(4)
        pow_calc = int(line) * volts[0]
        return pow_calc


##
##
##    x = 1
##    while x<5:
##        load_pow = calculate_power()
##
##        print(x)
##        print(load_pow)
##
##        x = x + 1




    x = 0
    loads = []
    sume=0.00
    total_power=0
    #kitchen = = load1
    kitchen_cur = 0
    kitchen_pow = 0
    kitchen_volt = 0
    total_kitchen_pow =0
    load3_cur = 0
    load3_pow = 0
    load3_volt = 0
    total_load3_pow =0
    load4_cur = 0
    load4_pow = 0
    load4_volt = 0
    total_load4_pow =0
    bedroom_cur = 0
    bedroom_pow = 0
    bedroom_volt = 0
    total_bedroom_pow = 0
    volts_total =0
    flager =False
    cur_time = datetime.datetime.now()
    awesome_cur_time = str(cur_time)
    q=0
    while (q<4):
       line = test.readline(4)
       if line == "load":
           line = test.readline(4)   
           break
    while x < 5:

           
        volts = getVolts()

        
        

        #test.write(line)
        if(x == 1):
            #kitchen_cur = int(line)
            kitchen_pow = int(line) * volts[0]
            total_kitchen_pow = total_kitchen_pow +kitchen_pow
        if(x == 2):
            #bedroom_cur = int(line)
            bedroom_pow = int(line) * volts[0]
            total_bedroom_pow = total_bedroom_pow +bedroom_pow
        if(x == 3):
            #bedroom_cur = int(line)
            load3_pow = int(line) * volts[0]
            total_load3_pow = total_load3_pow +load3_pow
        if(x == 4):
            #bedroom_cur = int(line)
            load4_pow = int(line) * volts[0]
            total_load4_pow = total_load4_pow +load4_pow
        power = volts[0] * int(line)
        total_power = power + total_power
        volts_total = volts[0] + volts_total

        sume = sume + int(line)
        print("current = " + str(float(line)/100) + "A\n")
        x = x + 1
        line = test.readline(4)



    total_power_avg = total_power /100 /4
    total_kitchen_avg = total_kitchen_pow/100
    total_bedroom_avg = total_bedroom_pow / 100
    total_load3_avg = total_load3_pow / 100
    total_load4_avg = total_load4_pow / 100
    volts_total_avg = volts_total/6
    sume=sume/6
    final_sume = sume / 100
    sume1 = sume/15
    print("Avg power : " + str(total_power_avg))
    print("Avg volts : " + str(volts_total_avg))
    print("Avg Load 1 : " + str(total_kitchen_avg) + "  W")
    print("Avg Load 2 : " + str(total_bedroom_avg) + "  W")
    print("Avg Load 3 : " + str(total_load3_avg) + "  W")
    print("Avg Load 4 : " + str(total_load4_avg) + "  W")
    print("Avg current : " + str(final_sume))

    #calls create db funct in functions
    myDatabase = create_db("coolstuff")
    myDatabase_load_2 = create_db("load2")
    myDatabase_load_3 = create_db("load3")
    myDatabase_load_4 = create_db("load4")





    sume2 = sume/6

    print(volts[0])
    sampleData = [
       [final_sume, volts_total_avg, total_kitchen_avg, "kitchen",awesome_cur_time, db_id_1]
     ]
    sampleData_load_2 = [
       [final_sume, 25, total_bedroom_avg,"bedroom",awesome_cur_time, db_id_2]
     ]
    sampleData_load_3 = [
       [final_sume, 25, total_load3_avg,"load 3",awesome_cur_time, db_id_3]
     ]
    sampleData_load_4 = [
       [final_sume, 25, total_load4_avg,"load 4",awesome_cur_time, db_id_4]
     ]


    # Create docummments using the sample data.
    # Go through each row in the array
    for document in sampleData:
     # Retrieve the fields in each row.
     number = document[0]
     name = document[1]
     description = document[2]
     circuit = document[3]
     time = document[4]
     db_id_1 = document[5]

    for document in sampleData_load_2:
     # Retrieve the fields in each row.
     number_load_2 = document[0]
     name_load_2 = document[1]
     description_load_2 = document[2]
     circuit_load_2 = document[3]
     time_load_2 = document[4]
     db_id_2 = document[5]

    for document in sampleData_load_3:
     # Retrieve the fields in each row.
     number_load_3 = document[0]
     name_load_3 = document[1]
     description_load_3 = document[2]
     circuit_load_3 = document[3]
     time_load_3 = document[4]
     db_id_3 = document[5]


    for document in sampleData_load_4:
     # Retrieve the fields in each row.
     number_load_4 = document[0]
     name_load_4 = document[1]
     description_load_4 = document[2]
     circuit_load_4 = document[3]
     time_load_4 = document[4]
     db_id_4 = document[5]


     # Create a JSON document that represents
     # all the data in the row.
     jsonDocument = {
         "current": number,
         "Voltage": name,
         "Power": description,
         "Circuit" : circuit,
         "Time" : time,
         "_id" : time
     }


     jsonDocument_load_2 = {
         "current": number_load_2,
         "Voltage": name_load_2,
         "Power": description_load_2,
         "Circuit" : circuit_load_2,
         "Time" : time_load_2,
         "_id" : time
     }
     jsonDocument_load_3 = {
         "current": number_load_3,
         "Voltage": name_load_3,
         "Power": description_load_3,
         "Circuit" : circuit_load_3,
         "Time" : time_load_3,
         "_id" : time
     }

     jsonDocument_load_4 = {
         "current": number_load_4,
         "Voltage": name_load_4,
         "Power": description_load_4,
         "Circuit" : circuit_load_4,
         "Time" : time_load_4,
         "_id" : time
     }

     # Create a document using the Database API.
     newDocument = myDatabase.create_document(jsonDocument)
     newDocument_load_2 = myDatabase_load_2.create_document(jsonDocument_load_2)
     newDocument_load_3 = myDatabase_load_3.create_document(jsonDocument_load_3)
     newDocument_load_4 = myDatabase_load_4.create_document(jsonDocument_load_4)

    #increasing include_docs
    db_id_1 += 1
    db_id_2 += 1
    db_id_3 += 1
    db_id_4 += 1
    db_id_5 += 1
    # dat_of_stat =  MofoData()
    # status_circuit = dat_of_stat.getStatusCircuit()
    # print(status_circuit)
    # if status_circuit == '1':
    #     turnOn()
    # else:
    #     turnOff()
    client.disconnect()
