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

    print("Quantes persones anireu: ",end="")
    quantitatPersones = int(input())

    if opcioEscollida == "opcioI":

        preuTotalDies = (opcioI * quantitatDies)

        preuPerPersona = (opcioI * quantitatPersones)

        preuFinal = (preuTotalDies + preuPerPersona)

    elif opcioEscollida == "opcioB":


        preuTotalDies = (295 * quantitatDies)

        preuPerPersona = (295 * quantitatPersones)

        preuFinal = (preuTotalDies + preuPerPersona)


    print(preuFinal)





