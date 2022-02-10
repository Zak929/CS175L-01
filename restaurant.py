#CS175L-01
#Zak Ahmed
#restaurant

vegetarian = False
vegan = False
gluten_free = False

response_1 = str(input('Is anyone in your party a vegetarian? '))
response_2 = str(input('Is anyone in your party a vegan? '))
response_3 = str(input('Is anyone in your party gluten-free? '))

if response_1 == 'yes':
    vegetarian = True
if response_2 == 'yes':
    vegan = True
if response_3 == 'yes':
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


    
