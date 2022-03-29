price = int(input("금액을 입력하세요: "))

money_10k = str(price // 10000)
money_1k = str((price % 10000) // 1000)
money_100 = str((price % 1000) // 100)
money_10 = str((price % 100) // 10)
money_1 = str((price % 10))

print(money_10k+"만",money_1k+"천",money_100+"백",money_10+"십",money_1+"원")


