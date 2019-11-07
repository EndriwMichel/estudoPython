# Game Ping-Pong

from tkinter import * 
import random
import time

level_list = ['1', '2', '3', '4', '5']
level = 0
#setando uma variavel int em um input para pegar a resposta do usuario
while level not in level_list:
    level = input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n")
    if(level not in level_list):
        print('Selecione um level existente !')
        print('')
        level = 0
    else:
        length = 500/int(level) #tamanho da barra


root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

#canvas server para mostar elementos graficos
#cria tela principal aonde será exibido o game
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável
count = 0 #contador
lost = False #contador para game over

class Bola: #declarando classe bola e setando os parametros para construir a bolinha
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    #definindo tamanho da tela
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra: #declarando a classe barra para construila na tela
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()
        #setando os direcionais doteclado para mover a barra
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)
    #mover para esquerda
    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3
    #mover para direita
    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

#inicia as classes construidas e começa o jogo
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()

#função para contar pontuação
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))
#função ativada para quando der game over
def game_over():
    canvas.itemconfig(game, text="Game over!")

#setando as cores para barra e a bola
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

#cores das informações na tela como pontuação, fonte, etc.
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

#botão para iniciar o jogo
canvas.bind_all("<Button-1>", start_game)

root.mainloop()