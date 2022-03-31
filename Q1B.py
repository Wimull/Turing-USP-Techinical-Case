from ntpath import join 
def corrige_emails(emails):
    emailsCorrigidos = []
    email_Joiner = ""

    for conta in emails:
        if conta.find("@usp.br") == len(conta) - 7: emailsCorrigidos.append(conta) #Checks to see if the email isn't erroneous
        else:
            desvioHandler = []
            chars = [c for c in conta]                                       #characters (chars) in the string
            chars.reverse()
            desvio = (len(chars) - 7 - chars.index("@"))                     # "@"" should be inserted on 7th position from right to left, "desvio" checks for the deviation on that character position from right to left
            
            for i in range(0, (len(chars)))  :
                desvioHandler.append(chars[i - desvio])                      #With the deviation calculated, we can restore the original string by reading chars from the index given by "desvio"

            contaCorrigida = email_Joiner.join(desvioHandler)
            if contaCorrigida.find("@usp.br") == -1: contaCorrigida = "ERRO" #Checks to see if there there wasn't another problem with the given email other than reversing and shifting
            emailsCorrigidos.append(contaCorrigida)                          #Appends the corrected email if the process was successfull, and "ERRO" if not
    return emailsCorrigidos

#print (corrige_emails( [ "aninha@usp.br", "ibol.alimacrb.psu@ocna", "t.alalalimacrb.repsu@ppo", ".orbmem_ovonrb.psu@gnirut"])) 
#Expected output: ['aninha@usp.br', 'camila.lobianco@usp.br', 'ERRO', 'novo_membro.turing@usp.br']
