price = int(input("금액을 입력하세요: "))

money_10k = price // 10000
money_1k = (price % 10000) // 1000
money_100 = (price % 1000) // 100
money_10 = (price % 100) // 10
money_1 = (price % 10)



first_string = (str(money_10k)+"만 ")*(money_10k != 0)
second_string = (str(money_1k)+"천 ")*(money_1k > 0)
third_string = (str(money_100)+"백 ")*(money_100 > 0)
fourth_string = (str(money_10)+"십 ")*(money_10 > 0)
fifth_string = (str(money_1))*(money_1 > 0)+"원"

print(first_string+second_string+third_string+fourth_string+fifth_string)



