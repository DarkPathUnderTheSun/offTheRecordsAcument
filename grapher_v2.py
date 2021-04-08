#The script f2py.exe is installed in 'C:\Users\agcruz\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
import matplotlib.pyplot as plt
import datetime

filename = "net_tests.log"

with open(filename) as f:
    content = f.readlines()

print('Analyzing Download Speed Logs...')
download = []
for line in content:
    if 'Download Speed' in line:
        if 'defaulting' in line :
            download.append(float(line.split()[5]))
        else:
            download.append(float(line.split()[2]))

print('Analyzing Upload Speed Logs...')
upload = []
for line in content:
    if 'Upload Speed' in line:
        if 'defaulting' in line :
            upload.append(float(line.split()[5]))
        else:
            upload.append(float(line.split()[2]))

print('Analyzing Packet Loss Logs...')
packetLoss = []
for line in content:
    if 'acket' in line:
        if '%' in line:
            if 'defaulting' in line:
                stringHandler = line.split()[4]
                packetLoss.append(float(stringHandler))
            else:
                stringHandler = line.split()[2]
                packetLoss.append(float(stringHandler))

print('Cleaning up Date Formats...')
dates = []
for line in content:
    if 'Network Test starting' in line:
        #dates.append(line.split()[5])
        primitiveDateTime = line.split()[4]+' '+line.split()[5]
        date_time_str = primitiveDateTime
        date_time_obj = datetime.datetime.strptime(date_time_str, "%d/%m/%Y %H:%M:%S")
        dates.append(date_time_obj)


# print(upload)
# print(download)
# print(packetLoss)
# print(dates)


# PLOT
print('Success!')
print('Plotting results...')

figure, axis = plt.subplots(2, 1)

axis[0].plot(dates,upload)
axis[0].plot(dates,download)
axis[0].set(ylabel="Mb/s")
axis[0].legend(['Upload', 'Download'])
axis[0].set_title("Internet Speed")

axis[1].plot(dates,packetLoss)
axis[1].set(xlabel="Time", ylabel="%")
axis[1].set_title("Packet Loss")

print('Plot on screen. Close plot to end program.')

plt.show()

print('All done')