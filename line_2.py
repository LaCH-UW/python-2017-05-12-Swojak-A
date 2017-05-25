from _basic_func import line_plot, return_values, count_freq
from line_1 import words, filenames, titles

def creating_sum(words, filenames):
    data = []
    for e in filenames:
        data.append(return_values(count_freq(e), words)[1])

    results = []
    for word in range(len(words)):          # ten fragment chciałem zrobić jakoś sprytniej przy użyciu zipa, ale problem tkwi w tym, że len(words) może mieć różną długość
        temp = []
        for n in range(len(data)):
            temp.append(data[n][word])
        results.append(sum(temp))

    return "wszystkie", results

label_dict = {"wszystkie": "wszystkich książkach"}

line_plot(words, label_dict, creating_sum(words, filenames))

"""
teraz tak sobie myśle, że chyba nie o to chodziło, może zrobie jeszcze od nowa
UPDATE: jednak nie zrobię :)
"""