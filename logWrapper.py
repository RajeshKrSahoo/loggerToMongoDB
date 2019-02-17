from LoggerToServer import *
import sys,os

"""
Created by EZSAHRA @16th Feb 2019

"""

class logWrapper(ClsLogger):
    def __init__(self,botId,botInstanceId,server,path):
        try:
            
            self.botId=botId
            self.botInstanceId=botInstanceId
            self.server=server
            self.path=path
            # self.method=method
            ClsLogger.__init__(self,self.botId,self.botInstanceId,self.server,self.path)

        except:
            e = sys.exc_info()
            logInfo = "Exception caught ="+str(e)
            print(e)
    