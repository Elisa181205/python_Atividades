#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
num1 = int(input("Primeiro Num: "))
num2 = int(input("Segundo Num: "))
num3 = int(input("Terceiro Num:"))

# A o produto do dobro do primeiro com metade do segundo .
a = (num1*2)+(num2/2)
print ("O resultado é:", a)

# b. a soma do triplo do primeiro com o terceiro.
b=((num1*3)+ num3)
print('Resultado:', b )

# C. o terceiro elevado ao cubo
c=(num3**(3))  #ou c=pow(num3,3)
print ('Cubo de {} : {}'.format(num3,c ))