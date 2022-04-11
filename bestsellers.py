#bestsellers.py
#Zak Ahmed
#CS-175-03
#Spring 2022

import sys

def main():
    menu()

def menu():
    print('What would you like to do?')
    print('   1: Look up year range')
    print('   2: Look up month/year')
    print('   3: Search for author')
    print('   4: Search for title')
    print('   Q: Quit')
    userinput = input()
    while userinput != 'Q':
        if userinput == '1':
            yearfunc(books)
        elif userinput == '2':
            yearmonth(books)
        elif userinput == '3':
            authorfunc(books)
        elif userinput == '4':
            titlefunc(books)
        elif userinput.upper() == 'Q':
            print('Done')
            sys.exit()
        else:
            print('Invalid input')
        userinput = input()

books = []
booklist = open('bestsellers.txt','r')
for book in booklist:
    datalist = book.strip('\n')
    columns = datalist.split('\t')
    books.append(columns)
length = len(books)
print(f'Read {length} books')

    
def showBooks(books):
    for book in books:
        print(f'{book[0]} by: {book[1]} (pub date: {book[3]})')

def titlefunc(books):
    userinput = str(input('Enter search string: '))
    found = False
    for item in books:
        l = item[0].lower()
        userinput = userinput.lower()
        if l.find(userinput)!= -1:
            found = True
            print(f'{item[0]} by: {item[1]} (pub date: {item[3]})')
    if not found:
        print('No items found matching search')
    print('What would you like to do?')
    print('   1: Look up year range')
    print('   2: Look up month/year')
    print('   3: Search for author')
    print('   4: Search for title')
    print('   Q: Quit')
    return

def authorfunc(books):
    userinput = str(input('Enter author: '))
    found = False
    for item in books:
        l = item[1].lower()
        userinput = userinput.lower()
        if l.find(userinput)!= -1:
            found = True
            print(f'{item[0]} by: {item[1]} (pub date: {item[3]})')
    if not found:
        print('No items found matching search')
    print('What would you like to do?')
    print('   1: Look up year range')
    print('   2: Look up month/year')
    print('   3: Search for author')
    print('   4: Search for title')
    print('   Q: Quit')
    return

def yearfunc(books):
    userinput1 = int(input('Enter start year: '))
    userinput2 = int(input('Enter end year: '))
    found = False
    for item in books:
        date = item[3].split('/')
        if userinput1 <= int(date[2]) and userinput2 >= int(date[2]):
            found = True
            print(f'{item[0]} by: {item[1]} (pub date: {item[3]})')
    if not found:
        print('No items found matching search')
    print('What would you like to do?')
    print('   1: Look up year range')
    print('   2: Look up month/year')
    print('   3: Search for author')
    print('   4: Search for title')
    print('   Q: Quit')
    return

def yearmonth(books):    
    userinput1 = int(input('Enter month (1-12): '))
    userinput2 = int(input('Enter year: '))
    found = False
    for item in books:
        date = item[3].split('/')
        if userinput1 == int(date[0]) and userinput2 == int(date[2]):
            found = True
            print(f'{item[0]} by: {item[1]} (pub date: {item[3]})')
    if not found:
        print('No items found matching search')
    print('What would you like to do?')
    print('   1: Look up year range')
    print('   2: Look up month/year')
    print('   3: Search for author')
    print('   4: Search for title')
    print('   Q: Quit')
    return

main()


