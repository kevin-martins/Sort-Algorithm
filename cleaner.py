import sys

def cleaner(arg):
    newList = []
    stock = ''
    size = len(arg)
    for i in range(size):
        if arg[i] != ',' and arg[i] != ' ':
            stock += arg[i]
        if arg[i] == ',' or i == size-1:
            newList.append(int(stock))
            stock = ''
    return newList

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(cleaner(sys.argv[1]))
    else:
        print('\033[31mError: Invalid list\033[0m')
        print('try using:\n\t./cleaner.py \'23, 34, 12, 56...\'')