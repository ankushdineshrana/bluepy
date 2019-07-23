import time
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)


    def HandleDiscovery(self,dev,new_dev,new_dat):
        if new_dev:
            pass
        if new_dat:
            pass
        
scanner = Scanner().withDelegate(ScanDelegate())

time_diff = 0
first_time = 1
while 1:
    try:
        devices = scanner.scan(0.3)
#        print("Amount of Devices = "+str(len(devices)))
        for ii in devices:
#            print(ii.addr)
            if ii.addr =='ce:d2:dd:27:f2:67' and ii.rssi>-60:
                #print((ii.rssi))
		print("BLE tag ("+str(ii.addr)+") present in Room 1 with SSI = "+str(ii.rssi))
                if first_time == 1:
                    first_time = 0
                    pass
                else:
                    time_diff = time.time()-time_prev
                    

                
                time_prev = time.time()
                rssi_prev = ii.rssi
                continue

    except:
        continue
