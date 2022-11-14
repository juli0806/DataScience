week_temperature={'월':25.5,'화':28.3,'수':33.2,'목':32.1,'금':17.3,'토':35.3,'일':33.3}

print("기온이 30˚ 이상인 요일: ",end='')
result=[]
keys=[]
for key in week_temperature.keys():
    if week_temperature[key]>=30:
        keys.append(key)
        result=','.join(keys)
print(result)
