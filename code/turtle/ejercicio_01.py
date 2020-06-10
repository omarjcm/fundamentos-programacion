import turtle as tt

# Se configura la ventana
tt.setup(500, 500)
wn = tt.Screen()
wn.bgcolor("lightblue")
wn.title("La tortuguita")

# Se configura la tortuga
tess = tt.Turtle()
tess.shape("turtle")
tess.color("black")

wn.exitonclick()