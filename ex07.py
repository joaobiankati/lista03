valor_duplicata = float(input("Informe o valor da duplicata: "))
dias_atraso = int(input("Informe quantos dias de atraso: "))

multa = valor_duplicata * 0.05 * dias_atraso

valor_final = valor_duplicata + multa

print(f"O valor final de sera de R$ {valor_final}")