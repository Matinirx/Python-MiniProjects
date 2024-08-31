import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBS = 10

def gen_problem():
    
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    ans = eval(expr)
    
    return expr, ans

wrong = 0
input("Press Enter to start")
print("..........................")

st_time = time.time()

for i in range(TOTAL_PROBS):
    expr, ans = gen_problem()
    while  True:
        guess = input(f"Problem #{str(i + 1)}: {expr} = ")
        if guess == str(ans):
            break
        wrong += 1

nd_time = time.time()
total_time = nd_time - st_time 

print("..........................")
print(f"Nice Job!. You finished in {round(total_time, 2)} seconds!")

