import re

data = input()
data = re.sub("[^0-9]"," ",data).split()

data[1] = str(int(data[2]) // 24 + int(data[1])).zfill(2)
data[2] = str(int(data[2]) % int(24)).zfill(2)

print("{0[0]}/{0[1]} {0[2]}:{0[3]}".format(data))