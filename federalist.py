import nltk
from main import *
from plot_pca import plotpca
from string import punctuation

authors = ("Hamilton", "Madison", "Disputed", "Jay", "Shared")

papers = {
    'Madison': [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    'Hamilton': [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                 61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                 78, 79, 80, 81, 82, 83, 84, 85],
    'Jay': [2, 3, 4, 5],
    'Shared': [18, 19, 20],
    'Disputed': [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
    'TestCase': [64]
}

def main():
    # federalist_by_author = {}
    # for author, files in papers.items():
    #     federalist_by_author[author] = read_files_into_string(files, author)
    #
    # mergeTXT("outputs/", "merged.txt")
    # toJSON("outputs/")
    # generateMatrix("outputs/json/", "outputs/json/merged.json", "outputs/master.csv", 1000)
    # plotpca("outputs/master_T.csv", "PCA of Federalist Papers")
    plotpca("outputs/master_T_stripped.csv", "PCA of Federalist Papers (Reduced)")


def read_files_into_string(filenames, author):
    for filename in filenames:
        strings = ""
        with open(f'data/federalist_{filename}.txt') as f:
            strings = f.read()
        punct = punctuation + "”“"
        strings = strings.translate(str.maketrans('', '', punct)).lower()
        file = open("outputs/" + author + "_" + str(filename) + ".txt", "w")
        file.write(strings.strip())

main()
