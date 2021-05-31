elif menu == '3':
account_number = input('입금할 계좌번호')
money = input('입금액 입력바랍니다')
deposit = input('입금액 입력바랍니다')
print(f'>>  입금액: {deposit}')
for i, j in enumerate(ls):
    if j.account_number == account_number:
        print(f'>> 잔액 : {j.money}')
        replace = Account(j.account_number,
                          j.name,
                          int(j.money) + int(money))  # 입금 +
        int(j.money) + int(deposit))  # 입금 +
        Account.del_account(ls, account_number)
        ls.append(replace)
        elif menu == '4':
