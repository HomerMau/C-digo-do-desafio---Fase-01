import turtle

# Configurações da janela
window = turtle.Screen()
window.bgcolor("white")
window.title("Luta de Bonecos")

# Criando o boneco 1
boneco1 = turtle.Turtle()
boneco1.speed(0)
boneco1.color("blue")
boneco1.pensize(5)

# Desenhando o corpo do boneco 1
boneco1.left(90)
boneco1.forward(100)
boneco1.right(90)
boneco1.forward(50)
boneco1.right(90)
boneco1.forward(70)
boneco1.right(90)
boneco1.forward(50)
boneco1.right(90)
boneco1.forward(30)

# Criando o boneco 2
boneco2 = turtle.Turtle()
boneco2.speed(0)
boneco2.color("red")
boneco2.pensize(5)

# Desenhando o corpo do boneco 2
boneco2.right(180)
boneco2.forward(100)
boneco2.left(90)
boneco2.forward(50)
boneco2.left(90)
boneco2.forward(70)
boneco2.left(90)
boneco2.forward(50)
boneco2.left(90)
boneco2.forward(30)

# Movimentos de luta
boneco1.right(90)
boneco1.forward(30)
boneco1.left(90)
boneco1.forward(30)
boneco2.left(90)
boneco2.forward(30)
boneco2.right(90)
boneco2.forward(30)
boneco1.right(90)
boneco1.forward(50)
boneco1.left(90)
boneco1.forward(20)
boneco2.left(90)
boneco2.forward(20)
boneco2.right(90)
boneco2.forward(50)

# Fim do desenho
turtle.done()
