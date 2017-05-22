import re
import tarfile
import ipaddress
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfilename
import Tkinter, Tkconstants, tkFileDialog
import Tkinter
import Tkconstants
import tkMessageBox
import tkFileDialog


def pathOpen():
    Tk().withdraw()
    return askopenfilename()  # show an "Open" dialog box and return the path to the selected file

def unTar():
    tar = tarfile.open(pathOpen())
    f = tar.extractfile('./support.txt')  # Extracts the support.txt
    content = f.read().replace('\r\n', '\n')  # reads the content of the support.txt
    content = content.replace('\\\n', '')
    tar.close()
    return content



config = unTar().split("!Device Configuration")[1]
config = config.split("------------")[0]  # cutting the Configuration out of the support file.


IP = str(ipaddress.ip_address(unicode(raw_input("Input IP Address: "))))
Mask = str(int(unicode(raw_input("Input Prefix or Subnet Mask: "))))
Interface = str(int(raw_input("Input MNG Interface Number: ")))
GW = str(ipaddress.ip_address(unicode(raw_input("Input Default Gateway: "))))


config = re.sub(r'net ip-interface create [0-9].*',
           "net ip-interface create " + var1(IP) + ' ' + Mask + ' ' + Interface, config)
config = re.sub(r'net route table create [0-9].*',
            "net route table create 0.0.0.0 0.0.0.0 " + GW + ' -i ' + Interface, config)
config = re.sub(r'manage snmp [a-z].*', '', config)
config = re.sub(r'manage user table .*', '', config)


open("test_cfg", 'wb').write(config)
