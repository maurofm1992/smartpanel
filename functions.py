import datetime
import smbus
import time
import serial
import string


# Get I2C bus
bus = smbus.SMBus(1)

# I2C address, 0x2A(42)
# Command for reading device identification data
# 0x6A(106), 0x02(2), 0x00(0),0x00(0), 0x00(0) 0x00(0), 0xFE(254)
# Header byte-2, command-2, byte 3, 4, 5 and 6 are reserved, checksum
command2 = [0x6A, 0x02, 0x00, 0x00, 0x00, 0x00, 0xFE]
bus.write_i2c_block_data(0x2A, 0x92, command2)
j = 10
#time.sleep(0.5)

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
#time.sleep(0.5)

# I2C address, 0x2A(42)
# Read data back from 0x55(85), No. of Channels * 3 bytes
# current MSB1, current MSB, current LSB
data1 = bus.read_i2c_block_data(0x2A, 0x55, 2*3)


def getVolts ():
    volts = []
# Convert the data
    for i in range(0, 2) :

        msb1 = data1[i * 3]
        msb = data1[1 + i * 3]
        lsb = data1[2 + i * 3]

        # Convert the data to ampere
        volt = (msb1 * 65536 + msb * 256 + lsb) / 1000.0
        if volt > 130:
                 volt = volt /100
        if volt<90 and volt>80:
            volt = volt * 1.414213
        # volt = volt * 1.414213
        if volt<118:
            volt = volt * 1.0173
        volts.append(volt)
        print("CHANNEL = " )
        i = i+1
        print(i )
        i=i-1
        print(str(volts[i])+ "  V\n")
    return volts
