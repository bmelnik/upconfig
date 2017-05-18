
text = open("HT.txt", 'rb').read().replace('\r\n', '\n')
open("Test_CFG.txt", 'wb').write(text)

inputfile = open("Test_CFG.txt", "r")
lines = inputfile.readlines()
inputfile .close()

x = lines.index('!\n')
y = lines.index('Command: "system logfile"\n')
# Slice of Configuration
z = lines[x:y-1]
s = ' '.join(z)
c = s.split(' ')

a = c.index()

# a2 = "10.20.30.40"  # Input of required IP, Mask, Interface.


# test = ' '.join(c)
print c
# a = 'net ip-interface'
# a1 = "10.20.30.40 16 25"  # Input of required IP, Mask, Interface.

# a1 = z.index("create")

# a3 = "16"
# a4 = "25"



# print c
# print type(c)


# outputfile = open("Test_C.txt", "w")
# outputfile.writelines(lines[x:y+1])
# outputfile.close()



# print lines[x:y+1]

# outputfile = open("Test_C.txt", "w")
# outputfile.writelines(lines)
# outputfile.close()




