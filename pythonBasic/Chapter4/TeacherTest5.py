mileage={'kim99':12000,
        'lee66':11000,
        'han55':3000,
        'hong77':5000,
        'hwang':18000}
index=0
for key in mileage:
    index+=1
    print(f"{index}. 아이디: {key}, 마일리지:{mileage[key]}")