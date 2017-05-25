from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

# domyślna czcionka nie wspiera znaków unicode
# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

words = ['Wokulski', 'Rzecki', 'Izabela', 'Ochocki', 'sklep']
title1 = 'books/lalka-tom-pierwszy.txt'
title2 = 'lalka-tom-drugi.txt'

def line_plot(data1, data2, names):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")

    plt.scatter(range(len(names)), data1, color='r', label="Liczba słów w I tomie Lalki")
    plt.plot(data2, color='b', label="Liczba słów w II tomie Lalki")
    plt.legend()

    plt.grid()

    plt.xticks(range(len(names)), names, rotation=45)
    #funkcja tworząca listę na osi x

    plt.tight_layout()
    plt.savefig('sc.png')
    plt.show()

def line_plot2(data1, data2, names):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")

    #zip to ciekawa funkcja, ale muszę sprawdzić jak działa
    #iterator = zip(data1,data2)
    #delimiter = []

    plt.scatter(data1, data2, color='r', label="Liczba słów w I tomie Lalki")
    #plt.plot(data2, color='b', label="Liczba słów w II tomie Lalki")
    plt.legend()

    plt.grid()

    for label, x, y in zip(names, data1, data2):
        plt.annotate(label, xy=(x, y), xytext=(x-10, y+10) )
    #plt.xticks(range(len(names)), names, rotation=45)
    #funkcja tworząca listę na osi x

    plt.tight_layout()
    plt.savefig('sc2.png')
    plt.show()

def heatmap(data1, names):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")

    axis = range(len(names))
    plt.yticks([x + 0.5 for x in range(2)], ["dzieło I", "dzieło II"])
    plt.xticks([x + 0.5 for x in axis], names, rotation=90)
    plt.pcolor(data1)

    plt.tight_layout()
    plt.savefig('heatmap.png')
    plt.show()


def count_freq(fname):
    with open(fname, encoding="utf8") as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist

def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(file1, file2, words):
    freq1 = count_freq(file1)
    freq2 = count_freq(file2)

    res1 = return_values(freq1, words)
    res2 = return_values(freq2, words)

    line_plot2(res1, res2, words)

make_plot(title1, title2, words)

def make_plot2(file1, file2, words):
    freq1 = count_freq(file1)
    freq2 = count_freq(file2)


    #robimy wykres hitmap
    #do tego potrzebujemy udawać macierz

    val1 = []


    val1.append(return_values(freq1, words))
    val1.append(return_values(freq2, words))

    heatmap(val1, words)



def make_heatmap_iteracja(lista_dzieł, words):
    val1 = []
    for dzieło in lista_dzieł:
        freq = count_freq(dzieło)

        val1.append(return_values(freq, words))

    heatmap(val1, words)





# teraz dopisz kod tworzący wykres punktowy zawierający liczbę wystąpień słów z listy
# z punktami różnych kolorów dla pierwszego i drugiego tomu "Lalki"
# dostosuj legendę itp.

# podpowiedź: funkcję plt.plot(y) zastępuje funkcja plt.scatter(x, y)

