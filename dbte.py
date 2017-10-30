#!/usr/bin/env python

import serial
import string

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from Data import MofoData
from gpio_test import turnOff, turnOn
import datetime
import smbus
import time




while(True):
    client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                      "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                      url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
    client.connect()
    # Get I2C bus
    bus = smbus.SMBus(1)

    # I2C address, 0x2A(42)
    # Command for reading device identification data
    # 0x6A(106), 0x02(2), 0x00(0),0x00(0), 0x00(0) 0x00(0), 0xFE(254)
    # Header byte-2, command-2, byte 3, 4, 5 and 6 are reserved, checksum
    command2 = [0x6A, 0x02, 0x00, 0x00, 0x00, 0x00, 0xFE]
    bus.write_i2c_block_data(0x2A, 0x92, command2)
    j = 10
    time.sleep(0.5)

    # I2C address, 0x2A(42)
    # Read data back from 0x55(85), 3 bytes
    # Type of Sensor, Maximum Current, No. of Channels
    data = bus.read_i2c_block_data(0x2A, 0x55, 3)

    # Convert the data
    typeOfSensor = data[0]
    maxvolt = data[1]
    noOfChannel = data[2]
    # I2C address, 0x2A(42)
    # Command for reading voltage
    # 0x6A(106), 0x05(5), 0x01(1),0x02(2), 0x00(0), 0x00(0) 0x04(4)
    # Header byte-2, command-5, start channel-1, stop channel-12, byte 5 and 6 reserved, checksum
    command1 = [0x6A, 0x05, 0x01, 0x02, 0x00, 0x00, 0x04]
    bus.write_i2c_block_data(0x2A, 0x92, command1)
    time.sleep(0.5)

    # I2C address, 0x2A(42)
    # Read data back from 0x55(85), No. of Channels * 3 bytes
    # current MSB1, current MSB, current LSB
    data1 = bus.read_i2c_block_data(0x2A, 0x55, 2*3)
    volts = []
    # Convert the data
    for i in range(0, 2) :
            msb1 = data1[i * 3]
            msb = data1[1 + i * 3]
            lsb = data1[2 + i * 3]

            # Convert the data to ampere
            volt = (msb1 * 65536 + msb * 256 + lsb) / 1000.0
            if volt > 100:
                    volt = volt /100
            volt = volt * 1.414213
            volts.append(volt)



    ##sume ="2"
    test = serial.Serial("/dev/ttyACM0",9600)


    #test.open()
    x = 1

    sume=0.00
    total_power=0
    kitchen_cur = 0
    kitchen_pow = 0
    kitchen_volt = 0
    total_kitchen_pow =0
    bedroom_cur = 0
    bedroom_pow = 0
    bedroom_volt = 0
    total_bedroom_pow = 0
    volts_total =0

    cur_time = datetime.datetime.now()
    awesome_cur_time = str(cur_time)
    while x < 7:
        volts = []
    # Convert the data
        for i in range(0, 2) :

            msb1 = data1[i * 3]
            msb = data1[1 + i * 3]
            lsb = data1[2 + i * 3]

            # Convert the data to ampere
            volt = (msb1 * 65536 + msb * 256 + lsb) / 1000.0
            if volt > 100:
                    volt = volt /100
            volt = volt * 1.414213
            volts.append(volt)
            print(volts[i])


        line = test.readline(4)
        test.write(line)
        if(x%2 == 1):
            #kitchen_cur = int(line)
            kitchen_pow = int(line) * volts[0]
            total_kitchen_pow = total_kitchen_pow +kitchen_pow
        if(x%2 == 0):
            #bedroom_cur = int(line)
            bedroom_pow = int(line) * volts[0]
            total_bedroom_pow = total_bedroom_pow +bedroom_pow


        power = volts[0] * int(line)
        total_power = power + total_power
        volts_total = volts[0] + volts_total

        sume = sume + int(line)
        print(line)
        x = x + 1
    total_power_avg = total_power /100 /6
    total_kitchen_avg = total_kitchen_pow/100/3
    total_bedroom_avg = total_bedroom_pow / 100/ 3
    volts_total_avg = volts_total/6
    sume=sume/6
    final_sume = sume / 100
    sume1 = sume/15
    print("power : " + str(total_power_avg))
    print("volts : " + str(volts_total_avg))
    print("kitchen : " + str(total_kitchen_avg))
    print("bedroom : " + str(total_bedroom_avg))
    print("current : " + str(final_sume))


    sume2 = sume/6
    databaseName = "coolstuff"

    myDatabase = client.create_database(databaseName)

    if myDatabase.exists():
       print ("'{0}' successfully created.\n".format(databaseName))
    print(volts[0])
    sampleData = [
       [final_sume, volts_total_avg, total_kitchen_avg, "kitchen",awesome_cur_time],
       [final_sume, 25, total_bedroom_avg,"bedroom",awesome_cur_time]
     ]

    # Create documents using the sample data.
    # Go through each row in the array
    for document in sampleData:
     # Retrieve the fields in each row.
     number = document[0]
     name = document[1]
     description = document[2]
     circuit = document[3]
     time = document[4]

     # Create a JSON document that represents
     # all the data in the row.
     jsonDocument = {
         "current": number,
         "Voltage": name,
         "Power": description,
         "Circuit" : circuit,
         "Time" : time
     }

     # Create a document using the Database API.
     newDocument = myDatabase.create_document(jsonDocument)

     # Check that the document exists in the database.
     if newDocument.exists():
         print("Document '{0}' successfully created.".format(number))
    dat_of_stat = MofoData("Davied", 999999999)
    status_circuit = dat_of_stat.getStatusCircuit()
    print(status_circuit)
    if status_circuit == 1:
        turnOn()
    else:
        turnOff()
