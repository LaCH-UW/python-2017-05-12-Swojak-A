from _basic_func import return_values, count_freq
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

rc('font', family='DejaVu Sans')

words = ['Wokulski', 'Rzecki', 'subiekt', 'handel', 'sklep']
book = "books/lalka-tom-pierwszy.txt"
book2 = "books/lalka-tom-drugi.txt"

# print(return_values(count_freq(book), words), return_values(count_freq(book2), words))

def bar_chart(book, book2, words):
    data1 = return_values(count_freq(book), words)[1]
    data2 = return_values(count_freq(book2), words)[1]

    N = len(words)
    ind = np.arange(N)
    width = 0.10

    fig = plt.figure()
    ax = fig.add_subplot(111)    # trochę nie rozumiem co tu zrobiliśmy, ale działa

    ax.bar(ind-(0.5*width), data1, width, color='b')
    ax.bar(ind+(0.5*width), data2, width, color='g')

    plt.show()

bar_chart(book, book2, words)

"""
Niby działa, ale nie powiem, żebym to jakoś szczególnie rozumiał
"""