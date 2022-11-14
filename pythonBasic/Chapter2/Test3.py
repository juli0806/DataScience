fat = int(input("지방의 그램을 입력하세요:"))
carponhydrate= int (input("탄수화물의 그램을 입력하세요:"))
protein = int(input("단백질의 그램을 입력하세요:"))
calorie= fat*9 + protein*4 + carponhydrate*4
print(f"총칼로리:{format(calorie,'3,d')} cal")