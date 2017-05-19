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

def config():
    config = unTar().split("!Device Configuration")[1]
    config = config.split("------------")[0]  # cutting the Configuration out of the support file.
    return config
config = config()

IP = str(ipaddress.ip_address(unicode(raw_input("Input IP Address: "))))
Mask = str(int(unicode(raw_input("Input Prefix or Subnet Mask: "))))
Interface = str(int(raw_input("Input MNG Interface Number: ")))
GW = str(ipaddress.ip_address(unicode(raw_input("Input Default Gateway: "))))

r1 = re.sub(r'net ip-interface create [0-9].*',
           "net ip-interface create " + IP + ' ' + Mask + ' ' + Interface, config)

r2 = re.sub(r'net route table create [0-9].*',
            "net route table create 0.0.0.0 0.0.0.0 " + GW + ' -i ' + Interface, config)

def snmp():
    defaultSnmp = """manage snmp groups create SNMPv2c public -gn initial
    manage snmp access create initial SNMPv2c noAuthNoPriv -rvn iso -wvn iso -nvn iso
    manage snmp views create iso 1
    manage snmp notify create allTraps -ta v3Traps
    manage snmp community create public -n public -sn public"""
    config = r2
    r1 = config.split("manage web-services status set enable")[1]
    r1 = r1.split("services auditing status set Enabled")[0]
    config = re.sub(r1, '\nd-snmp\n', config)
    config = re.sub(r'd-snmp', defaultSnmp, config)
    return config
# config = re.sub(r'manage snmp [a-z].* create .*', '', config)

print snmp()

open("Test_CFG.txt", 'wb').write(config)
