from matplotlib import pyplot as plt

def createHistogram(string):
    histograma = {}
    for letter in string:
        histograma[letter] = histograma.get(letter, 0) + 1
    return histograma

#Daqui pra baixo a string vai ser lida, transformada num histograma e plotada
text1 = input("digite a string:\n")
histograma1 = createHistogram(text1)

def plotHistogram(histograma1, text1):
    lista1 = []
    for letter in text1:
        lista1.append(letter)
    plt.hist(lista1, len(histograma1) * 2, align = 'mid')
    plt.show()

plt.title("Histograma da string")
plotHistogram(histograma1, text1)

#Daqui pra baixo a outra string vai ser lida, transformada num histograma e plotada
text2 = input("digite a outra string:\n")
histograma2 = createHistogram(text2)

plt.title("Histograma da outra string")
plotHistogram(histograma2, text2)

def countDeletions(histograma1, histograma2):
    deletions = 0
    #no primeiro loop ele vai comparar os caracteres do primeiro histograma
    #entretanto, pode haver caracteres no segundo histograma que não estão no primeiro
    for letter in histograma1:
        if (histograma2.get(letter, 0) != histograma1[letter]):
            deletions += abs(histograma2.get(letter, 0) - histograma1.get(letter))

    for letra in histograma2:
    #se a letra do histograma2 nao estiver no histograma1
        if(histograma1.get(letra, 0) == 0):
            deletions += histograma2.get(letra)

    return deletions

def histogramaResultante(histograma1, histograma2):
    histogramaRes = {}
    for letter in histograma1:
        histogramaRes[letter] = histograma1[letter]

    #faz um merge dos 2 histogramas, mas eh necessario fazer a diferença e dividir por 2
    for letter in histograma2:
        if (histogramaRes.get(letter, 0) == 0):
            histogramaRes[letter] = histograma2[letter]
        else:
            histogramaRes[letter] += histograma2[letter]
    
    #tirar as duplicatas do resultado:
    for letter in histogramaRes:
        histogramaRes[letter] = min(histograma1.get(letter, 0), histograma2.get(letter, 0))
    return histogramaRes

histogramaRes = histogramaResultante(histograma1, histograma2)

lista3 = []
for letter in histogramaRes:
    if (histogramaRes[letter] != 0):
        vezes = histogramaRes[letter]
        for i in range(0, vezes):
            lista3.append(letter)

plt.title("Histograma resultante")
plt.hist(lista3, len(lista3)*2, align = 'mid')
plt.show()

print("o histograma da primeira string é: ", histograma1)
print("o histograma da segunda string é: ", histograma2)
print("o histograma da string resultante é: ", histogramaRes)
print("O número mínimo de delets para tornar os histogramas iguais é ", countDeletions(histograma1, histograma2))