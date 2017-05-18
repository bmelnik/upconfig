import ipaddress
import re

text = open("x420.txt", 'rb').read().replace('\r\n', '\n')

startConfig = text.split("!Device Configuration")[1]
config = startConfig.split("------------")[0]
# r = y.split(' ')


IP = str(ipaddress.ip_address(unicode(raw_input("Input IP Address: "))))
Mask = str(int(unicode(raw_input("Input Prefix or Subnet Mask: "))))
Interface = str(int(raw_input("Input MNG Interface Number: ")))
GW = str(ipaddress.ip_address(unicode(raw_input("Input Default Gateway: "))))

r1 = re.sub(r'net ip-interface create [0-9].*',
           "net ip-interface create " + IP + ' ' + Mask + ' ' + Interface, config)

r2 = re.sub(r'net route table create [0-9].*', "net route table create 0.0.0.0 0.0.0.0 " + GW + ' -i ' + Interface, r1)


print r2

open("Test_CFG.txt", 'wb').write(r2)
# outputFile = open("Test_CFG.txt", "w")
# outputFile.write(r2)
# outputFile.close()