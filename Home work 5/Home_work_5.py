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
        if isinstance(first, (int, float)) and isinstance(second, (int, float)):
            return first * second
        elif isinstance(first, str) and isinstance(second, str):
            return first + second
        else:
            return (first, second)
    except Exception:
        print('WRONG !')
        return 0

user_input1 = input("Enter something: ")
user_input2 = input("Enter another value: ")

try:
    user_input1_float = float(user_input1)
except ValueError:
    user_input1_float = user_input1

try:
    user_input2_float = float(user_input2)
except ValueError:
    user_input2_float = user_input2

result = my_calculator(user_input1_float, user_input2_float)
print(result)
# 3)Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
#Попросіть користувача ввести свсвій вік.
#- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
#- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
#- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
#- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
#- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
#Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).

def generate_message(user_input, declination):
    if '7' in str(user_input):
        return f"Вам {user_input} {declination}, вам пощастить"
    elif user_input < 7:
        return f"Тобі ж {user_input} {declination}! Де твої батьки?"
    elif 6 <= user_input < 16:
        return f"Тобі лише {user_input} {declination}, а це е фільм для дорослих!"
    elif user_input > 65:
        return f"Вам {user_input} {declination}? Покажіть пенсійне посвідчення!"
    else:
        return f"Незважаючи на те, що вам {user_input} {declination}, білетів всеодно нема!"

def cinema_cashier():
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
                print("Exceeded maximum attempts")
                exit()

    def get_age_declination(user_input):
        if user_input % 10 == 1 and user_input != 11:
            declination = " рік "
        elif 2 <= user_input % 10 <= 4 and (user_input < 10 or user_input > 20):
            declination = " роки "
        else:
            declination = " років "
        return declination

    declination = get_age_declination(user_input)
    message = generate_message(user_input, declination)
    
    return message

print(cinema_cashier())