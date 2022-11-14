mileage={'kim99':12000,
        'lee66':11000,
        'han55':3000,
        'hong77':5000,
        'hwang':18000}

find_id='han55'
mileage[find_id]=5000

print("for문으로 dic에 접근하기")
for key in mileage.keys():
    if key==find_id:
        print(f"{find_id}님의 마일리지가 {mileage[key]}점으로 수정되었습니다")

print("")
print("get으로 접근하기")
print(f"{find_id}님의 마일리지가 {mileage.get(find_id)}점으로 수정되었습니다")
