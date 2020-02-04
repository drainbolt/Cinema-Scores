import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db, firestore
from flask import Flask, jsonify
from flask import request
import pprint
from flask_cors import CORS

cred = credentials.Certificate("cinscdb_cert.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


'''
# get movies from db

ref = db.collection(u'movies').stream()
data = {}

def printer(refer):
    for refs in refer:
        data[refs.id] = refs.to_dict()
    json_data = json.dumps(data)
    return json_data
    
d = printer(ref)
out = open('/Users/smanikonda/Documents/cs425/CinemaScores/db.txt','w')
out.write(d)
'''
app = Flask(__name__)
CORS(app)

movie_list = {}

#search for desired movie name's details ex: /Alien
@app.route('/<mv>',methods=['GET'])
def get(mv):
    movie_deets = db.collection(u'movies').document(mv).get().to_dict()
    return movie_deets

#get all the movie titles
@app.route('/movielist',methods=['GET'])
def get_movie():
    with open('db.txt','r') as f:
        jData = json.loads(f.read())
    i = 1
    for keys in jData.keys():
        movie_list[keys] = i
        i = i + 1
    return movie_list

#get 50 movies per page ex: /movieinfo/12
@app.route('/movieinfo/<num>',methods=['GET'])
def movie_info(num):
    with open('db.txt','r') as f:
        jData = json.loads(f.read())
    if(num == "1"):
        first = {k: jData[k] for k in list(jData)[:51]}
        return first
    elif(num == "2"):
        first = {k: jData[k] for k in list(jData)[51:101]}
        return first
    elif(num == "3"):
        first = {k: jData[k] for k in list(jData)[101:151]}
        return first
    elif(num == "4"):
        first = {k: jData[k] for k in list(jData)[151:201]}
        return first
    elif(num == "5"):
        first = {k: jData[k] for k in list(jData)[201:251]}
        return first
    elif(num == "6"):
        first = {k: jData[k] for k in list(jData)[251:301]}
        return first
    elif(num == "7"):
        first = {k: jData[k] for k in list(jData)[301:351]}
        return first
    elif(num == "8"):
        first = {k: jData[k] for k in list(jData)[351:401]}
        return first
    elif(num == "9"):
        first = {k: jData[k] for k in list(jData)[401:451]}
        return first
    elif(num == "10"):
        first = {k: jData[k] for k in list(jData)[451:501]}
        return first
    elif(num == "11"):
        first = {k: jData[k] for k in list(jData)[501:551]}
        return first
    elif(num == "12"):
        first = {k: jData[k] for k in list(jData)[551:601]}
        return first
    elif(num == "13"):
        first = {k: jData[k] for k in list(jData)[601:651]}
        return first
    elif(num == "14"):
        first = {k: jData[k] for k in list(jData)[651:701]}
        return first
    elif(num == "15"):
        first = {k: jData[k] for k in list(jData)[701:751]}
        return first
    elif(num == "16"):
        first = {k: jData[k] for k in list(jData)[751:801]}
        return first
    elif(num == "17"):
        first = {k: jData[k] for k in list(jData)[801:851]}
        return first
    elif(num == "18"):
        first = {k: jData[k] for k in list(jData)[851:901]}
        return first
    elif(num == "19"):
        first = {k: jData[k] for k in list(jData)[901:951]}
        return first
    elif(num == "20"):
        first = {k: jData[k] for k in list(jData)[951:1001]}
        return first
    elif(num == "21"):
        first = {k: jData[k] for k in list(jData)[1001:1051]}
        return first
    elif(num == "22"):
        first = {k: jData[k] for k in list(jData)[1051:1101]}
        return first
    elif(num == "23"):
        first = {k: jData[k] for k in list(jData)[1101:1151]}
        return first
    elif(num == "24"):
        first = {k: jData[k] for k in list(jData)[1151:1201]}
        return first
    elif(num == "25"):
        first = {k: jData[k] for k in list(jData)[1201:1251]}
        return first
    elif(num == "26"):
        first = {k: jData[k] for k in list(jData)[1251:1301]}
        return first
    elif(num == "27"):
        first = {k: jData[k] for k in list(jData)[1301:1351]}
        return first
    elif(num == "28"):
        first = {k: jData[k] for k in list(jData)[1351:1401]}
        return first
    elif(num == "29"):
        first = {k: jData[k] for k in list(jData)[1401:1451]}
        return first
    elif(num == "30"):
        first = {k: jData[k] for k in list(jData)[1451:1501]}
        return first
    elif(num == "31"):
        first = {k: jData[k] for k in list(jData)[1501:1551]}
        return first
    elif(num == "32"):
        first = {k: jData[k] for k in list(jData)[1551:1601]}
        return first
    elif(num == "33"):
        first = {k: jData[k] for k in list(jData)[1601:1651]}
        return first
    elif(num == "34"):
        first = {k: jData[k] for k in list(jData)[1651:1701]}
        return first
    elif(num == "35"):
        first = {k: jData[k] for k in list(jData)[1701:1751]}
        return first
    elif(num == "36"):
        first = {k: jData[k] for k in list(jData)[1751:1801]}
        return first
    elif(num == "37"):
        first = {k: jData[k] for k in list(jData)[1801:1851]}
        return first
    elif(num == "38"):
        first = {k: jData[k] for k in list(jData)[1851:1901]}
        return first
    elif(num == "39"):
        first = {k: jData[k] for k in list(jData)[1901:1951]}
        return first
    elif(num == "40"):
        first = {k: jData[k] for k in list(jData)[1951:2013]}
        return first

if __name__ == '__main__':
    app.run(debug=True)

