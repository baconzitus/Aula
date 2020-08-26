numero1 = 2
numero2 = 3

#operadores aritimeticos

#soma
resposta_soma = numero1 + numero2
print("resposta da soma",resposta_soma)
print("resposta da soma", (numero1 + numero2))

#subtracao
resposta_subtracao = numero1 - numero2
print("respsota da subtracao", resposta_subtracao)
print("resposta da subtracao", (numero1 - numero2))

#multiplicacao
resposta_multiplicacao = numero1 * numero2
print("resposta da multiplicacao" , resposta_multiplicacao)
print("resposta da multiplicacao" , (numero1 * numero2))

#divisao
resposta_divisao = numero1 / numero2
print("respsota da divisao",resposta_divisao)
print("respsota da divisao", numero1 / numero2)

#expoente
resposta_expoente = numero1 ** numero2
print("resposta do expoente", resposta_expoente)
print("resposta do expoente", numero1 ** numero2)

#operadores logicos e relacionais
print("operador logico AND(e)", (numero1 < 5 and numero2 <10))
print("operador logico or(ou)" , (numero1 <5 or numero2 >20))
print("operador logico de negacao (NOT)" , (not(numero1 < 5 and numero2 < 5)))
print("operador relacional !=(diferente", (numero1 != numero2))

#armazena inserir e mudar de tipo de varialvel

nome = input("digite um nome: ")
print(nome)
print("tipo do dado",type(nome))

numeroint =int(input("digite um numero inteiro: "))
print(numeroint)
print("tipo do dado",type(numeroint))

numerofloat = float(input("digite um numero real: "))
print(numerofloat)
print("tipo do dado",type(numerofloat))


