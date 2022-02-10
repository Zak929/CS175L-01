#CS175L-01
#Zak Ahmed
#restaurant

vegetarian = False
vegan = False
gluten_free = False
loop_continue = True

while loop_continue:
    vegetarian = False
    vegan = False
    gluten_free = False

    response_1 = str(input('Is anyone in your party a vegetarian?(Yes or No) '))
    response_2 = str(input('Is anyone in your party a vegan?(Yes or No) '))
    response_3 = str(input('Is anyone in your party gluten-free?(Yes or No) '))
    if response_1.lower() == 'yes':
        vegetarian = True
    if response_2.lower() == 'yes':
        vegan = True
    if response_3.lower() == 'yes':
        gluten_free = True

    print('Here are your restaurant choices:')
    if (not vegetarian) and (not vegan) and (not gluten_free):
        print("Joe's Gourmet Burgers")
    if (not vegan) and (not gluten_free):
        print("Mama's Fine Italian")
    if (not vegan):
        print('Main Street Pizza')
    print('Corner Cafe')
    print("Chef's Kitchen")

    response_4 = str(input('Would you like to do another restuarant search?(Yes or No) '))
    if response_4.lower() == 'yes':
        loop_continue = True
    else:
        print('Program has ended')
        break


    
