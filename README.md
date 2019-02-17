# <font color="red"> loggerToMongoDB </font>
Sending log information from multiple client BOTs via flask server to store in mongoDB  (Audit and Debug Database) using Python

## Architecture:
> There may be question why we need intermediate Server? when we can directly send the log data to mongoDB using Python modules ? and The answer is for the security and to avoid repeated connection to db we used this architcture
> Here we are sending multiple log information(Audit and Debug log infomration) from multiple automation BOTs at a time and the it goes to Flask server from where it passes to mongoDB and stored according to Audit or Debug log infomraition audit aand debug database

### Architecture for Logging into MongoDB using Python

![logtomongodatabase 1](https://user-images.githubusercontent.com/27301175/52909701-e2136480-32b2-11e9-9dea-2560813dfd1b.jpg)
