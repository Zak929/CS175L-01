#average_grade_function.py
#Zak Ahmed
#CS-175L-01
#Spring 2022

def main():
    score1,score2,score3,score4,score5,average = calc_average()
    g1,g2,g3,g4,g5,ga = determine_grade(score1,score2,score3,score4,score5,average)
    print('Score        Numeric Grade          Letter Grade')
    print('------------------------------------------------')
    print(f'score 1:          {score1}                    {g1}')
    print(f'score 2:          {score2}                    {g2}')
    print(f'score 3:          {score3}                    {g3}')
    print(f'score 4:          {score4}                    {g4}')
    print(f'score 5:          {score5}                    {g5}')
    print(f'Average score:    {average}                  {ga}')
    loop_again = repeat()
    if loop_again == True:
        main()
    
def calc_average():
    total = 0
    score1 = int(input('Enter score 1: '))
    total = total + score1
    score2 = int(input('Enter score 2: '))
    total = total + score2
    score3 = int(input('Enter score 3: '))
    total = total + score3
    score4 = int(input('Enter score 4: '))
    total = total + score4
    score5 = int(input('Enter score 5: '))
    total = total + score5
    average = total / 5
    return score1,score2,score3,score4,score5,average
    
def determine_grade(g1,g2,g3,g4,g5,ga):
    if g1 >= 90:
        g1 = "A"
    elif g1 >= 80:
        g1 = "B"
    elif g1 >= 70:
        g1 = "C"
    elif g1 >= 60:
        g1 = "D"
    else:
        g1 = "F"
    if g2 >= 90:
        g2 = "A"
    elif g2 >= 80:
        g2 = "B"
    elif g2 >= 70:
        g2 = "C"
    elif g2 >= 60:
        g2 = "D"
    else:
        g2 = "F"
    if g3 >= 90:
        g3 = "A"
    elif g3 >= 80:
        g3 = "B"
    elif g3 >= 70:
        g3 = "C"
    elif g3 >= 60:
        g3 = "D"
    else:
        g3 = "F"
    if g4 >= 90:
        g4 = "A"
    elif g4 >= 80:
        g4 = "B"
    elif g4 >= 70:
        g4 = "C"
    elif g4 >= 60:
        g4 = "D"
    else:
        g4 = "F"
    if g5 >= 90:
        g5 = "A"
    elif g5 >= 80:
        g5 = "B"
    elif g5 >= 70:
        g5 = "C"
    elif g5 >= 60:
        g5 = "D"
    else:
        g5 = "F"
    if ga >= 90:
        ga = "A"
    elif ga >= 80:
        ga = "B"
    elif ga >= 70:
        ga = "C"
    elif ga >= 60:
        ga = "D"
    else:
        ga = "F"
    return g1,g2,g3,g4,g5,ga

def repeat():
    loop_again = str(input('Would you like to continue(yes/no): '))
    if loop_again == 'yes':
        return True
    else:
        return False
main()
    
