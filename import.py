import turtle

turtle.Screen().bgcolor("blue")
sc=turtle.Screen()
sc.setup(300,300)

turtle.title("Hello! You're using Turtle")
board=turtle.Turtle()

for i in range(3):
  board.forward(100)
  board.left(120)
  i=i+1


turtle.done()