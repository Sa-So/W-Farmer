#cd Library/Android/sdk/platform-tools
#./adb pair 192.168.0.90:port
#pair code

from ppadb.client import Client as AdbClient
import time as t
import pyautogui as p
from pass_code import password as pw

# Default is "127.0.0.1" and 5037
adb = AdbClient(host="127.0.0.1", port=5037)
#print(adb.version())
devices=adb.devices()
print(devices)
device=devices[0]

#image = device.screencap()
#with open('screen_cap1.png','wb') as f:
#    f.write(image)

def unlock():
    #device.shell('input touchscreen swipe 500 1235 500')
    #device.shell('input touchscreen swipe 500 1235 500')
    #double tap to wake not working ?!
    device.shell('input keyevent 26')
    t.sleep(1)
    device.shell('input touchscreen swipe 500 1200 500 500 1000')
    device.shell('input text '+pw)

def lock_unlock():
    device.shell('input keyevent 26')
    t.sleep(5)
    unlock()
    
def open_bs():
    device.shell('input touchscreen tap 576 2340')
    t.sleep(1)
    device.shell('input touchscreen tap 150 635')
    t.sleep(10)
    print('bs opened')
    
def dnd():
    device.shell('input touchscreen tap 2150 95')
    t.sleep(1)
    device.shell('input touchscreen tap 777 850')
    t.sleep(1)
    print('dnd on')
    
def play():
    print('playing')
    for i in range(350):
        device.shell('input touchscreen tap 2300 950')
        t.sleep(3)
        device.shell('input touchscreen tap 1891 1000')
        if(i%15==0):
            #gadget
            #device.shell('input touchscreen tap 1858 535')
            #t.sleep(1)
            ti=t.time()
            print(t.ctime(ti),i)
            #time elapsed and left 
        if(i%35==0):
            p.moveTo(500,500,2)
            #to keep laptop active
            

if len(devices) == 0:
    print('no devices')
    quit()


#unlock()
#open_bs()
#dnd()
#play()
#30287 340-1621/3430
#30
