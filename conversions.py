import string

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

def getDataFor5min(load):
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load" + load+"/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)

   i=1
   table = []
   while (i<2):
       #make a function that adds all the data for past min
       #each db entry is an average of 3 seconds
       # there are 60/3 entries in a min
       if i==1:
           x=1
       else:
           x= (i-1)*60
       total_power_for_one_min = 0
       while (x< 60*i):
           total_power_for_one_min += response.json()['rows'][-x]['doc']['Power']
           x += 1

           #since we are getting the average for 3 seconds we are only getting
           #20 seconds worth of total power so multiply by 3 and you get one minute

       table.append(total_power_for_one_min)
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   client.disconnect()

   return table

while(True):
    client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                      "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                      url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
    client.connect()
    l2 =getDataFor5min("2")
    l3 = getDataFor5min("3")
    l4 = getDataFor5min("4")

    cur_time = datetime.datetime.now()
    awesome_cur_time = str(cur_time)

    myDatabase_load_2 = create_db("load2_min")
    myDatabase_load_3 = create_db("load3_min")
    myDatabase_load_4 = create_db("load4_min")





    sampleData_load_2 = [
       [l2, awesome_cur_time]
     ]
    sampleData_load_3 = [
       [l3, awesome_cur_time]
     ]
    sampleData_load_4 = [
       [l4, awesome_cur_time]
     ]


    # Create docummments using the sample data.
    # Go through each row in the array

    for document in sampleData_load_2:
     # Retrieve the fields in each row.
     number_load_2 = document[0]
     time_load_2 = document[1]

    for document in sampleData_load_3:
     # Retrieve the fields in each row.
     number_load_3 = document[0]
     time_load_3 = document[1]

    for document in sampleData_load_4:
     # Retrieve the fields in each row.
     number_load_4 = document[0]
     time_load_4 = document[1]


     # Create a JSON document that represents
     # all the data in the row.



     jsonDocument_load_2 = {
         "data": number_load_2,
         "_id" : time
     }
     jsonDocument_load_3 = {
         "data": number_load_3,
         "_id" : time
     }

     jsonDocument_load_4 = {
         "data": number_load_4,
         "_id" : time
     }

     # Create a document using the Database API.
     newDocument_load_2 = myDatabase_load_2.create_document(jsonDocument_load_2)
     newDocument_load_3 = myDatabase_load_3.create_document(jsonDocument_load_3)
     newDocument_load_4 = myDatabase_load_4.create_document(jsonDocument_load_4)

    #increasing include_docs

    # dat_of_stat =  MofoData()
    # status_circuit = dat_of_stat.getStatusCircuit()
    # print(status_circuit)
    # if status_circuit == '1':
    #     turnOn()
    # else:
    #     turnOff()
    client.disconnect()
