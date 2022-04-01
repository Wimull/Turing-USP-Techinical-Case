def estado_atual(TAMANHO, horários, INSTANTE):
    class Carro:                                  #Defines a class (cars) with an id, moment of entry and position in the parking lot
        def __init__(self, entrada, id):
            self.entrada = entrada
            self.id = id
            self.posição = 0

        def position(self, momento):
            self.posição = momento - self.entrada #Uptades the position of the car based on the rule that the car moves one position in the parking lot each instant
            if (self.posição < TAMANHO) & (self.posição > -1): return self.posição
            return -1                             #Calculates the position of the car based on the instant given or, if the car has moved out of the parking lot, returns -1

    
    estacionamento = []                           #Defines a parking lot as an array of length "TAMANHO" filled with 0's
    for x in range(0, TAMANHO):
        estacionamento.append(0)

    for i in range(1, len(horários) + 1):
        i = Carro(horários[i - 1], i)
        if i.position(INSTANTE) > -1:
            estacionamento[i.position(INSTANTE)] = i.id
    return estacionamento                         #Returns an array with the id of the car in that position, or zero if that position is empty

#print(estado_atual(4,[1,4,6,2],7))               #Expected output: [0, 3, 0, 2]
#print(estado_atual(5,[3,6,12,9,4,15,16],7))      #Expected output:[0, 2, 0, 5, 1]
#print(estado_atual(5, [1,4,6,2], 6))             #Expected output: [3, 0, 2, 0, 4]
