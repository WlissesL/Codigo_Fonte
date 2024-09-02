
"""
indice = 13 
soma = 0
k = 0 

while k < indice :
      k = k + 1
      soma = soma + k


print (soma )

"""
numero = int (input("Dgite um número para verificar se ele pertence á sequencia de Fibonacci:"))

a,b = 0,1

while b < numero :
    a, b = b, a + b

if b == numero:
     print(f"O número {numero} pertence a sequencia de fibonacci")

else:
     print(f"O número {numero} não pertence a sequencia de fibonacci")