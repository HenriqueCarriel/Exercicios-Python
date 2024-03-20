nome = input("Digite o nome do aluno: ")
n1 = float(input("\nPrimeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))

media = (n1 + n2) / 2
print(f"\nA média entre {n1} e {n2}\nNOTA {media}")

if (media>=7):
    (print(f"\nParabéns, o {nome} está aprovado!")
)
else:
   print(f"\nEstude mais, o {nome} está reprovado!")