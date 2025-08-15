import os

#print(os.system('df -h'))
#print(os.system('uptime'))
#print(os.system('free -h'))


print(os.system('wmic diskdrive get size'))
print(os.system('wmic logicaldisk get size,freespace,caption'))
print(os.system('systeminfo | find "System Boot Time"'))
print(os.system('systeminfo'))