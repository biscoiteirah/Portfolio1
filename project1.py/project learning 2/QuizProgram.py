print('Boas vindas ao meu quiz!')

playing = input("Você quer jogar o quiz? ")

if playing.lower() != 'sim':
    quit()
    
print('Legal! Vamos começar: :)')
score = 0

answer = input('O que vem primeiro? O ovo ou a galinha? ').lower()
if answer == 'ovo':
    print('Correto!')
else:
    print("Incorreto!")
    
answer = input('Um jogo em 2018 que deveria ter ganhado o GOTY, mas perdeu injustamente? ').lower()
if answer == 'red dead redemption 2':
    print('Correto!')
    score += 1
else:
    print("Incorreto!")
    
answer = input('Bairro mais super faturado do RJ? ')
if answer == 'Leblon':
    print('Correto!')
    score += 1
else:
    print("Incorreto!")
    
answer = input('O que está na frente de você o tempo todo, mas não pode ser visto? ').lower()
if answer == 'o futuro':
    print('Correto!')
    score += 1
else:
    print("Incorreto!")
    
answer = input('O que é algo que você pode segurar, mas nunca pode tocar? ').lower()
if answer == 'promessa':
    print('Correto!')
    score += 1
else:
    print("Incorreto!")
    
answer = input('O que é, o que é, quanto mais você tira, maior fica? ').lower()
if answer == 'buraco':
    print('Correto!')
    score += 1
else:
    print("Incorreto!")
    
answer = input('Se você olhar para o futuro, quem está refletindo sobre isso? ').lower()
if answer == 'você':
    print('Correto!')
    score += 1
else:
    print("Incorreto!")
    
answer = input('O que é invisível, mas você pode sentir seu peso? ').lower()
if answer == 'silêncio':
    print('Correto!')
    score += 1
else:
    print("Incorreto!")
    
print('Você acertou ' + str(score) + ' questões!')