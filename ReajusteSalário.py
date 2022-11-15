# Reajuste Salarial
print("Este e Um Programa Que Informa O Valor de Um Reajuste Salarial")
s = float(input("Insira o Valor Do Salário Atual: "))
r = float(input("Insira a Porcentagem de Reajuste: "))
a = s + (s * r / 100)
print("O Salário Era De R${:.2f}, Com Reajuste De %{:.1f}, O Valor Passa a Ser: R${:.2f}".format(s, r, a))

