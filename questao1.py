fib = [0, 1]
def calculo_fibonacci(num):
    while True:
        prox_num = fib[-1] + fib[-2]
        if prox_num > num:
            break
        fib.append(prox_num)
    comparacao_num(num)
    
def comparacao_num(num):
    if num in fib:
        print(f"O número {num} está dentro da sequência Fibonacci.")
    else:
        print(f"O número {num} não está dentro da sequência Fibonacci.")

num = int(input("Informe um número:"))
calculo_fibonacci(num)