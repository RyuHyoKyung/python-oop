class Bmi:
    def bmi(height, weight):
        height = int(input("Input your height in meters: "))
        weight = int(input("Input your weight in kilogram: "))
        result = (weight + height)
        return result

    print("Your body mass index is: ", round(weight / (height * height), 2))