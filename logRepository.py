from sshtunnel import SSHTunnelForwarder
import pymongo
import gridfs
import time
import yaml
from datetime import datetime
import json
from collections import OrderedDict

class logRepository():
    """
    The Logot Repository class establishes connection to the Logger database.
    It stores the Logger information as in Audit and Debug data base.

    """
    """ Below are the db connection parameters"""
   
    def __init__(self):
        try:
            self.connection = pymongo.MongoClient('mongodb://localhost:27017/')
            self.database = self.connection["logger"]
            self.audit = self.database["audit"]
            self.debug = self.database["debug"]
        except Exception as exc:
            print ("database could not connect because")
            print (exc)

    
    def msgLogger(self,timeStamp,levelName,botId,botInstanceId,msg):
        try:
            configLogDB = {"timeStamp":timeStamp,
                    "levelName":levelName,
                    "botId":botId,
                    "botInstanceId":botInstanceId,
                    "msg":msg
            }

            print(configLogDB["timeStamp"])

            return configLogDB

        except Exception as exc:
            print ("database could not connect because")
            print (exc)


    def dbInsert(self,loggerInfo):
        try:
            cLogInfo=loggerInfo
            configLogDB={}
            ts=float(cLogInfo['created'])
            timeStamp=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
            print("\r\n")
            auditMsg=str(timeStamp)+', '+cLogInfo['levelname']+', '+cLogInfo['msg']
            logMsges=cLogInfo["msg"]
            logMsges=logMsges.split(',')
            botID=logMsges[0]
            botInstanceID=logMsges[1]

            #print(logMsges[0:2])
            #print("\r\n")
            messageLog=','.join(logMsges[2:])
            configLogDB = self.msgLogger(timeStamp,cLogInfo['levelname'],botID,botInstanceID,messageLog)
            print(configLogDB)
            #print("\r\n")
            #print(auditMsg)
            #BOOK["auditMsg"]=auditMsg
            #audit.insert(BOOK)

            if "audit" in cLogInfo['funcName']:
                self.audit.insert(configLogDB)#BOOK)
                print("\r\n")
            elif "dev" in cLogInfo['funcName']:
                self.debug.insert(configLogDB)

        except Exception as exc:
            print ("Log insertion failure")
            print (exc)

        

        
