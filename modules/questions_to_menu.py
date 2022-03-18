
questions_list = lambda q_list, value, name : [f"{_[value]}. {_[name]}" for _ in q_list]
main_questions = [
    {'value': 1, 'name':'Administrar'},
    {'value': 2, 'name':'Operaciones'},
    {'value': 3, 'name':'Salir'},
]
main_questions_list = questions_list(main_questions, 'value', 'name')

admin_questions = [
    {'value': 1, 'name':'Clientes'},
    {'value': 2, 'name':'Productos'},
    {'value': 3, 'name':'Vendedores'},
    {'value': 4, 'name':'Proveedores'},
    {'value': 5, 'name':'Atras'},
]
admin_questions_list = questions_list(admin_questions, 'value', 'name')

operational_questions = [
    {'value': 1, 'name':'Ventas'},
    {'value': 2, 'name':'Atras'},
]
operational_questions_list = questions_list(operational_questions, 'value', 'name')

customer_questions = [
    {'value': 1, 'name':'Mostrar Clientes'},
    {'value': 2, 'name':'Agregar Cliente'},
    {'value': 3, 'name':'Eliminar Cliente'},
    {'value': 4, 'name':'Atras'},
]
customer_questions_list = questions_list(customer_questions, 'value', 'name')

products_questions = [
    {'value': 1, 'name':'Mostrar Productos'},
    {'value': 2, 'name':'Agregar Producto'},
    {'value': 3, 'name':'Eliminar Producto'},
    {'value': 4, 'name':'Atras'},
]
products_questions_list = questions_list(products_questions, 'value', 'name')

seller_questions = [
    {'value': 1, 'name':'Mostrar Vendedores'},
    {'value': 2, 'name':'Agregar Vendedor'},
    {'value': 3, 'name':'Eliminar Vendedor'},
    {'value': 4, 'name':'Atras'},
]
seller_questions_list = questions_list(seller_questions, 'value', 'name')

supplier_questions = [
    {'value': 1, 'name':'Mostrar proveedores'},
    {'value': 2, 'name':'Agregar proveedor'},
    {'value': 3, 'name':'Eliminar proveedor'},
    {'value': 4, 'name':'Atras'},
]
supplier_questions_list = questions_list(supplier_questions, 'value', 'name')