import random
def sortLoteria(qtdTotalNum,qtdNumSort) :
    listaNum = [*range(1,qtdTotalNum + 1)]
    listaSort = []

    while len(listaSort) < qtdNumSort + 1 :
        random.shuffle(listaNum)
        sortedNumber = listaNum[0]

        if (sortedNumber not in listaSort) :
            listaSort.append(sortedNumber)
				
    listaSort.sort()
    return listaSort
print(sortLoteria(60,6))