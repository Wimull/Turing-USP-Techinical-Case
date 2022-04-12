def conta_economia(emails):
    emailHandler = []      #Used in the comparison of two sequential emails by storing each of them and them comparing each letter from left to right
    caracteresEconomizados = 0
    for conta in emails:
        conta = conta.split("@")[0]
        emailHandler.append(conta)                                 # Adds two emails to emailHandler and them compares each letter
        if len(emailHandler) > 1:
            if conta[0] != emailHandler[0][0]: emailHandler.pop(0) #Looks if the second email can be trimmed and, if not, takes out the first one
            else:
                for caracteres in emailHandler[0]:
                    if emailHandler[1][0] == caracteres: 
                        emailHandler[1] = emailHandler[1].split(caracteres, 1)[1] #Takes out the first letter of the second email so that it can compare the next one
                        caracteresEconomizados += 1                               #then counts the number of characters saved
                emailHandler.clear()
                emailHandler.append(conta)                         #Clears emailHandler and then adds the full version of the trimmed email, so as to compare it to the next email on the list
                
    return caracteresEconomizados

#print(conta_economia(["aninha123@usp.br","aninhazinha000@usp.br","aninhazinhainha@usp.br","jerson331@usp.br","jersaopika@usp.br","aninhaeudnv@usp.br"])) #expected output: 21
