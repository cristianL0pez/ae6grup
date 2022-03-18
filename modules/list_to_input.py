import inquirer

new_customer = [
    inquirer.Text( name = 'rut', message ='Ingrese rut del cliente'),
    inquirer.Text( name = 'name', message ='Ingrese nombre del cliente'),
    inquirer.Text( name = 'surname', message ='Ingrese apellido del cliente'),
    inquirer.Text( name = 'email', message ='Ingrese el email del cliente'),
    inquirer.Text( name = 'balance', message ='Ingrese el saldo del cliente'),
]

new_product = [
    inquirer.Text( name = 'name', message ='Ingrese nombre del producto'),
    inquirer.Text( name = 'category', message ='Ingrese la categoria a la que pertenece'),
    inquirer.Text( name = 'stock', message ='Ingrese el stock del producto'),
    inquirer.Text( name = 'value', message ='Ingrese el precio neto del producto'),
    inquirer.Text( name = 'made_in', message ='Ingrese donde fue hecho el producto'),
    inquirer.Text( name = 'rut', message ='Ingrese rut del proveedor'),
    inquirer.Text( name = 'business_name', message ='Ingrese el nombre legal del proveedor'),
    inquirer.Text( name = 'supplier_name', message ='Ingrese el nombre de fantasia del proveedor'),
]

new_supplier = [
    inquirer.Text( name = 'rut', message ='Ingrese el rut del proveedor'),
    inquirer.Text( name = 'business_name', message ='Ingrese el nombre legal'),
    inquirer.Text( name = 'supplier_name', message ='Ingrese el nombre de fantasia'),
]

new_seller = [
    inquirer.Text( name = 'rut', message ='Ingrese el rut del vendedor'),
    inquirer.Text( name = 'name', message ='Ingrese el nombre'),
    inquirer.Text( name = 'surname', message ='Ingrese el apellido?'),
    inquirer.Text( name = 'section', message ='Ingrese la seccion a la que pertenece'),
]