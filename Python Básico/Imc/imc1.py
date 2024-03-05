
peso = float (input ("Digite seu peso:"))

altura = float (input ("Digite sua altura:"))

imc = round (peso/(altura**2) , 1)


if imc <= 18.5:
        print("Abaixo do peso" , "imc:" , imc)


elif imc >= 18.6 and imc <= 24.9:
        print("Peso ideal" , "imc:" , imc)        


elif imc >= 25 and imc <= 29.9:
        print("Acima do peso" , "imc:" , imc)


elif imc >= 30 and imc <= 34.9:
        print("Obesidade grau 1" , "imc:" , imc)


elif imc >= 35 and imc <= 39.9:
        print("Obesidade grau 2" , "imc:" , imc)


else:
        print("Obesidade grau 3" , "imc:" , imc)