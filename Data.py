from cloudant.client import Cloudant


client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                  "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                  url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
client.connect()

end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
end_point_status = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "status" + "/_all_docs?")

params = {'include_docs': 'true'}
response = client.r_session.get(end_point,params=params)
response_status = client.r_session.get(end_point_status,params=params)


class MofoData:
   'Common base class for all employees'
   empCount = 0

   def __init__(self):

      MofoData.empCount += 1



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
           if response.json()['rows'][-i]['doc']['Power'] != 0:
               table.append(response.json()['rows'][-i]['doc']['Power'])
           # table[i] = (response.json
           # table.insert(i,response.json()['rows'][i]['doc']['current'])
           i = i+1
       return table

   def getCurId (self):
       curId = response.json()['rows'][-i]['doc']['_id']

       return curId

   # def getStatusCircuit (self):
   #     if(response_status.json()['rows'][-1]['doc']['status'] == 1):
   #         return "1"
   #     else:
   #         return "0"
