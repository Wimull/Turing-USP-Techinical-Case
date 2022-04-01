from string import octdigits


def estacionamento_ok(TAMANHO, instantes):
    estacionamento = []
    for instructions in instantes:
        if instructions < 0:
            try:                                     #Tries for an empty array and returns "no" if it can't pop "estacionamento"              
                if estacionamento.pop() != abs(instructions): return "não"  #Looks if the exiting car can in fact exit or if there is a car in front of it, returns "no"
            except:
                return "não"
        else:
            try:                                     #Looks if "estacionamento" already contains the car given by "instructions" and returns "no" if it encouters it
                estacionamento.find(instructions) 
                return "não" 
            except: estacionamento.append(instructions)
            if len(estacionamento) > TAMANHO: return "não"
    if len(estacionamento) != 0: return "não"        #Checks to see if at the end of instructions, "estacionamento" is empty and if not, returns "no"
    return "sim"                                     #Returns yes if all checks passed

print(estacionamento_ok(3,[1,2,-2,3,-3,-1]))         #Expected output: "sim"
#print(estacionamento_ok(3,[1,2,-2,3,5,-3,-1,-5]))   #Expected output: "não"
print(estacionamento_ok(5,[1,2,3,4,3,-4,-3,-2,-1]))   #Expected output: "não"