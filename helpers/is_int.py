def is_int_except(num):
    try:
        num = int(num)
        return num
    except ValueError:
        return 'La edad debe ser un numero'

def is_int():
    while True:
        number_input = input('escribe tu edad: ')
        print(is_int_except(number_input))