import sys
import time
from tri import cleaner

def insert_sort(liste, comp, dep):
    for i in range(1,len(liste)):
        is_position = liste[i]
        j = i
        while j>0 and liste[j-1]>is_position:
            liste[j]=liste[j-1]
            j = j-1
            comp += 1
        liste[j]=is_position
        dep += 1
    return liste, comp, dep

def main():
    newList = cleaner.cleaner(sys.argv[1])
    comp = 0
    dep = 0
    print('unsorted list: ', newList)
    beggin = time.time()
    sortedList, comp, dep = insert_sort(newList, comp, dep)
    end = time.time()
    print('sorted list:   ', sortedList)
    print('It takes ', round(end-beggin, 3), 'seconds to sort ', len(newList), ' numbers.')
    print(comp , ' comparaison, ', dep, ' moves')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('\033[31mError: Invalid list\033[0m')
    else:
        main()