print("Bem vindo a sequencia de Fibonacci Wélida")
n = int(input( "Quantos termos voce deseja visualizar? "))
r1 = 0
r2 = 1
print("{} - {}".format(r1, r2), end=" ")
cont = 3
while cont <= n:
    r3 = r1 + r2
    print("- {} ".format(r3), end= " ")
    r1 = r2
    r2 = r3
    cont += 1
print("Fim")
