#pgzero
import random

WIDTH = 900
HEIGHT = 600
TITLE = "TIC TAC TOE"
FPS = 30

turn = 'user'
CPU_mov = 0
score = 0

fullSpaces = [] # Lista para guardar los movimientos ya realizados
columnsD = 2 # Variabla para la iteracion de matriz de derecha a izquierda (cruzada)
mode = 'neutro' #Establece la victoria o derrota 

# Tic Tac Toe
TTT = [[0,0,0],
       [0,0,0],
       [0,0,0]]  

# White squares
background = Actor('background',)
square1 = Actor('square',(130,100))
square2 = Actor('square',(300,100))
square3 = Actor('square',(470,100))
square4 = Actor('square',(130,270))
square5 = Actor('square',(300,270))
square6 = Actor('square',(470,270))
square7 = Actor('square',(130,440))
square8 = Actor('square',(300,440))
square9 = Actor('square',(470,440))

# checks the CPU's movements
def CPU_process():
    global CPU_mov
    global turn
    
    while True:
        CPU_mov = random.randint(1, 9)
        if CPU_mov not in fullSpaces: # Garantiza que la computadora no haga un movimiento en un cuadro lleno
            
            if CPU_mov == 1:
                square1.image = 'circle'
                TTT[0][0] = 2 # El num. 2 representa la computadora y el 1 al usuario
                
            elif CPU_mov == 2:
                square2.image = 'circle'
                TTT[0][1] = 2
                
            elif CPU_mov == 3:
                square3.image = 'circle'
                TTT[0][2] = 2
                
            elif CPU_mov == 4:
                square4.image = 'circle'
                TTT[1][0] = 2
                
            elif CPU_mov == 5:
                square5.image = 'circle'
                TTT[1][1] = 2
                
            elif CPU_mov == 6:
                square6.image = 'circle'
                TTT[1][2] = 2
                
            elif CPU_mov == 7:
                square7.image = 'circle'
                TTT[2][0] = 2
                
            elif CPU_mov == 8:
                square8.image = 'circle'
                TTT[2][1] = 2
                
            elif CPU_mov == 9:
                square9.image = 'circle'
                TTT[2][2] = 2
            
            fullSpaces.append(CPU_mov)
            turn = 'user'
            break
        
def check_winner():
    global score
    global columnsD
    global columnsI
    global mode
    
    # USUARIO / VICTORIA
    
    # Verifica victorias por el usuario de manera horizontal
    for r in range(len(TTT)): # Iteración por las filas
        for c in range(3): # Iteracion por las columnas
            if TTT[r][c] == 1:
                score += 1
            else: 
                score = 0
        if score == 3:
            mode = 'win'
                
    # Verifica victorias por el usuario de manera vertical
    for c in range(len(TTT[0])): 
        for r in range(len(TTT)):
            if TTT[r][c] == 1:
                score += 1
            else:
                score = 0
        if score == 3:
            mode = 'win'
    
    #Verifica la victoria de forma cruzada de izquierda a derecha               
    for i in range(len(TTT)):

        if TTT[i][i] == 1:
            score += 1
        else:
            score = 0
        
        if score == 3:
            mode = 'win'
    
    #Verifica la victoria de forma cruzada de derecha a izquierda
    for r in range(len(TTT)):
        if columnsD >= 0:
            if TTT[r][columnsD] == 1:
                score += 1
                columnsD -= 1
            else:
                score = 0
        
        if score == 3:
            mode = 'win'
            
    # CPU / DERROTA
    
    #Verifica victorias por la CPU de manera horizontal
    for r in range(len(TTT)): # Iteración por las filas
        for c in range(3): # Iteracion por las columnas
            if TTT[r][c] == 2:
                score += 1
            else: 
                score = 0
        if score == 3:
            mode = 'lose'
                
    # Verifica victorias por el usuario de manera vertical
    for c in range(len(TTT[0])): 
        for r in range(len(TTT)):
            if TTT[r][c] == 2:
                score += 1
            else:
                score = 0
        if score == 3:
            mode = 'lose'
    
    #Verifica la victoria de forma cruzada de izquierda a derecha               
    for i in range(len(TTT)):

        if TTT[i][i] == 2:
            score += 1
        else:
            score = 0
        
        if score == 3:
            mode = 'lose'
    
    #Verifica la victoria de forma cruzada de derecha a izquierda
    for r in range(len(TTT)):
        if columnsD >= 0:
            if TTT[r][columnsD] == 2:
                score += 1
                columnsD -= 1
            else:
                score = 0
        
        if score == 3:
            mode = 'lose'
    
    
    

def draw():
    background.draw()
    square1.draw()
    square2.draw()
    square3.draw()
    square4.draw()
    square5.draw()
    square6.draw()
    square7.draw()
    square8.draw()
    square9.draw()
    
def on_mouse_down(button, pos):
    global turn
    global mode
    
    if turn == 'user' and mode == 'neutro':
        if square1.collidepoint(pos) and 1 not in fullSpaces:
            square1.image = 'cross'
            fullSpaces.append(1) # cuadro 1
            TTT[0][0] = 1
            check_winner()
            turn = 'CPU'
        
        elif square2.collidepoint(pos) and 2 not in fullSpaces:
            square2.image = 'cross'
            fullSpaces.append(2) 
            TTT[0][1] = 1
            check_winner()
            turn = 'CPU'
        
        elif square3.collidepoint(pos) and 3 not in fullSpaces:
            square3.image = 'cross'
            fullSpaces.append(3)
            TTT[0][2] = 1
            check_winner()
            turn = 'CPU'
            
        elif square4.collidepoint(pos) and 4 not in fullSpaces:
            square4.image = 'cross'
            fullSpaces.append(4)
            TTT[1][0] = 1
            check_winner()
            turn = 'CPU'
        
        elif square5.collidepoint(pos) and 5 not in fullSpaces:
            square5.image = 'cross'
            fullSpaces.append(5)
            TTT[1][1] = 1
            check_winner()
            turn = 'CPU'

        elif square6.collidepoint(pos) and 6 not in fullSpaces:
            square6.image = 'cross'
            fullSpaces.append(6)
            TTT[1][2] = 1
            check_winner()
            turn = 'CPU'
            
        elif square7.collidepoint(pos) and 7 not in fullSpaces:
            square7.image = 'cross'
            fullSpaces.append(7)
            TTT[2][0] = 1
            check_winner()
            turn = 'CPU'
            
        elif square8.collidepoint(pos) and 8 not in fullSpaces:
            square8.image = 'cross'
            fullSpaces.append(8)
            TTT[2][1] = 1
            check_winner()
            turn = 'CPU'
            
        elif square9.collidepoint(pos) and 9 not in fullSpaces:
            square9.image = 'cross'
            fullSpaces.append(9)
            TTT[2][2] = 1
            check_winner()
            turn = 'CPU'
            
    
    if mode == 'win':
        square9.image = 'victory'
    
    elif mode == 'lose':
        square9.image = 'game_over'
        
    else:
        CPU_process()

    