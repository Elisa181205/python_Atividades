#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input("Informe o valor do Lado: "))

area = lado * lado
# Calculando a área usando a fórmula de Heron (formula para calcularÁreas) 1/2*base*altura, onde base e altura

dobro = area*2

print("O dobro da área do quadrado é : ", dobro)