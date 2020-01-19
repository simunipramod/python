def calculater_BMI(weight, hight):
    BMI = weight / (hight * hight)
    return BMI


weight = float(input("please enter weight: "))
hight = float(input("please enter hight: "))
print(calculater_BMI(weight, hight))
