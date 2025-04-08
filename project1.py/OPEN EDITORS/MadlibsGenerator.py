with open("story.txt", "r") as f:
    story = f.read()

words = set() #conjunto q cria elementos únicos
start_of_word = -1

target_start = '<'
target_end = ">"

#vai e localiza todas as palavras diferentes q estão dentro
for i, char in enumerate(story): #dá acesso a posição da palavra
    if char == target_start:
        start_of_word = i #achou o começo, marca e indica na var

    if char == target_end and start_of_word != -1: #pegar a palavra toda e add na lista de palavras
        word = story[start_of_word: i + 1] #pegar o inicio da palavra mas sem pegar o final
        word.add(word) #add ao conjunto
        start_of_word = -1 #redefine o inicio das palavras

#pedir ao user gerar uma resposta pra eles
answers = {} #dicionario

#percorrer todas as palavras exclusivas e pedir ao user q de um valor a elas
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

#substitui uma string por outra
for word in words:
    story = story.replace(word, answers[word]) 

print(story)