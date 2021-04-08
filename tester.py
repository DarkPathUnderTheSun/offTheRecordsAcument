import speedtest
from datetime import datetime
from subprocess import check_output
from time import sleep

logBuffer = []
print('---------- Starting Network Tester ---------\n')
print('Programmed by Carlos Morin for Acument Global Technologies')
logBuffer.append('---------- Starting Network Tester ---------\n')
with open('net_tests.log', 'a') as log:
  log.write('\n'.join(logBuffer))

while True:
  try:
    logBuffer = []
    
    now = datetime.now()
    format = "%d/%m/%Y %H:%M:%S"
    testStartDate = now.strftime(format)
    stringBuffer = ('Network Test starting at ' + testStartDate)
    print(stringBuffer)
    logBuffer.append(stringBuffer)
    
    try:
      stringBuffer = 'Testing for Packet Loss...'
      print(stringBuffer)
      logBuffer.append(stringBuffer)
      ping = check_output('ping /n 100 ns1.telstra.net', shell=True).decode()
      packetLoss = ping[ping.find('(')+1:ping.find('%')]
      stringBuffer = ('Packet Loss: ' + str(packetLoss) + ' %')
      print(stringBuffer)
      logBuffer.append(stringBuffer)
    except:
      stringBuffer = 'Not connected, defaulting to 100% packet loss'
      print(stringBuffer)
      logBuffer.append(stringBuffer)
      packetLoss = 100
    
    try:
      stringBuffer = 'Testing download speed...'
      print(stringBuffer)
      logBuffer.append(stringBuffer)
      tester = speedtest.Speedtest()
      downloadSpeed = round(tester.download()/1000000, 2)
      stringBuffer = ('Download Speed: ' + str(downloadSpeed) + ' Mb/s')
      print(stringBuffer)
      logBuffer.append(stringBuffer)
    except:
      print('Error, defaulting Download Speed to 0 Mb/s')
      logBuffer.append('Error, defaulting Download Speed to 0 Mb/s')
      downloadSpeed = 0
    
    try:
      stringBuffer = 'Testing upload speed...'
      print(stringBuffer)
      logBuffer.append(stringBuffer)
      tester = speedtest.Speedtest()
      uploadSpeed = round(tester.upload()/1000000, 2)
      stringBuffer = ('Upload Speed: ' + str(uploadSpeed) + ' Mb/s')
      print(stringBuffer)
      logBuffer.append(stringBuffer)
    except:
      stringBuffer = 'Error, defaulting Upload Speed to 0 Mb/s'
      print(stringBuffer)
      logBuffer.append(stringBuffer)
      uploadSpeed = 0
    
    now = datetime.now()
    testEndDate = now.strftime(format)
    stringBuffer = ('Network Test finished at ' + testEndDate)
    print(stringBuffer)
    logBuffer.append(stringBuffer)
    
    print('--------------------------------------------\n')
    logBuffer.append('--------------------------------------------\n')
    
    logBuffer.insert(0, '')
    with open('net_tests.log', 'a') as log:
      log.write('\n'.join(logBuffer))

    sleep(600)
  
  except KeyboardInterrupt:
    logBuffer = []
    stringBuffer = "Network Tester interrupted. If a user did this, you can ignore this message.\n"
    print(stringBuffer)
    logBuffer.append(stringBuffer)

    now = datetime.now()
    format = "%d/%m/%Y %H:%M:%S"
    errorDate = now.strftime(format)
    stringBuffer = ('Tester terminated at ' + testStartDate)
    print(stringBuffer)
    logBuffer.append(stringBuffer)
    stringBuffer = ('--------------------------------------------\n')
    print(stringBuffer)
    logBuffer.append(stringBuffer)

    logBuffer.insert(0, '')
    with open('net_tests.log', 'a') as log:
      log.write('\n'.join(logBuffer))
    
    raise
