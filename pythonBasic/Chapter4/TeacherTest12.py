week_temperature={'월':25.5,'화':28.3,'수':33.2,'목':32.1,'금':17.3,'토':35.3,'일':33.3}

sum=0
for val in week_temperature.values():
    sum+=val

avg= sum / len(week_temperature)
print(f'일주일간 최고 기온의 평균: {format(avg,".1f")}˚')
