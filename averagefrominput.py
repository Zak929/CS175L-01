#averagefrominput.py
#Zak Ahmed
#CS-175L-01
#Spring 2022
import sys

def main():
    count = 0
    total = 0
    try:
        infile = open('numbers.txt', 'r')
    except IOError:
        print('There was an error trying to open the file')
        sys.exit()
    try:
        for line in infile:
            num = int(line)
            count = count + 1
            total = total + num
            print(f'I read in {count} number(s) Current number is: \
    {num:.2f} Total is: {total:.2f}')
        infile.close()
        average = total / count
        print(f'Average: {average}')
    except ValueError:
        print('There was an error trying to read values inside the file')

if __name__ == '__main__':
    main()
