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
            BOOK={}

            try:
                

                if "audit" in cLogInfo['funcName']:
                    ts=float(cLogInfo['created'])
                    timeStamp12=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                    print("\r\n")
                    auditMsg=str(timeStamp12)+', '+cLogInfo['levelname']+', '+cLogInfo['msg']
                    logMsges=cLogInfo["msg"]
                    logMsges=logMsges.split(',')
                    #print(logMsges[0:2])
                    #print("\r\n")
                    messageLog=','.join(logMsges[2:])
                    configLogDB_Audit = self.msgLogger(timeStamp12,cLogInfo['levelname'],logMsges[0],logMsges[1],messageLog)
                    print(configLogDB_Audit)
                    print("\r\n")
                    print(auditMsg)
                    BOOK["auditMsg"]=auditMsg
                    #audit.insert(BOOK)
                    self.audit.insert(configLogDB_Audit)#BOOK)
                    print("\r\n")

            except Exception as exc:
                print ("Audit Log insertion failure")
                print (exc)
    ##############################################################################################################


    #######For Debug report below is to create the message########################################################

            try:
                if "dev" in cLogInfo['funcName']:
                    print("hi Debug")
                    print(cLogInfo['funcName'])
                    ts1=float(cLogInfo['created'])
                    print(ts1)
                    timeStamp21=datetime.utcfromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
                    print(timeStamp21)
                    print("\r\n")
                    devMsg=str(timeStamp21)+', '+cLogInfo['levelname']+', '+cLogInfo['msg']

                    ##############*************##############
                    devlogMsges=cLogInfo["msg"]
                    devlogMsges=devlogMsges.split(',')
                    print(devlogMsges[0:2])
                    #print("\r\n")
                    devMessageLog=','.join(devlogMsges[2:])
                    configLogDB_Debug = self.msgLogger(timeStamp21,cLogInfo['levelname'],devlogMsges[0],devlogMsges[1],devMessageLog)
                    print(configLogDB_Debug)
                    ##############************###############
                    print(devMsg)
                    BOOK["debugMsg"]=devMsg
                    #debug.insert(BOOK)
                    self.debug.insert(configLogDB_Debug)
                    print("\r\n")


            except Exception as exc:
                print ("Debug Log insertion failure")
                print (exc)
            # try:
            #     self.connection.close()
                
            # except Exception as exc:
            #     print("Connection couldn't be closed",exc)

        except Exception as exc:
            print ("Log insertion failure")
            print (exc)

        


        
