import logging,sys,os,datetime
import yaml
import os
import logging.handlers
import time

# server = '127.0.0.1:5000'
# path = '/'
# method = 'GET'


class ClsLogger(object):
  
    def __init__(self,botId,botInstanceId,server,path):
        try:
            self.path=path
            self.server=server
            self.method='GET'
            self.botId=botId
            self.botInstanceId=botInstanceId
            self.auditName =  "auditLog"
            self.debugName = "debugLog"
            self.formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(message)s')
            self.task="task001"
            self.auditLevel = "info"
            self.debugLevel = "debug"
            self.audit_logger = self.setup_logger(self.auditName,self.auditLevel,self.path, self.server ,self.method)
            self.debug_logger = self.setup_logger(self.debugName,self.debugLevel,self.path, self.server ,self.method)

        except:
            e = sys.exc_info()
            logInfo = "Exception caught ="+str(e)
            print(e)
#    /         
#     def getlogPath(self):
#         return self.logDir
    def setup_logger(self,name, level, path, server ,method):
                try:
                    if(level == "info"):
                        level = logging.INFO
                    elif(level == "debug"):
                        level = logging.DEBUG
                    elif(level == "warning"):
                        level = logging.WARNING
                    elif(level == "error"):
                        level = logging.ERROR
#                     handler = logging.FileHandler(log_file)
                    handler = logging.handlers.HTTPHandler(self.server, self.path, method=self.method)
                    handler.setFormatter(self.formatter)
#                     print str(level)
                    logger = logging.getLogger(name)
                    logger.setLevel(level)
                    logger.addHandler(handler)  
                    return logger
                except:
                        e = sys.exc_info()
                        logInfo = "Exception caught ="+str(e)
                        print(e)

    def devDebug(self, logInfo, img=None, x=None, y=None):
        try:
            logInfo.replace(',',':')
            self.debug_logger.debug(str(self.botId)+','+str(self.botInstanceId)+','+str(self.task)+','+str(img)+','+str(x)+','+str(y)+','+logInfo)
        except:
            e = sys.exc_info()
            print(e)    
    def devWarning(self,logInfo, img=None, x=None, y=None):
        try:
            logInfo.replace(',',':')
            self.debug_logger.warning(str(self.botId)+','+str(self.botInstanceId)+','+str(self.task)+','+str(img)+','+str(x)+','+str(y)+','+logInfo)
        except:    
            e = sys.exc_info()
            print(e)                    
    def devError(self,logInfo, img=None, x=None, y=None):
        try:
            logInfo.replace(',',':')
            self.debug_logger.error(str(self.botId)+','+str(self.botInstanceId)+','+str(self.task)+','+str(img)+','+str(x)+','+str(y)+','+logInfo)
        except:    
            e = sys.exc_info()
            print(e)
    def auditInfo(self, logInfo, img=None,x=None, y=None):
        try:
            img=str(img)
            if img.isdigit()==True:
                y=x
                x=img
                img=None
            str(logInfo).replace(',',':')
            self.audit_logger.info(str(self.botId)+','+str(self.botInstanceId)+','+str(self.task)+','+str(img)+','+logInfo+','+str(x)+','+str(y))
        except:    
            e = sys.exc_info()
            print(e)
    def auditWarning(self,logInfo, img=None, x=None, y=None):
        try:
            logInfo.replace(',',':')
            self.audit_logger.Warning(str(self.botId)+','+str(self.botInstanceId)+','+str(self.task)+','+str(img)+','+str(x)+','+str(y)+','+logInfo)
        except:    
            e = sys.exc_info()
            print(e)
    def auditError(self,logInfo, img=None, x=None, y=None):
        try:
            logInfo.replace(',',':')
            self.audit_logger.error(str(self.botId)+','+str(self.botInstanceId)+','+str(self.task)+','+str(img)+','+str(x)+','+str(y)+','+logInfo)
        except:    
            e = sys.exc_info()
            print(e)
    def setTask(self,taskName):
        try:
            self.task=taskName
            self.audit_logger.info(str(self.task)+"started")
            self.debug_logger.debug(str(self.task)+"started")
        except:
            e = sys.exc_info()
            print(e)                

# logged=ClsLogger('botId','botInstanceId',server,path,method)
# logged.devError("Fevug")
# logged.auditInfo("Holla")

#     if (time.time-strt)>200:
#         break
