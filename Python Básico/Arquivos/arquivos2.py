
arquivo = open("bom.txt" , "w")
arquivo.write("Bom Dia")
arquivo.close()

leitura = open("bom.txt" , "r")
print(leitura.read())
leitura.close()

