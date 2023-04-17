from menu import MENU, recursos

def bebidas(bebida_seleccionada:str):
    for item in MENU[bebida_seleccionada]["ingredientes"]:
        if MENU[bebida_seleccionada]["ingredientes"][item] >= recursos[item]:
            print(f"No hay suficientes {item} para preparar {bebida_seleccionada}")
            return False
    return True
