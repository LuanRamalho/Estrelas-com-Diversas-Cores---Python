import turtle
import random

# Configuração da janela
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Estrelas Coloridas com Turtle")
tela.setup(width=800, height=600)

# Configuração do objeto turtle
desenhador = turtle.Turtle()
desenhador.speed(0)
desenhador.width(2)
desenhador.hideturtle()

# Função para desenhar uma estrela
def desenhar_estrela(tamanho, cor):
    desenhador.color(cor)
    desenhador.begin_fill()
    for _ in range(5):
        desenhador.forward(tamanho)
        desenhador.right(144)
    desenhador.end_fill()

# Função para gerar uma cor aleatória
def cor_aleatoria():
    return (random.random(), random.random(), random.random())

# Função principal para desenhar estrelas em posições aleatórias
def desenhar_estrelas(qtd_estrelas):
    for _ in range(qtd_estrelas):
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        tamanho = random.randint(10, 50)
        desenhador.penup()
        desenhador.goto(x, y)
        desenhador.pendown()
        desenhar_estrela(tamanho, cor_aleatoria())

# Desenha 20 estrelas coloridas
desenhar_estrelas(20)

# Mantém a janela aberta até o clique
tela.exitonclick()
