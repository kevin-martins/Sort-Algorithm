import sys
import time
from tri import cleaner

def bubble_sort(liste, comp, dep):
    is_sorted = False
    parse = 0
    while is_sorted == False:
        is_sorted = True
        parse += 1
        for i in range(len(liste)-parse):
            if liste[i] > liste[i+1]:
                is_sorted = False
                stock = liste[i]
                liste[i] = liste[i+1]
                liste[i+1] = stock
                dep += 1
            comp += 1
    return liste, comp, dep

def main():
    newList = cleaner.cleaner(sys.argv[1])
    comp = 0
    dep = 0
    print('unsorted list: ', newList)
    beggin = time.time()
    sortedList, comp, dep = bubble_sort(newList, comp, dep)
    end = time.time()
    print('sorted list:   ', sortedList)
    print('It takes ', round(end-beggin, 3), 'seconds to sort ', len(newList), ' numbers.')
    print(comp , ' comparaison, ', dep, ' moves')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('\033[31mError: Invalid list\033[0m')
    else:
        main()