import pgzrun
import random
import threading

semaforo = threading.Semaphore()
WIDTH = 800
HEIGHT = 600
# Criação dos Jogadores, Sistema operacional Linux e Windows
#
#    player1 = Jogador 1
#    player2 = Jogador 2
#
player1 = Actor('player1')
player1.x = WIDTH // 2 - 100
player1.y = HEIGHT - 40
player2 = Actor('player2')
player2.x = WIDTH // 2 + 100
player2.y = HEIGHT - 40
linux = Actor('linux')
windows = Actor('windows')

# configuração de jogo
is_game_over = False
game_timer = 60
score = 0
score2 = 0
prioridade1 = False
prioridade2 = False
roda_dado = True

def position_SO_Linux():
    '''
    Função para posicionar o sistema operacional Linux em um lugar aleatório na tela
    '''
    linux.x = random.randint(40, WIDTH - 40)
    linux.y = -100
def position_windows():
    '''
    Função para posicionar o sistema operacional Windows em um lugar aleatório na tela
    '''
    windows.x = random.randint(40, WIDTH - 40)
    windows.y = -100

def draw_score():
    '''
    Função para desenhar o score na tela
    '''


    screen.draw.text("Time: " + str(round(game_timer)), (HEIGHT//2, 20))

    screen.draw.text("JOGADOR1", (45, 20))
    screen.draw.text("score: " + str(score), (45, 40))


    screen.draw.text("JOGADOR2", (650, 20))
    screen.draw.text("score: " + str(score2), (650, 40))

    if is_game_over:
        if score > score2:
            display_text = "Game Over\nJOGADOR 1 VENCEU"
        if score2 > score:
            display_text = "Game Over\nJOGADOR 2 VENCEU"
        if score == score2:
            display_text = "Game Over\nEMPATE"
        position=((WIDTH//2)-100, (HEIGHT//2))
        screen.draw.text(display_text,position, fontsize=50, color=(255, 255, 255))

# MOVIMENTO DO JOGADOR 1
def move_player1():
    if keyboard.left:
        if player1.x -7 > 40 :
            player1.x -= 7
    elif keyboard.right:
        if player1.x +7 < 760:
            player1.x += 7
# MOVIMENTO DO JOGADOR 2
def move_player2():
    if keyboard.a:
        if player2.x -7 > 40:
            player2.x -= 7
    elif keyboard.d:
        if player2.x + 7 < 760:
            player2.x += 7


# Função criar a queda do Linux e do Windows
def linux_fall():
    if linux.y > HEIGHT + 40:
        position_SO_Linux()
    else:
        linux.y += 13
def windows_fall():
    if windows.y > HEIGHT + 40:
        position_windows()
    else:
        windows.y += 15

# Função para criar quem tem a prioridade
def dado_inicial():
    global prioridade1
    global prioridade2
    global roda_dado

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    if dado1 > dado2:
        prioridade1 = True
        prioridade2 = False
        roda_dado = False
    if dado2 > dado1:
        prioridade2 = True
        prioridade1 = False
        roda_dado = False
    if dado1 == dado2:
        dado_inicial()


# Thread para a coleta de itens dos jogadores
def thread1():
    global score
    global roda_dado
    global prioridade1
    global prioridade2
    global is_game_over

    while True:
        if player1.colliderect(player2) and prioridade1 and player1.colliderect(linux):
            semaforo.acquire()
            sounds.pop.play()
            score += 1
            position_SO_Linux()
            roda_dado = True
            semaforo.release()
        
        elif player1.colliderect(player2) and prioridade1 and player1.colliderect(windows):
            semaforo.acquire()
            sounds.pop.play()
            if score == 0:
                score = 0
            else:
                score -= 1
            if score <= score2:
                prioridade1 = False
                prioridade2 = True
            position_windows()
            semaforo.release()
        elif player1.colliderect(linux) and not player1.colliderect(player2):
            sounds.pop.play()
            score += 1
            position_SO_Linux()
        elif player1.colliderect(windows) and not player1.colliderect(player2):
            sounds.pop.play()
            if score == 0:
                score = 0
            else:
                score -= 1
                if score2 <= score:
                    prioridade1 = False
                    prioridade2 = True
            position_windows()
        if is_game_over:
            break

def thread2():
    global score2
    global roda_dado
    global prioridade1
    global prioridade2
    global is_game_over
    while True:
       

        if player2.colliderect(player1) and prioridade2 and player2.colliderect(linux):
            semaforo.acquire()
            sounds.pop.play()
            score2 += 1
            position_SO_Linux()
            roda_dado = True
            semaforo.release()

        elif player2.colliderect(player1) and prioridade2 and player2.colliderect(windows):
            semaforo.acquire()
            sounds.pop.play()
            if score2 == 0:
                score2 = 0
            else:
                score2 -= 1
            if score2 < score:
                prioridade1 = True
                prioridade2 = False
            position_windows()
            semaforo.release()
        
        elif player2.colliderect(linux) and not player2.colliderect(player1):
            sounds.pop.play()
            score2 += 1
            position_SO_Linux()
        elif player2.colliderect(windows) and not player2.colliderect(player1):
            sounds.pop.play()
            if score2 == 0:
                score2 = 0
            else:
                score2 -= 1
            position_windows()
        if is_game_over:
            break
            

def draw():
    global game_timer,isgame
    screen.clear()
    screen.blit('screenpc', (0, 0))
    draw_score()
    player1.draw()
    player2.draw()
    linux.draw()
    windows.draw()

def update():
    global game_timer, is_game_over
    


    if not is_game_over:
        move_player2()
        move_player1()
        linux_fall()
        windows_fall()
        if score == score2 and roda_dado == True:
            dado_inicial()

        if game_timer<=0:
            sounds.gameover.play()
            is_game_over = True
        else:
            game_timer -= 0.017


trabalhador1 = threading.Thread(target=thread1)
trabalhador2 = threading.Thread(target=thread2)
trabalhador1.start()
trabalhador2.start()


position_SO_Linux()
pgzrun.go()
