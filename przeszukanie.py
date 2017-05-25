from przyklad_liniowy import make_heatmap_iteracja

words = ["Polska", "duży"]

nazwy_plikow = ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt",
                "ziemia-obiecana-tom-pierwszy.txt"]

if __name__ == "__main__":
    make_heatmap_iteracja(nazwy_plikow, words)