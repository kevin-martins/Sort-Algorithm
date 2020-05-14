import sys
import random

def usage():
    print('How to use:')
    print('\033[32mFlags:')
    print('\t-help: Print the \'How to use\' pannel.')
    print('\t-repeat: False by default. Can be set to true by adding the value after.')
    print('\t-number: 100 by default. You can change it by adding the desier value after.')
    print('\t-max: 1000 by default.You can change it by adding the desier value after.\033[0m')
    print('./generator.py -help -repeat true -number 50 -max 300')

def remove_occurence(liste, number):
    for i in range(len(liste)):
        if number == liste[i]:
            return False
    return True

def generator(repeat, number, max_value):
    liste = []
    valid_number = False
    for i in range(number):
        valid_number = False
        while valid_number == False:
            number = random.randint(1, max_value)
            if repeat == False:
                valid_number = remove_occurence(liste, number)
            else:
                valid_number = True
        liste.append(number)
    return liste

def repeat_flag(repeat, i):
    try:
        repeat = sys.argv[i+1].lower() in ['True', 'true', '1']
    except ValueError:
        print('\033[31mError: Incorrect repeat flag value. Only boolean accepted\033[0m')
        print('Using the default value of -repeat = ', repeat)
    except IndexError:
        print('\033[31mError: repeat flag is empty. Try with True or False\033[0m')
        print('Using the default value of -repeat = ', repeat)
    return repeat

def number_flag(number, i):
    try:
        number = int(sys.argv[i+1])
    except ValueError:
        print('\033[31mError: Incorrect number flag value. Only whole numbers accepted\033[0m')
        print('Using the default value of -number = ', number)
    except IndexError:
        print('\033[31mError: number flag is empty. Try with 100 or 1000\033[0m')
        print('Using the default value of -number = ', number)
    return number

def max_flag(max_value, i):
    try:
        max_value = int(sys.argv[i+1])
    except ValueError:
        print('\033[31mError: Incorrect max_number flag value. Only whole numbers accepted\033[0m')
        print('Using the default value of -max = ', max_value)
    except IndexError:
        print('\033[31mError: max_number flag is empty. Try with 1000 or 10000\033[0m')
        print('Using the default value of -max = ', max_value)
    return max_value

def check_error(repeat, number, max_value):
    if repeat == False and number > max_value:
        print('\033[31mError: You can\'t generate more numbers than the max_value specified\033[0m')
        number = 100
        max_value = 1000
        print('Using the default value of -number', number, 'and -max = ', max_value)
    if max_value < 1:
        print('\033[31mError: You can\'t generate more numbers than the max_value specified\033[0m')
        max_value = 1000
        print('Using the default value of -max = ', max_value)
    return repeat, number, max_value

def check_arg():
    repeat = False
    number = 100
    max_value = 1000
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '-help':
            usage()
        if sys.argv[i] == '-repeat' or sys.argv[i] == '-r':
            repeat = repeat_flag(repeat, i)
        if sys.argv[i] == '-number' or sys.argv[i] == '-n':
            number = number_flag(number, i)
        if sys.argv[i] == '-max' or sys.argv[i] == '-max_value' or sys.argv[i] == '-m':
            max_value = max_flag(max_value, i)
    return check_error(repeat, number, max_value)

def main():
    repeat, number, max_value = check_arg()
    return generator(repeat, number, max_value)

if __name__ == '__main__':
    print(main())