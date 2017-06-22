'''
Created on Jun 21, 2017

@author: Shrikanth
'''
from subprocess import Popen, PIPE

#finding connected android device id works only for Android
def find_device_id():
    stdout, stderr = execute_cmd("adb devices")
    stdout = stdout.strip()
    adb_output = stdout.split("\n")
    for device_string in adb_output:
        if "\tdevice" in device_string:
            device_id = device_string.replace("\tdevice", "").strip()
            return device_id
    return None

def execute_cmd(cmd):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    return p.communicate()

if __name__ == '__main__':
    find_device_id()
    print "Here"