#averagefrominput.py
#Zak Ahmed
#CS-175L-01
#Spring 2022

def main():
    # Open a file for reading.
    count = 0
    total = 0
    infile = open('numbers.txt', 'r')
    for line in infile:
        num = int(line)
        count = count + 1
        total = total + num
        print(f'I read in {count} number(s) Current number is: \
{num:.2f} Total is: {total:.2f}')
    #Close the file.
    infile.close()

    # Add the numbers.
    average = total / count

    # Display the average.
    print(f'Average: {average}')

# Call the main function.
if __name__ == '__main__':
    main()
