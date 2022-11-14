menu={'누가바':10, '바밤바':4,'보석바':7}

while True:
    option=int(input("반갑습니다. 500원 샵입니다.\nmenu 보기: 1, 구매: 2, 프로그램 종료: -1\n>>>"))
    if(option==1):
        idx=0
        for key in menu:
            idx+=1
            print(f'{idx}. 이름:{key},',end='')
            if menu[key]!=0:
                print(f'수량:{menu[key]}')
            else:
                print('품절된 상품입니다.')
        print()
    elif(option==2):
        buy_item=input("구매하실 아이스크림을 입력하세요: ")

        IS_NOT_EXISTED = False
        for key in menu:
            if key!=buy_item:
                print("입력하신 상품이 존재하지 않습니다\n")
                IS_NOT_EXISTED = True
            else:
                print(f"{key}를 고르셨습니다")
                if(menu[key]!=0):
                    buy_quantity = int(input("구매하실 수량을 입력하시오: "))
                    if(buy_quantity<=menu[key]):
                        price=500*buy_quantity
                        print(f"감사합니다. {price}원 결제 도와드리겠습니다\n")
                        menu[key]-=buy_quantity
                    else:
                        print("입력하신 수량이 구매하실 수 있는 수량보다 많습니다.\n")
                        continue
                else:
                    print("품절된 상품입니다")
                    continue
        if IS_NOT_EXISTED:
            break

    elif (option == -1):
        print('이용해주셔서 감사합니다\n')
        break
    else:
        print("잘못된 접근입니다\n")
        continue