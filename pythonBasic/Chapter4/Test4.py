position=['과장','부장','대리','사장','대리','과장']

position_set=set(position)
not_duplicate_position=position_set

position_frequency={}
for key in position:
    position_frequency[key]=position_frequency.get(key,0)+1

print(f"중복되지 않은 직위:{not_duplicate_position}")
print(f"각 직위별 빈도수: {position_frequency}")