from tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfilename
import re
import tarfile
import ipaddress

def show_entry_fields():
    def pathOpen():
        Tk().withdraw()
        return askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    def pathSave():
        ftypes = [('Normal text file', 'txt')]
        path = asksaveasfilename(filetypes=ftypes, defaultextension='.txt')
        return path

    def unTar():
        tar = tarfile.open(pathOpen())
        f = tar.extractfile('./support.txt')  # Extracts the support.txt
        content = f.read().replace('\r\n', '\n')  # reads the content of the support.txt
        content = content.replace('\\\n', '')
        tar.close()
        return content

    config = unTar().split("!Device Configuration")[1]
    config = config.split("------------")[0]  # cutting the Configuration out of the support file.

    ip = "%s" % str(ipaddress.ip_address(unicode(e1.get())))
    mask = "%s" % (e2.get())
    interface = "%s" % (e3.get())
    gw = "%s" % str(ipaddress.ip_address(unicode(e4.get())))

    config = re.sub(r'net ip-interface create [0-9].*',
                    "net ip-interface create " + ip + ' ' + mask + ' ' + interface, config)
    config = re.sub(r'net route table create [0-9].*',
                    "net route table create 0.0.0.0 0.0.0.0 " + gw + ' -i ' + interface, config)
    config = re.sub(r'manage snmp [a-z].*', '!', config)
    config = re.sub(r'manage user table .*', '!', config)

    open(pathSave(), 'wb').write(config)

master = Tk()
Label(master, text="Input IP Address: ").grid(row=0)
Label(master, text="Input Prefix or Subnet Mask: ").grid(row=1)
Label(master, text="Input MNG Interface Number: ").grid(row=2)
Label(master, text="Input Default Gateway: ").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Go !', command=show_entry_fields).grid(row=4, column=1, sticky=W, pady=4)

mainloop()
