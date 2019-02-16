# loggerToMongoDB
Sending Log information from client to Server and from Server to mongoDB using Python

# Below is the whole architecture

As per the Architecture the Log information first goes from Client log to the HTTP Server using GET PUSH methods and then after that goes to mongoDB data base. 
We Created Logger Database within which two collections present which is used to story Audit Log data and Debug log Data.
> Logger: 1) Audit 2)Debug

# Why Use server in between while you can directly send to mongoDB ?
> For security reason of the mongoDB this steps is very good by avoiding direct connection/push of logs into mongo

