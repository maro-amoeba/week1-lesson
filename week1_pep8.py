a = input()
b = a.split()
day = b[0][3:5]
time = b[1][0:2]

c = int(time) // 24
result_day = c + int(day)
result_time = int(time) % 24

month = b[0][0:2]
minuts = b[1][3:5]

if len(str(result_time)) == 1:
    print(month +"/"+ str(result_day) +" 0"+ str(result_time) +":"+ minuts)
else:
    print(month +"/"+ str(result_day) +" "+ str(result_time) +":"+ minuts)
