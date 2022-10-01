import sys
import csv
from SimilarRecipes import *


def main():
    if len(sys.argv) < 2:
        raise Exception("Not enough arguments!")
    # try:
    ingridients = sys.argv[1:]
    ingridients_clean = []
    for ingr in ingridients:
        if ingr[-1] == ',':
            ingr = ingr.rstrip(',')
            ingridients_clean.append(ingr)
        else:
            ingridients_clean.append(ingr)
    with open ('data/names.csv') as csv_file:
          names = [line.strip() for line in csv_file.readlines()]
    for ing in ingridients_clean:
        if ing not in names:
            print('Ingridient ' + ing + ' is not found in base')
            exit()
    print(ingridients_clean)
    print('I. OUR FORECAST')


    print('\n')
    print('II. NUTRITION FACTS')

    print('\n')
    print('III. TOP-3 SIMILAR RECIPES')
    sr = SimilarRecipes(ingridients_clean)
    # print('Hello')
    print(sr.top_similar(3))
    # except:
    #     print('Some error happened')



if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)