
class Stock(object):
    def __init__(self,name,code):
        self.name = name
        self.code = code

    def get_stock(self):
        return f'종목명:{self.name} 종목코드:{self.name}'


    @staticmethod
    def main():

        while True:
            menu = input("0.프로그램 종료\n1.종목 추가")
            if menu == '0':
                print('프로그램 종료.')
                break
            elif menu == '1':
                s = Stock(input('종목이름:'), input('종목코드'))
            elif menu == '2':
                print(s.get_stock())

            else:
                print('잘못된 번호 입니다.')
                continue

Stock.main()