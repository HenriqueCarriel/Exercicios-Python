import time

nome = input('Digite o seu nome completo: ').strip()
nome_sem_espaco = len(nome) - nome.count(' ')
primeiro_nome = nome.split()

print('Processando dados...')
time.sleep(5)

print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print(f'Seu nome com letras minúsculas: {nome.lower()}')
print(f'seu nome tem {nome_sem_espaco} letras')
print(f'seu primeiro nome tem: {len(primeiro_nome[0])} ')