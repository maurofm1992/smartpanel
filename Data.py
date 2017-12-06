from cloudant.client import Cloudant



def getTimeLast():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
   end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)
   response_status = client.r_session.get(end_point_status,params=params)
   i=1
   table = []
   while (i<7):

       table.append(response.json()['rows'][-i]['doc']['current'])
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   client.disconnect()

   return table

#actually currently ref get data by 3 second
def getDataByMinute():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
   end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)
   response_status = client.r_session.get(end_point_status,params=params)
   i=1
   table = []
   while (i<7):
       table.append(response.json()['rows'][-i]['doc']['Power'])
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   client.disconnect()
   return table

def getDataByMinute2():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load2" + "/_all_docs?")
   end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status2" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)
   response_status = client.r_session.get(end_point_status,params=params)
   i=1
   table = []
   while (i<7):
       table.append(response.json()['rows'][-i]['doc']['Power'])
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   client.disconnect()
   return table

def getDataByMinute3():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load3" + "/_all_docs?")
   end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status3" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)
   response_status = client.r_session.get(end_point_status,params=params)
   i=1
   table = []
   while (i<7):
       table.append(response.json()['rows'][-i]['doc']['Power'])
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   return table

def getDataByMinute4():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load4" + "/_all_docs?")
   end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status4" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)
   response_status = client.r_session.get(end_point_status,params=params)
   i=1
   table = []
   while (i<7):
       table.append(response.json()['rows'][-i]['doc']['Power'])
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1

   client.disconnect()
   return table


def getDataBySecond(load):
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load" + load+"/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)

   i=1
   table = []
   while (i<7):
       #make a function that adds all the data for past min
       #each db entry is an average of 3 seconds
       # there are 60/3 entries in a min
       if i==1:
           x=1
       else:
           x= (2*(i-1))
       total_power_for_one_min = 0
       while (x< 2*i):
           total_power_for_one_min += response.json()['rows'][-x]['doc']['Power']
           x += 1

           #since we are getting the average for 3 seconds we are only getting
           #20 seconds worth of total power so multiply by 3 and you get one minute

       table.append(total_power_for_one_min * 1)
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   client.disconnect()

   return table






def getDataByMin():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)

   i=1
   table = []
   while (i<7):
       #make a function that adds all the data for past min
       #each db entry is an average of 3 seconds
       # there are 60/3 entries in a min
       if i==1:
           x=1
       else:
           x= (20*(i-1))
       total_power_for_one_min = 0
       while (x< 20*i):
           total_power_for_one_min += response.json()['rows'][-x]['doc']['Power']
           x += 1

           #since we are getting the average for 3 seconds we are only getting
           #20 seconds worth of total power so multiply by 3 and you get one minute

       table.append(total_power_for_one_min * 3)
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   client.disconnect()

   return table

def getDataByMin2():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load2" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)

   i=1
   table = []
   while (i<7):
       #make a function that adds all the data for past min
       #each db entry is an average of 3 seconds
       # there are 60/3 entries in a min
       if i==1:
           x=1
       else:
           x= (20*(i-1))
       total_power_for_one_min = 0
       while (x< 20*i):
           total_power_for_one_min += response.json()['rows'][-x]['doc']['Power']
           x += 1

           #since we are getting the average for 3 seconds we are only getting
           #20 seconds worth of total power so multiply by 3 and you get one minute

       table.append(total_power_for_one_min * 3)
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   client.disconnect()

   return table

def getDataByMin3():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load3" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)

   i=1
   table = []
   while (i<7):
       #make a function that adds all the data for past min
       #each db entry is an average of 3 seconds
       # there are 60/3 entries in a min
       if i==1:
           x=1
       else:
           x= (20*(i-1))
       total_power_for_one_min = 0
       while (x< 20*i):
           total_power_for_one_min += response.json()['rows'][-x]['doc']['Power']
           x += 1

           #since we are getting the average for 3 seconds we are only getting
           #20 seconds worth of total power so multiply by 3 and you get one minute

       table.append(total_power_for_one_min * 3)
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   return table



def getDataByMin4():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load4" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)

   i=1
   table = []
   while (i<7):
       #make a function that adds all the data for past min
       #each db entry is an average of 3 seconds
       # there are 60/3 entries in a min
       if i==1:
           x=1
       else:
           x= (20*(i-1))
       total_power_for_one_min = 0
       while (x< 20*i):
           total_power_for_one_min += response.json()['rows'][-x]['doc']['Power']
           x += 1

           #since we are getting the average for 3 seconds we are only getting
           #20 seconds worth of total power so multiply by 3 and you get one minute

       table.append(total_power_for_one_min * 3)
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   return table



def getDataByMin2():
   client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                     "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                     url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
   client.connect()

   end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "load2" + "/_all_docs?")

   params = {'include_docs': 'true'}
   response = client.r_session.get(end_point,params=params)

   i=1
   table = []
   while (i<7):
       #make a function that adds all the data for past min
       #each db entry is an average of 3 seconds
       # there are 60/3 entries in a min
       if i==1:
           x=1
       else:
           x= (20*(i-1))
       total_power_for_one_min = 0
       while (x< 20*i):
           total_power_for_one_min += response.json()['rows'][-x]['doc']['Power']
           x += 1

           #since we are getting the average for 3 seconds we are only getting
           #20 seconds worth of total power so multiply by 3 and you get one minute

       table.append(total_power_for_one_min * 3)
       # table[i] = (response.json
       # table.insert(i,response.json()['rows'][i]['doc']['current'])
       i = i+1
   return table





def getCurId ():
   curId = response.json()['rows'][-i]['doc']['_id']

   return curId

# def getStatusCircuit (self):
#     if(response_status.json()['rows'][-1]['doc']['status'] == 1):
#         return "1"
#     else:
#         return "0"
