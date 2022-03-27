# Opret
def min_funktion_1():
    print('Hej')

# Kald/Brug
min_funktion_1()

# Med et Argument
def min_funktion_2(fnavn):
    print(f'Hej {fnavn}')    

# Kald/Brug
min_funktion_2('Tue')

# Med flere Arguments
def min_funktion_2(fnavn, lname):
    print(f'Hej {fnavn} {lname}')    

# Kald/Brug
min_funktion_2('Tue', 'Hellstern')

# Med flere Arguments + default
def min_funktion_3(fnavn, lname, ven = 'Ja'):
    print(f'Hej {fnavn} {lname}, Ven: {ven}')    

# Kald/Brug
min_funktion_3('Tue', 'Hellstern')
min_funktion_3('Ole', 'Olsen', 'Nej')