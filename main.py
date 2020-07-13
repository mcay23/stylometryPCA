import nltk
import json
import pandas as pd
import os
from plot_pca import plotpca
from string import punctuation
from nltk import word_tokenize
from nltk.probability import FreqDist


def main():
    print('Starting..')
    # nltk.download('punkt')
    # generateMatrix('democrats/json/', 'master_merged.json', 'democrats/dem_matrix.csv', 1000)
    # generateMatrix('republicans/json/', 'master_merged.json', 'republicans/repub_matrix.csv', 1000)
    # plotpca("matrix_master.csv")


def fitdict(target_keys, input):
    """
    Assigns values of the required words in target_keys to
    a new list, indexed indentically with sortedKeys()
    Meant to be used to assign an object values to the merged
    frequency set
    """
    list = [0] * len(target_keys)
    count = 0
    for x in target_keys:
        if x in input:
            list[count] = input[x]
        count += 1
    return list


def generateMatrix(directory, source_file, output_file, limit, factor=1000):
    """
    Generates matrix for all .json in folder and writes as a .csv file

    directory - e.g. 'democrats/json/' or 'republicans/json/'
    source_file - Master merged.json dictionary
    output_file - file name, will overwrite (.csv)
    limit - use N words from the master dictionary
    factor - exaggerate values by a factor
    """
    # clear file if it exists
    open(output_file, 'w').close()

    dem_dict = getfirstN(readDist(source_file), limit)
    keys = dem_dict.keys()

    df = pd.DataFrame(keys, columns=['words'])
    for filename in os.listdir(directory):
        if filename.endswith(".json") & (filename != source_file):
            f = open(directory + filename)
            as_list = readDist(directory + filename)
            normalize(as_list, factor)
            fit_list = fitdict(keys, as_list)
            col_name = filename[:-5]
            df[col_name] = fit_list
            f.close()
    df.to_csv(output_file, index=False)

def normalize(dict, exaggerate_factor):
    """
    Divide each dict entry by total number of words

    exaggerate_factor lets you multiply by a value to increase readability
    """
    num_words = sum(dict.values())
    for key, value in dict.items():
        dict[key] = value / num_words * exaggerate_factor

def sortedKeys(dict):
    """
    force sort a dict by values, then get the sorted keys
    """
    list = []
    for key, value in sortdict(dict):
        list.append(key)
    return list


def sortdict(dict):
    """
    sort dictionaries by values
    """
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)


def printdict(dict):
    """
    print dictionaries
    """
    for key, value in dict.items():
        print(key, value)


def getfirstN(dict, N):
    """
    get first N elements of a dict
    """
    x = sortdict(dict)
    ret = {}
    count = 0
    for key, value in x:
        ret[key] = value
        count += 1
        if count == N:
            break
    return ret


def readDist(dir):
    """
    read frequency distribution from textfile
    """
    with open(dir) as file:
        list = json.load(file)
    return list


def dist(dir):
    """
    create frequency distribution from textfile
    """
    with open(dir) as f:
        data = f.read()
    fdist = FreqDist(word.lower() for word in word_tokenize(data))
    return fdist


def writeDist(input, output):
    """
    write text file to JSON of frequencies
    """
    items = dist(input)
    with open(output, 'w') as json_file:
      json.dump(items, json_file)


def toJSON(directory):
    """
    write all text files in directory to FreqDist JSON
    param: directory -> 'democrats/' or 'republicans/'
    """
    for filename in os.listdir(directory):
        input_file = directory + filename
        output_file = directory + "json/" + filename[:-4] + ".json"
        if filename.endswith(".txt"):
            writeDist(input_file, output_file)


def mergeTXT(directory, f):
    """
    merge all .TXT files in directory, then output as f
    """
    open(f, 'w').close()
    output_file = open(f, 'a')
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            f = open(directory + filename)
            output_file.write(f.read())
            count += 1
            f.close()
    print("Merged " + str(count) + " files.");
    output_file.close()

main()
