
class Tacts(object):

    def __init__(self,gim,la,bok,end):
        self.gim = gim
        self.la = la
        self.bok = bok
        self.end = end

    @staticmethod
    def main():
        while True:
            menu = int(input("1.김밥\n2.라면\n3.볶음밥\n0.프로그램 종료"))
            if menu == 1:
                print("김밥")
                break
            elif menu == 2:
                print("라면")
                break
            elif meun == 3:
                print("볶음밥")
                break
            elif meun == 0:
                print("프로그램 종료.")
                break
            else:
                print("잘못된 주문입니다.")
                continue

Tacts.main()
