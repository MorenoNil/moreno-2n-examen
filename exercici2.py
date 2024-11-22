from tkinter import IntVar

if __name__ == '__main__':

    opcioI = float()
    opcioB = float()
    opcioP = float()
    opcioM = float()
    quantitatPersones = int()
    quantitatDies = int()
    preuPerPersona = float()
    preuTotalDies = float()
    opcioEscollida = str()

    preuFinal = float()


    #PREU PER PERSONA Y DIA

    opcioI = 430,00
    opcioB = 295,00
    opcioP = 125,00
    opcioM = 395,00

    print("Escriu quina opcio escolliras: ",end="")
    opcioEscollida =input()

    print("Quants dies anireu de viatge: ",end="")
    quantitatDies = int(input())

    if quantitatDies < 0:

        print("ERROR \n Torna a entrar els dies que anireu de viatge: ", end="")
        quantitatDies = int(input())

    print("Quantes persones anireu: ",end="")
    quantitatPersones = int(input())


    if opcioEscollida == "I":

        preuTotalDies = (430,00 * quantitatDies)

        preuPerPersona = (430,00 * quantitatPersones)

        preuFinal = (preuTotalDies + preuPerPersona)

    elif opcioEscollida == "B":


        preuTotalDies = (295 * quantitatDies)

        preuPerPersona = (295 * quantitatPersones)

        preuFinal = (preuTotalDies + preuPerPersona)

    elif opcioEscollida == "P":


        preuTotalDies = (125 * quantitatDies)

        preuPerPersona = (125 * quantitatPersones)

        preuFinal = (preuTotalDies + preuPerPersona)

    elif opcioEscollida == "M":

        preuTotalDies = (395 * quantitatDies)

        preuPerPersona = (395 * quantitatPersones)

        preuFinal = (preuTotalDies + preuPerPersona)


    else:

        print("Opcio invalida" "\n Torna a entrar la opcio: ",end="")
        opcioEscollida = str(input())

        if opcioEscollida == "I":

            preuTotalDies = (430, 00 * quantitatDies)

            preuPerPersona = (430, 00 * quantitatPersones)

            preuFinal = (preuTotalDies + preuPerPersona)

        elif opcioEscollida == "B":

            preuTotalDies = (295 * quantitatDies)

            preuPerPersona = (295 * quantitatPersones)

            preuFinal = (preuTotalDies + preuPerPersona)

        elif opcioEscollida == "P":

            preuTotalDies = (125 * quantitatDies)

            preuPerPersona = (125 * quantitatPersones)

            preuFinal = (preuTotalDies + preuPerPersona)

        elif opcioEscollida == "M":

            preuTotalDies = (395 * quantitatDies)

            preuPerPersona = (395 * quantitatPersones)

            preuFinal = (preuTotalDies + preuPerPersona)



    print("EL PREU FINAL ES: ", preuFinal)








