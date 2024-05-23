preco_unitario = float(input("Informe o preço unitario do produto: "))
desconto = float(input("Informe a % do desconto: "))

valor_final = preco_unitario - (preco_unitario * desconto / 100)

print(f"O valor final ficou de R$ {valor_final}")