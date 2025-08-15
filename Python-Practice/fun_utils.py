import os
import datetime

command = "wmic diskdrive get size"
command = 'systeminfo | find "System Boot Time"'
command = "systeminfo"
command = 'date /t'
command = 'time /t'
print(os.system(command))
print("***********************")

def check_cpu(command):
    print(os.system(command))

def check_date(command):
    print(os.system(command))

def check_ram(command):
    print(os.system(command))

def check_uptime(command):
    print(os.system(command))

def check_time(command):
    return os.system(command)

check_cpu('wmic diskdrive get size')
check_date('date /t')
check_ram('systeminfo')
check_uptime('systeminfo | find "System Boot Time"')
check_time('time /t')

def run_command(command):
    return os.system(command)
run_command('date /t')


#using datetime library
def show_date():
    return datetime.datetime.today()
today = show_date()
print(today)