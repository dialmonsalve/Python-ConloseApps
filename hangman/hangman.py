def hangman(fail:int):
    
    if fail == 0:
        print(""" 
            |-------|
                    |
                    |
                    |
                    |
                    |
                |-------|\n"""
            )
    elif fail == 1:
        print(""" 
            |-------|
            O       |
                    |
                    |
                    |
                    |
                |-------|\n"""
            )
    elif fail == 2:
        print(""" 
            |-------|
            O       |
            |       |
            |       |
                    |
                    |
                |-------|\n"""
            )
    elif fail == 3:
        print(""" 
            |-------|
            O       |
            |\      |
            |       |
                    |
                    |
                |-------|\n"""
            )
    elif fail == 4:
        print(""" 
            |-------|
            O       |
           /|\      |
            |       |
                    |
                    |
                |-------|\n"""
            )
    elif fail == 5:
        print(""" 
            |-------|
            O       |
           /|\      |
            |       |
             \      |
                    |
                |-------|\n"""
            )
    else:
        print('='*20, 'GAME OVER','='*20)
        print(""" 
            |-------|
            O       |
           /|\      |
            |       |
           / \      |
                    |
                |-------|\n"""
            )