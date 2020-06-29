def false_multiplier(number):
    import random
    #wrong is storing any random value in b/w 1,9
    wrong = random.randint(1,9 )
    table = []
    for i in range(1, 11):
        product = number * i
        table.append(product)
    #at random index number of table list, any random number b/w 0 and 10 number will be added to item on that index
    #eg. if table[5] = 18 then table[5] = 18 + (0,10)
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def find_mistake(false_table, number):
    for x in range(1, 11):
        if false_table[x-1] != x*number:
            return x
        
    return None

def correct_table(number):
    table = []
    for i in range(1, 11):
        product = number * i
        table.append(product)
    return table



if __name__ == '__main__':
    print("\nWelcome to the program\tcreated by \x1b[6;30;42m'Jatin Rathi'\x1b[0m")
    name = input("Enter the name who is creating false multiplier : ").capitalize()
    number = int(input(f"\nEnter the number to display {name}'s multiplier : "))
    false_table = false_multiplier(number)
    j = 1
    for i in false_table:
        print(f"({j}) : {number}  x  {j}  = {i}")
        j += 1
    user = input(f"\nPress 'ENTER' to see the mistake in {name}'s Multiplication Table ")
    mistake_sno = find_mistake(false_table, number)
    print(f"=> S.NO.{mistake_sno} is false in {name}'s Multiplication Table")
    show = input(f"\nPress 'ENTER' to display the True Multiplication Table\n")
    j = 1
    for k in correct_table(number):
        print(f"{number}  x  {j}  = {k}")
        j += 1
