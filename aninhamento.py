# Variável Idade
idade = 30
# Variável Cartão
tem_cartao = True

# Condição Para Verificar a Idade
if idade >= 18:
    # Condição Para Verificar se o Usuário tem Cartão
    if tem_cartao:
        print("Você pode comprar o produto.")
    else:
        print("Você não pode comprar o produto sem um cartão.")
else:
    print("Você é menor de idade e não pode comprar o produto.")