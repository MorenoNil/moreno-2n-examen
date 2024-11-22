if __name__ == '__main__':

    hores = int()
    minuts = int()
    totalMinuts = int()
    horesAminuts = int()

    print("Quantes hores has treballat: ",end="")
    hores = int(input())

    print("Quantes minuts has treballat: ",end="")
    minuts = int(input())

    while not hores or minuts < 0:

        print("ERROR \n Torna a entrar les hores: ",end="")
        hores = int(input())

        print("Quants minuts has treballat: ",end="")
        minuts = int(input())


    horesAminuts = hores / 60

    totalMinuts = horesAminuts + minuts

    print("El total de minuts es: ",totalMinuts)