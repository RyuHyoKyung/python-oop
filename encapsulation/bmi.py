#def bmi_function(height, weight):
    #return weight / height ** 2 * 10000

class Bmi(object):

    def __init__(self, height, weight):
        self.height = height
        self.weigth = weight

    def get_bmi(self):
        return self.weigth / self.height ** 2 * 10000

#if __name__ == '__main__':
    #pass
    #b = Bmi(178, 75)
    #print(b.get_Bmi())

    def get_bmi(self):
        bmi = ''
        index = self.weigth / self.height ** 2 * 10000
        if index >= 30:
            bmi = '비만'
        elif index >= 25:
            bmi = '과체중'
        elif index >= 20:
            bmi = '정상'
        elif index < 20:
            bmi = '저체중'
        return bmi


    @staticmethod
    def main():
        b = Bmi(int(input('키(Cm)를 입력하세요.')),int(input('몸무게(Kg)를 입력하세요.')))
        print(b.get_bmi())


Bmi.main()