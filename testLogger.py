
from logWrapper import *
import time
import sys

server = '127.0.0.1:5000'
path = '/'
method = 'GET'


logged=logWrapper("id034","botInstance034",server,path,method)



strt=time.time()
process=1

while True:
    print("Event 1, Process number:",process)
    logged.auditInfo("Testing 4")
    time.sleep(3)
    print("Event 1, Process number:",process)
    logged.devError("Debug and Information")
    time.sleep(2)
    process+=1
    print(strt)

    if (time.time()-strt)>=200:
        break