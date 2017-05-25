from _basic_func import line_plot, return_values, count_freq

def add_folder_to_filenames(filenames, folder_name):
    result = []
    for e in filenames:
        e = folder_name + e
        result.append(e)
    return result

def create_book_dict(filenames, titles):
    for e in zip(filenames, titles):
        book_dict[e[0]] = e[1]

    return book_dict

words = ['morze', 'Polska', 'sklep', 'wiosna', 'morze', 'dziecko']
filenames = ['books/lord-jim.txt', 'books/przedwiosnie.txt', 'books/sklepy-cynamonowe.txt', 'books/szewcy.txt',
             'books/ziemia-obiecana-tom-pierwszy.txt']
titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]
book_dict = {'books/lord-jim.txt': 'Lord Jim', 'books/przedwiosnie.txt': 'Przedwiośnie',
             'books/sklepy-cynamonowe.txt': 'Sklepy cynamonowe',
             'books/szewcy.txt': 'Szewcy', 'books/ziemia-obiecana-tom-pierwszy.txt': 'Ziemia obiecana Tom I'}



def color_lines(func, words, book_dict, list_of_files):
    data = []
    for e in list_of_files:
        data.append(return_values(count_freq(e), words))
    func(words, book_dict, *data)           # * odpakowuje listę albo tupla do *args'ów



if __name__ == "__main__":
    color_lines(line_plot, words, book_dict, filenames)

"""
DROBNA UWAGA:
zmieniłem trochę formułę tej funkcji, tj. color_lines() przyjmuje wiecej argumentów niż "texts"
zgaduje jednak, ze trochę nie o to chodzi, żebym tę funkcję opakował teraz w jeszcze jedną funkcję :)
"""


