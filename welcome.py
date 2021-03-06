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
# Motherfuckin Data
from Data import *
from flask import request
from add_signal_db import add_signal
#import dbte
from flask import url_for, redirect
from flask import render_template

# Block of code that connects and retrieves data from database
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask,jsonify,json

# client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
#                   "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
#                   url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
# client.connect()
#
# end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
# params = {'include_docs': 'true'}
#
# response = client.r_session.get(end_point,params=params)
# table22 =response.json()['rows'][0]['doc']['current'],5,6

# code for routing begins

app = Flask(__name__)

@app.route('/')
def Welcome():
    return redirect(url_for('static', filename='index.html'))


@app.route('/registration')
def Register():
    return redirect(url_for('static', filename='registration.html'))


@app.route('/myapp')
def WelcomeToMyapp():



    client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                      "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                      url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
    client.connect()

    end_point = '{0}/{1}'.format("https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com", "coolstuff" + "/_all_docs?")
    params = {'include_docs': 'true'}

    response = client.r_session.get(end_point,params=params)
    table22 =response.json()['rows'][0]['doc']['current'],5,6
    # table22 = 4,5,6

    return render_template('tester.html', table = table22)



@app.route('/myappe')
def WelcomeToMyappe():
    dtab = getDataByMinute()
    dTime = getTimeLast()


    return render_template('graph18s.html', table = dtab, time_table = dTime)


@app.route('/myappe_load2')
def WelcomeToMyappe_load2():
    dtab = getDataBySecond("2")
    dTime = getTimeLast()


    return render_template('graph18s.html', table = dtab, time_table = dTime)


@app.route('/myappe_load3')
def WelcomeToMyappe_load3():
    dtab = getDataBySecond("3")
    dTime = getTimeLast()



    return render_template('graph18s.html', table = dtab, time_table = dTime)


@app.route('/myappe_load4')
def WelcomeToMyappe_load4():
    dtab = getDataBySecond("4")
    dTime = getTimeLast()


    return render_template('graph18s.html', table = dtab, time_table = dTime)

# code for loading cost of each load for 5 minute
###################################################

@app.route('/load1_cost_5m')
def load1Cost5min():
    dtab = getDataFor5min("1")
    dTime = getTimeLast()


    return render_template('graph18s_cost_for_5_min.html', table = dtab, time_table = dTime)


@app.route('/load2_cost_5m')
def load2Cost5min():
    # dtab = getDataFor5min("2")
    dtab = getDataFromMinTable("2")
    dTime = getTimeLast()


    return render_template('graph18s_cost_for_5_min.html', table = dtab, time_table = dTime)


@app.route('/load3_cost_5m')
def load3Cost5min():
    # dtab = getDataFor5min("3")
    dtab = getDataFromMinTable("3")
    dTime = getTimeLast()


    return render_template('graph18s_cost_for_5_min.html', table = dtab, time_table = dTime)


@app.route('/load4_cost_5m')
def load4Cost5min():
    # dtab = getDataFor5min("4")
    dtab = getDataFromMinTable("4")
    dTime = getTimeLast()


    return render_template('graph18s_cost_for_5_min.html', table = dtab, time_table = dTime)


@app.route('/myappe2')
def WelcomeToMyappe2():
    # dtab = mygData.getDataByMinute()
    dTime = getTimeLast()
    dtab = getDataFromMinTable("2")
    dtab2 = getDataFromMinTable("2")
    dtab3 = getDataFromMinTable("3")
    dtab4 = getDataFromMinTable("4")



    return render_template('graph.html', table = dtab, table2 = dtab2, table3 = dtab3, table4 = dtab4,time_table = dTime)


@app.route('/all_loads_usage_18s')
def WelcomeToMyappe3():
    # dtab = mygData.getDataByMinute()
    dTime = getTimeLast()
    dtab = getDataByMinute()
    dtab2 = getDataByMinute2()
    dtab3 = getDataByMinute3()
    dtab4 = getDataByMinute4()


    return render_template('graph_18_mult_use.html', table = dtab, table2 = dtab2, table3 = dtab3, table4 = dtab4,time_table = dTime)


@app.route('/all_loads_usage_18s_cost')
def WelcomeToMyappeCost():
    # dtab = mygData.getDataByMinute()
    dTime = getTimeLast()
    dtab = getDataByMinute()
    dtab2 = getDataByMinute2()
    dtab3 = getDataByMinute3()
    dtab4 = getDataByMinute4()






    return render_template('graph_18_mult.html', table = dtab, table2 = dtab2, table3 = dtab3, table4 = dtab4,time_table = dTime)


#############################################################################################################
# code for displaying a "mock 24 hour chart" takes last 24 data for that load and calculates usage for an hour
#############################################################################################################

@app.route('/l1_24')
def load1_24():
    dtab = getDataFor24("1")
    dTime = getTimeLast()
    total_cost = 0
    for data in dtab:
        total_cost += (data*0.000065950)


    return render_template('graph24.html', table = dtab, time_table = dTime,  cost_total= total_cost)


@app.route('/l2_24')
def load2_24():
    dtab = getDataFor24("2")
    total_cost = 0
    for data in dtab:
        total_cost += (data*0.000065950)
    dTime = getTimeLast()



    return render_template('graph24.html', table = dtab, time_table = dTime, cost_total= total_cost)


@app.route('/l3_24')
def load3_24():
    dtab = getDataFor24("3")
    total_cost = 0
    for data in dtab:
        total_cost += (data*0.000065950)
    dTime = getTimeLast()



    return render_template('graph24.html', table = dtab, time_table = dTime,  cost_total= total_cost)


@app.route('/l4_24')
def load4_24():
    dtab = getDataFor24("4")
    total_cost = 0
    for data in dtab:
        total_cost += (data*0.000065950)
    dTime = getTimeLast()



    return render_template('graph24.html', table = dtab, time_table = dTime,  cost_total= total_cost)


@app.route('/all_loads_compare')
def all_loads():
    total_cost2 = 0
    total_cost3 = 0
    total_cost4 = 0
    dtab2 = getDataFor24("2")
    for data in dtab2:
        total_cost2 += (data*0.000065950)
    dtab3 = getDataFor24("3")
    for data3 in dtab3:
        total_cost3 += (data3*0.000065950)
    dtab4 = getDataFor24("4")
    for data4 in dtab4:
        total_cost4 += (data4*0.000065950)



    return render_template('graphCmp.html', table2 = dtab2, table3 = dtab3, table4 = dtab4,    cost_total2= total_cost2, cost_total3= total_cost3, cost_total4= total_cost4 )



@app.route('/vcb')
def my_form():
    return render_template("VCB.html")


@app.route('/', methods=['POST'])
def my_form_post():
    status= 0
    status2= 1
    status3= 1
    status4= 1

#    text = request.form['text']
#    text2 = request.form['text2']
#    text3 = request.form['text3']
#    text4 = request.form['text4']
#    text = text.upper()
#    text2 = text2.upper()
#    text3 = text3.upper()
#    text4 = text4.upper()

    #value of checkbox for each load 0 or Load for On
    load1 = request.form['Load1']
    load2 = request.form['Load2']
    load3 = request.form['Load3']
    load4 = request.form['Load4']

    if load1 == "Load":
        status = 1
    else:
        status = 0
    if load2 == "Load":
        status2 = 1
    else:
        status2 = 0
    if load3 == "Load":
        status3 = 1
    else:
        status3 = 0
    if load4 == "Load":
        status4 = 1
    else:
        status4 = 0


#    if text == "ON":
#        status = 1
#    elif (text =='OFF'):
#        status = 0
#    if text2 == "ON":
#        status2 = 1
#    elif (text2 == 'OFF'):
#        status2 = 0
#    if text3 == "ON":
#        status3 = 1
#    elif (text3 == 'OFF'):
#
#        status3 = 0
#    if text4 == "ON":
#        status4 = 1
#    elif (text4 == 'OFF'):
#
#        status4 = 0

    # processed_text = text.upper()
    # if processed_text == "ON":  # the user has signal on
    #     status = 1
    # else:
    #     status = 0


    #table_name is the variable being used to determine which load to turn on/off
    # e.g status = load 1, status2= load 2
    table_name = "status"
    table_name2 = "status2"
    table_name3 = "status3"
    table_name4 = "status4"
    add_signal(status4, table_name4)
    add_signal(status3, table_name3)
    add_signal(status2, table_name2)
    add_signal(status, table_name)


    print("HERE IS THE ADD SIGNAL FUNCTION")


    #fix: return same page w updated JS
    return render_template("VCB.html")




@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)





port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
