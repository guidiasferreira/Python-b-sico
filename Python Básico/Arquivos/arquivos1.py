
arquivo = open ("arqText.txt" , "w")

arquivo.write ("Curso Python , \n")
arquivo.write ("Aula Pratica")
arquivo.close()

#Leitura do arquivo em texto

leitura = open("arqText.txt" , "r")
print(leitura.read())
leitura.close()