import time, sys, os, pyautogui
count = 0
vezes = 0
achados = 0
armazenar = 0
numeral = 0
armazenados = 0
armazenou = 0
quantidade = 0
achou = []
autos = []
print('-' * 40)
print(f'{"Bem-Vindo!":^40}')
print('-' * 40)
print('Digite o(s) número(s) para armazenamento')
print('J para parar de imediato.')
pyautogui.PAUSE = 2.5
while True:
	armazenar = str(input().upper())
	autos.append(armazenar)
	vezes += 1
	quantidade += 1
	armazenou += 1

	if quantidade == 10:
		armazenados -= armazenados
		print(f'Você já armazenou {armazenou}, deseja continuar armazenando? [S/N]: ')
		continuar = str(input().upper())
		
		if continuar == 'N':
			print('Aguarde...')
			for i in range(0, 2):
					sys.stdout.flush()
					time.sleep(1)
			os.system('cls')
	while True:

	print('\n')
	auto = str(input('Digite o número do auto.\n '))
	vezes += 1

	if auto in autos:
		print('\n')
		print('Consta no Diário.')
		print(f'O auto é o número {autos.index(auto)} na sequência')
		count += 1
		achados += 1
		achou.append(auto)

		if vezes == 5:
			vezes -= 5
			print('\n')
			print('Aguarde...')
			for i in range(0, 2):
					sys.stdout.flush()
					time.sleep(1)
			os.system('cls')
			print(f'Você parou no {auto}, continue.')

		if count == 5:
			count -= 5
			print(f'Parabéns, você já encontrou {achados} autos!')
			print('\n')
			continuar = str(input('Deseja continuar procurando? [S/N] ')[0].upper().strip())

			if continuar == 'N':
				print('-' * 40)
				print(f'Você achou os seguintes autos...\n {achou}')
				print('-' * 40)
				print('Até logo!')
				fechar = str(input('Fechar Programa? [S/N] ')[0].upper().strip())
				if fechar == 'S':
					print('Fechando Programa...')
					print('-' * 40)
					for i in range(0, 3):
						sys.stdout.flush()
						time.sleep(1)
					break

	else:
		print('\n')
		print('Não consta no Diário.')

		if vezes == 5:
			vezes -= 5
			print('\n')
			print('Aguarde...')
			for i in range(0, 2):
					sys.stdout.flush()
					time.sleep(1)
			os.system('cls')
			print(f'Você parou no {auto}, continue.')


		