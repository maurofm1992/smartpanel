# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify
#import dbte
from flask import url_for, redirect
# Block of code that connects and retrieves data from database
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask,jsonify,json

client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                  "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                  url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
client.connect()

end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
params = {'include_docs': 'true'}

response = client.r_session.get(end_point,params=params)
table22 =response.json()['rows'][0]['doc']['current']

# code for routing begins

app = Flask(__name__)

@app.route('/')
def Welcome():
    # return app.send_file('static/index.html')

    return redirect(url_for('static', filename='index.html'))


@app.route('/myapp')
def WelcomeToMyapp():
    return 'Aelcome again to my app running on Bluemix!'



@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
