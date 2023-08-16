# 1) Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.

def my_converter(arg):
    try:
        return float(arg)

    except ValueError:
        print('ValueError')
        return 0

    except TypeError:
        print('TypeError')
        return 0

    except NameError:
        print('NameError')
        return 0

    except Exception:
        print('WRONG !')
        return 0
    
print(my_converter(input("Enter the nomber :")))

# 2) Напишіть функцію, що приймає два аргументи. Функція повинна якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернутиу будь-якому іншому випадку повернути кортеж з цих аргументів

def my_calculator(first, second):
    try:
        if first.isdigit() and second.isdigit():
            return int(first) * int(second) 
        
        elif not first.isdigit() and not second.isdigit():
            return first + second
        else:
            my_tuple = (first, second)
            return my_tuple
    except Exception:
        print('WRONG !')
        return 0

user_input = input("Enter something: ")
print(my_calculator(user_input, input("Enter another value: ")))

# 3)Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
#Попросіть користувача ввести свсвій вік.
#- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
#- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
#- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
#- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
#- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
#Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).

def cinema_cashier ():
    max_attempts = 3
    attempts = 0
    while True:
        user_input = input('Enter your real age: ')
        if user_input.isdigit():
         user_input = int(user_input)
         if 3 <= user_input <= 122:
                break
         else:
            print('Wrong! Enter the NUMBER!')
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Remaining attempts: {remaining_attempts}")
        if attempts == max_attempts:
            return ("Exceeded maximum attempts")
            

    if 3 <= user_input < 5:
        declination = " роки "
    elif 5 <= user_input < 21:
        declination = " років "
    elif user_input == 21:
        declination = " рік "
    elif 21 < user_input < 25 :
        declination = " роки "
    elif 25 <= user_input < 31:
        declination = " років "
    elif user_input == 31:
        declination = " рік "
    elif 31 < user_input < 35:
        declination = " роки "
    elif 35 <= user_input < 41:
        declination = " років "
    elif user_input == 41:
        declination = " рік "
    elif 41 < user_input < 45:
        declination = " роки "
    elif 45 <= user_input < 51:
        declination = " років "
    elif user_input == 51:
        declination = " рік "
    elif 51 < user_input < 55:
        declination = " роки "
    elif 55 <= user_input < 61:
        declination = " років "
    elif 61 < user_input < 65:
        declination = " роки "
    elif 65 <= user_input < 71:
        declination = " років "
    elif user_input == 71:
        declination = " рік "
    elif 71 < user_input < 75:
        declination = " роки "
    elif 75 <= user_input < 81:
        declination = " років "
    elif user_input == 81:
        declination = " рік "
    elif 81 < user_input < 85:
        declination = " роки "
    elif 85 <= user_input < 91:
        declination = " років "
    elif user_input == 91:
        declination = " рік "
    elif 91 < user_input < 95:
        declination = " роки "
    elif 95 <= user_input < 101:
        declination = " років "
    elif user_input == 101:
        declination = " рік "
    elif 101 < user_input < 105:
        declination = " роки "
    elif 105 <= user_input < 123:
        declination = " років "
    if user_input < 7:
        return (f"Тобі ж {user_input} {declination}! Де твої батьки?")
    elif 6 <= user_input < 16:
        if '7' in str(user_input):
            return (f"Вам {user_input} {declination}, вам пощастить")
        else: 
            return (f"Тобі лише {user_input} {declination}, а це е фільм для дорослих!")
    elif user_input > 65:
        if '7' in str(user_input):
            return (f"Вам {user_input} {declination}, вам пощастить")
        else: 
            return (f"Вам {user_input} {declination}? Покажіть пенсійне посвідчення!")
    else:
        if '7' in str(user_input):
            return (f"Вам {user_input} {declination}, вам пощастить")
        else: 
            return (f"Незважаючи на те, що вам {user_input} {declination}, білетів всеодно нема!")

print(cinema_cashier())