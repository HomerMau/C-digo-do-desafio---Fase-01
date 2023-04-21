import turtle

# Configurações da tela
tela = turtle.Screen()
tela.bgcolor("white")

# Configurações dos bonecos
boneco1 = turtle.Turtle()
boneco1.color("blue")
boneco1.pensize(5)
boneco1.speed(0)

boneco2 = turtle.Turtle()
boneco2.color("red")
boneco2.pensize(5)
boneco2.speed(0)

# Desenho dos bonecos
def desenhar_boneco(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(20)
    turtle.backward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.backward(20)
    turtle.right(135)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)

desenhar_boneco(boneco1, -100, 0)
desenhar_boneco(boneco2, 100, 0)

# Movimentos dos bonecos
boneco1.penup()
boneco1.goto(-100, 0)
boneco1.pendown()

boneco2.penup()
boneco2.goto(100, 0)
boneco2.pendown()

for i in range(5):
    boneco1.right(90)
    boneco1.forward(20)
    boneco1.backward(20)
    boneco1.left(90)
    
    boneco2.left(90)
    boneco2.forward(20)
    boneco2.backward(20)
    boneco2.right(90)

# Mantém a tela aberta até que o usuário feche
turtle.done()
