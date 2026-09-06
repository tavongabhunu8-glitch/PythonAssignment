fruits = ['Mazhanje', 'Tsubvu', 'Hacha','Nhunguru', 'Matamba']

with open('fruits.txt','w') as file:
    for fruit in fruits:
        file.write(fruit + '\n')

with open('fruits.txt', 'r') as file:
    for fruit in file:
        print(fruit.strip())
