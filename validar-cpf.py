# Função prepara soma = 0, o processamento: alinhamento (zip), conversão e cálculo int(dig)
# e o acumulo. A lógica do resto (módulo) e entrega final (return) 
def digito_verificador(digitos, pesos):
    soma = 0
    for dig, pes in zip(digitos, pesos):
        soma += int(dig) * pes
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

dados = input("Digite seu número de CPF: ")

# Limpeza de caracteres não numéricos
cpf_limpo = "".join(filter(str.isdigit, dados))

# Validação inicial: deve ter 11 dígitos e não pode ser sequência repetida
if len(cpf_limpo) == 11 and cpf_limpo != cpf_limpo[0] * 11:
    
    pesos1 = list(range(10, 1, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = list(range(11, 1, -1)) # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Cálculo dos dígitos
    digito1 = digito_verificador(cpf_limpo[:9], pesos1)
    digito2 = digito_verificador(cpf_limpo[:10], pesos2)
    
    # Comparação final
    if cpf_limpo[-2:] == f"{digito1}{digito2}":
        print("CPF válido!")
    else:
        print("CPF inválido!")
else:
    print("CPF inválido!")