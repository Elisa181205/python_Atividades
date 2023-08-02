#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
h = float(input("Informe sua altura: "))
homens= (72.7*h)-58
mulheres = (62.1*h)-44.7

print("O peso ideal para mulher é:", mulheres)
print("O peso ideal para homem é:", homens)

#ou podemos fazer dessa outra forma

altura = float(input("Informe sua altura: "))

genero = input("Informe seu genero com F ou M: ")

if genero == "F":
    print ("Seu peso ideal é", 62.1 * altura - 44.7)

else:
    print("seu peso ideal é", (72.7*altura)-58)