from nltk import FreqDist
from matplotlib import pyplot as plt
from matplotlib import rc
import unicodedata

rc('font', family='DejaVu Sans')

# def count_freq(fname):
#     with open(fname, encoding="utf8") as fp:
#         split_words = fp.read().split()
#         freq_dist = FreqDist(split_words)
#     return freq_dist

def count_freq(fname):
    # count_freq changed to faster and more precise version
    struct = {}
    with open(fname, encoding="utf8") as fp:
        for word in ''.join(c if unicodedata.category(c) in ('Zs', 'Zl', 'Ll', 'Lu') else ' ' for c in fp.read()).lower().split():
            if word not in struct:
                struct[word] = 1
            else:
                struct[word] += 1

    return fname, struct


def return_values(freq, words):
    # words have to be a list, otherwise it will iterate on chars
    assert type(words) == list

    book = freq[0]
    freq = freq[1]
    result = []
    for s in words:
        s = s.lower()
        result.append(freq[s] if s in freq else 0)

    return book, result


def line_plot(names, book_dict, *args):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")
    colors_dict = {0: "b", 1: "g", 2: "r", 3: "c", 4: "m", 5: "y", 6: "k"}

    for no in range(len(args)):
        plt.plot(args[no][1], color=colors_dict[(no%len(colors_dict))], label="Liczba słów w " + str(book_dict[args[no][0]]))

    plt.xticks(range(len(names)), names)
    plt.legend()

    plt.show()


if __name__ == "__main__":
    words = ["Majuskuła", "liter", "antonimem", "miar"]
    book = "books/test_file.txt"
    book2 = "books/test_file2.txt"

    book_dict = {"books/test_file.txt" : "Test File 1", "books/test_file2.txt" : "Test File 2"}

    data = return_values(count_freq(book), words)
    data2 = return_values(count_freq(book2), words)

    line_plot(words, book_dict, data, data2)

