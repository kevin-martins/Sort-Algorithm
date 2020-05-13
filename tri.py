import sys
import time
import cleaner
import generator
from sort_algorithm import bubble_sort
from sort_algorithm import insert_sort

def usage():
    print('How to use:')
    print('./tri.py')
    print('\033[32mFlags:')
    print('\t-help: Print the \'How to use\' pannel')
    print('\t-all: Lunch all kind of sort algorithm')
    print('\t-tri: Kind of sort algorithm the program have')
    print('\t-bubble: Specify the Bubble Sort algorithm')
    print('\t-insert: Specify the Insert Sort algorythm')
    print('\t-print_unsorted: Print the unsorted list of numbers')
    print('\t-print_sorted: Print the sorted list of numbers')
    print('\t-repeat: False by default. Can be set to true by adding the value after')
    print('\t-number: 100 by default. You can change it by adding the desier value after')
    print('\t-max: 1000 by default.You can change it by adding the desier value after\033[0m')

def sort_algorithm():
    print('Sort algorithm:\n\t-Bubble sort\n\t-Insert sort')

def more_info(duration, comp, dep, print_list):
    if print_list:
        print('\nIt took ', duration, 'seconds')
        print(comp , ' comparaison, ', dep, ' moves')
    else:
        print('\tIt took ', duration, 'seconds')
        print('\t', comp , ' comparaison, ', dep, ' moves')

def bubble_algorithm(unsortedList, print_unsorted, print_sorted):
    print('-bubble_sort:')
    comp = 0
    dep = 0
    start = time.time()
    sortedList, comp, dep = bubble_sort.bubble_sort(unsortedList, comp, dep)
    end = time.time()
    if print_sorted:
        print('sorted list:   ', sortedList)
    more_info(round(end-start, 3), comp, dep, print_sorted)
    

def insert_algorithm(unsortedList, print_unsorted, print_sorted):
    print('-insert_sort:')
    comp = 0
    dep = 0
    start = time.time()
    sortedList, comp, dep = insert_sort.insert_sort(unsortedList, comp, dep)
    end = time.time()
    if print_sorted:
        print('sorted list:   ', sortedList)
    more_info(round(end-start, 3), comp, dep, print_sorted)

def start(algo, auto, print_unsorted, print_sorted):
    unsortedList = []
    if auto:
        unsortedList = cleaner.cleaner(auto)
    else:
        unsortedList = generator.main()
    if print_unsorted:
        print('unsorted list: ', unsortedList)
        print('\nFor ', len(unsortedList), ' numbers:')
    else:
        print('For ', len(unsortedList), ' numbers:')
    if algo == 'bubble_sort' or algo == 'all':
        bubble_algorithm(unsortedList[:], print_unsorted, print_sorted)
    if algo == 'insert_sort' or algo == 'all':
        insert_algorithm(unsortedList[:], print_unsorted, print_sorted)

def main():
    algo = 'all'
    auto = ''
    print_unsorted = False
    print_sorted = False
    print_help = False
    print_algo = False
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-bubble_sort' or sys.argv[i] == '-bubble' or sys.argv[i] == 'bubble_sort' or sys.argv[i] == 'bubble' or sys.argv[i] == '-b':
            algo = 'bubble_sort'
        if sys.argv[i] == '-insert_sort' or sys.argv[i] == '-insert' or sys.argv[i] == 'insert_sort' or sys.argv[i] == 'insert' or sys.argv[i] == '-i':
            algo = 'insert_sort'
        if sys.argv[i] == '-all' or sys.argv[i] == 'all':
            algo = 'all'
        if sys.argv[i] == '-print_unsorted':
            print_unsorted = True
        if sys.argv[i] == '-print_sorted':
            print_sorted = True
        if sys.argv[i][0] == '\'' and sys.argv[i][-1] == '\'':
            print('auto:', sys.argv[i][0])
            auto = sys.argv[i]
        if sys.argv[i] == '-h' or sys.argv[i] == '-help' or sys.argv[i] == 'help':
            print_help = True
        if sys.argv[i] == '-tri' or sys.argv[i] == '-t':
            print_algo = True
    if print_help:    
        usage()
        if print_algo:
            sort_algorithm()
        return 0
    if print_algo:
        sort_algorithm()
    start(algo, auto, print_unsorted, print_sorted)

if __name__ == '__main__':
    main()