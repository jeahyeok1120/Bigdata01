# 1) 아아 : 2000 2) 라떼 : 2500
prices = [1500, 2500]
while True:
    menu = input(f"1) 아이스 아메리카노 {prices[0]}원 2) 카페 라떼 {prices[1]}원 3) 주문종료 : ")
    if menu == "1":
        print(f"아이스 아메리카노를 주문하셨습니다. 가격은 {prices[0]}원 입니다")
    elif menu == "2":
        print(f"카폐 라뗴를 주문하셨습니다. 가격은 {prices[1]}원 입니다")
    elif menu == "3":
        print("주문을 종료합니다")
        break