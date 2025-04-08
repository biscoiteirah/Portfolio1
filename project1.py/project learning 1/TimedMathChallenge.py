import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) #escolhe um elemento aleatorio da lista
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) #avalia uma str como uma expr python
    return expr, answer

wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time() #vai dar o registro de tempo

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    #continua perguntando quando errar, vai quebrar quando acertar
    while True:
       guess = input("Problem #" + str(i + 1) + ': ' + expr + " = ") #aqui ta o problema
       if guess == str(answer): #convertendo um int em str
        break
       wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2) #arrendodar o tempo mais prox de 2 digitos

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
