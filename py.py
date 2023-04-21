import turtle

# cria uma tartaruga
t = turtle.Turtle()

# define o tamanho da caneta
t.pensize(4)

# define a cor da caneta
t.pencolor("blue")

# desenha uma estrela
for i in range(5):
    t.forward(100)
    t.right(144)

# esconde a tartaruga
t.hideturtle()

# espera o usuário fechar a janela
turtle.done()
