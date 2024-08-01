a = input("Digite sua nota: ")
nota = float (a)

if nota >=7.0:
    print ("Você está aprovado por média.")
    if nota>9.0:  # IF ANINHADO
        print ("Parabéns!")  # se nota > 9
    print ("Boas Ferias!")  #  se nota >=7
else:
    if nota>=4: # IF ANINHADO
        print ("Você pode fazer RECUPERAÇÃO.");
        print ("Venha na próxima semana")
    else:
        print ("Você está reprovado!")
        print ("Você não pode fazer RECUPERAÇÃO.")
       
print ("Acabou.")