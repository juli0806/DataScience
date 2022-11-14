mileage={'kim99':12000,
        'lee66':11000,
        'han55':3000,
        'hong77':5000,
        'hwang':18000}


# max_key='kim99'
#
# for key in mileage.keys():
#     if mileage[max_key]<mileage[key]:
#         max_key=key

print(max(mileage.values()))

for key in mileage:
    if mileage[key]==max((mileage).values()):
        max_key=key
        max_val=max(mileage.values())

print(f"{max_key}님의 마일리지({max_val})점이 가장 높은 점수입니다")