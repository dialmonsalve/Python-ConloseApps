from bebidas import bebidas
from menu import MENU, recursos

def ui(bebida_seleccionada:str):

    if bebida_seleccionada == 'reporte':
        reporte()
    elif bebida_seleccionada == 'espresso' or bebida_seleccionada == 'latte' or bebida_seleccionada == 'cappuccino':
        bebidas(bebida_seleccionada)
        
        valor_bebida = MENU[bebida_seleccionada]["costo"]

        if bebidas(bebida_seleccionada):
            insert_coins(bebida_seleccionada, valor_bebida )
    else:
        print('Opción no existe')


def reporte():

    print(f"\n\tAgua: {recursos['agua'] }")
    print(f"\tLeche: {recursos['leche'] }")
    print(f"\tCafé: {recursos['cafe'] }\n")
        

def insert_coins(bebida_seleccionada:str, valor_bebida:float ):

    if bebida_seleccionada != 'reporte':
        
        print(f'''
    NUESTRA MÁQUINA SOLO ACEPTA LAS SIGUIENTES MONEDAS:

    OPCIÓN |      VALOR       | DENOMINACIÓN
    -----------------------------------------
    1      |   1  centavo     |   (Penny)
    5      |   5  centavos    |   (Nickel)
    10     |   10 centavos    |   (Dime)
    25     |   25 centavos    |   (Quarter)
    
    VALOR BEBIDA: {valor_bebida}

    Introduzca las monedas:\n''')

        penny   = 0.01
        nickel  = 0.05
        dime    = 0.10
        quarter = 0.25
        
        total = 0
        
        while total < valor_bebida:
            insert_coin = int(input(''))

            if insert_coin == 1:
                total += penny
                print(f"Saldo actual: {round(total,2)}")
            elif insert_coin == 5:
                total += nickel
                print(f"Saldo actual: {round(total,2)}")
            elif insert_coin == 10:
                total += dime
                print(f"Saldo actual: {round(total,2)}")
            elif insert_coin == 25:
                total += quarter
                print(f"Saldo actual: {round(total,2)}")
            else:
                print(f'Moneda no aceptada por nuestra máquina. Saldo actual: {total}')
        
    if round(total,2) > valor_bebida:
        print(f'Aca tiene su devolución: ${round(total-valor_bebida,2)} ')
        print(f"Su {bebida_seleccionada} ha sido preparado")
        return total