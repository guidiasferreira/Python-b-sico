
salario = float (input("Informe seu salário:"))

if salario <= 3000:
            print("Programador junior")

elif salario > 3000 and salario <= 6000:
            print("Programador pleno")    

elif salario > 6000 and salario <= 12000:
            print("Programador sênior")        


else:
            print("Gerente de projetos")