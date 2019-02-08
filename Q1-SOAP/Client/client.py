import zeep
import json
import datetime
import subprocess


wsdl = 'http://207.23.184.72:8080/clock-sync-json/services/ClockImpl?wsdl'
client = zeep.Client(wsdl=wsdl)

startTime = datetime.datetime.now()
timeStr = client.service.getTime()
endTime = datetime.datetime.now()

rtt = endTime - startTime
offset = rtt / 2

jData = json.loads(timeStr.content)

print("Server time is {0}".format(jData['time']))
result = datetime.datetime.strptime(jData['time'], '%Y-%m-%d %H:%M:%S.%f') + offset
print("Result is {0}".format(result))
subprocess.run(["date", "-s", str(result)])



