from ntpath import join 
def corrige_emails(emails):
    emailsCorrigidos = []
    email_Joiner = ""

    for conta in emails:
        if conta.find("@usp.br") == len(conta) - 7: emailsCorrigidos.append(conta)
        else:
            desvioHandler = []
            chars = [c for c in conta]
            chars.reverse()
            desvio = (len(chars) - 1 - 6 - chars.index("@"))
            
            for i in range(0, (len(chars)))  :
                desvioHandler.append(chars[i - desvio])

            contaCorrigida = email_Joiner.join(desvioHandler)
            if contaCorrigida.find("@usp.br") == -1: contaCorrigida = "ERRO" 
            emailsCorrigidos.append(contaCorrigida)
    return emailsCorrigidos

#print (corrige_emails( [ "aninha@usp.br", "ibol.alimacrb.psu@ocna", "t.alalalimacrb.repsu@ppo", ".orbmem_ovonrb.psu@gnirut"]))
