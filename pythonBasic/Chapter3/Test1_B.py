while True:
    weight=int(input("짐의 무게는 얼마입니까? "))
    if (weight<10):
        print("수수료는 없습니다\n")
    else:
        fee=int(weight/10)*10000
        print(f"수수료는 {format(fee,'3,d')}원 입니다\n")