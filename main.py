from modules.questions_to_menu import main_questions_list, admin_questions_list, operational_questions_list
from helpers import menu

value_opt = lambda funcion : funcion.split('.')[0]

def run():
    opt = ''
    while opt != '3':
        opt = value_opt(menu.menu('Comercializadora', main_questions_list))
        if opt == '1':
            admin_opt = value_opt(menu.menu('Administrar', admin_questions_list))

        elif opt == '2':
            operation_opt = value_opt(menu.menu('Operaciones', operational_questions_list))
            
        else:
            print('Gracias por preferirnos.')

        if opt != '3':
            menu.pause()

if __name__ == '__main__':
    run()