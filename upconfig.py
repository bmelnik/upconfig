import re
import tarfile
import ipaddress
from Tkinter import Tk
from tkFileDialog import askopenfilename


def path():
    Tk().withdraw()
    return askopenfilename()  # show an "Open" dialog box and return the path to the selected file

def unTar():
    tar = tarfile.open(path())
    f = tar.extractfile('./support.txt')  # Extracts the support.txt
    content = f.read().replace('\r\n', '\n')  # reads the content of the support.txt
    content = content.replace('\\\n', '')
    tar.close()
    return content


## Change number 1

startConfig = unTar().split("!Device Configuration")[1]
config = startConfig.split("------------")[0]  # cutting the Configuration out of the support file.

IP = str(ipaddress.ip_address(unicode(raw_input("Input IP Address: "))))
Mask = str(int(unicode(raw_input("Input Prefix or Subnet Mask: "))))
Interface = str(int(raw_input("Input MNG Interface Number: ")))
GW = str(ipaddress.ip_address(unicode(raw_input("Input Default Gateway: "))))

r1 = re.sub(r'net ip-interface create [0-9].*',
           "net ip-interface create " + IP + ' ' + Mask + ' ' + Interface, config)

r2 = re.sub(r'net route table create [0-9].*', "net route table create 0.0.0.0 0.0.0.0 " + GW + ' -i ' + Interface, r1)

r3 = re.sub(r'')




print r2

open("Test_CFG.txt", 'wb').write(r2)
outputFile = open("Test_CFG.txt", "w")
outputFile.write(r2)
outputFile.close()