
from ui import ui

def main():
    bebida_seleccionada = ''
    
    while bebida_seleccionada != 'salir':
        bebida_seleccionada = input('Que quieres? (espresso/latte/cappuccino): ').lower()
        ui(bebida_seleccionada)