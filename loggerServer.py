
from flask import Flask, request
from datetime import datetime
import pymongo
from logRepository import *


'''
Created on 13th Feb 2019 @EZSAHRA
'''

sendLog=logRepository()

### Program for Creating server sending to mongoDB for sending Logger ###


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])  #Working for GET here an dGET in LoggerToServer
def loggerServer():
    #print(request.args.items())
    my_list=request.args.items()
    cLogInfo=dict(my_list)
    print(cLogInfo)
    
    try:
        sendLog.dbInsert(cLogInfo)
    except Exception as exc:
        print("Error {0} while sending Log to db".format(exc))

    # connection = pymongo.MongoClient('mongodb://mongo-admin:boteyeDB@127.0.0.1:27017/admin')
    return 'response'

if __name__ == "__main__":
    app.run(debug=True)



