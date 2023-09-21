import turtle 
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. State Game ")
image = r"day25\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pd.read_csv(r"day25\50_states.csv")
all_states = state_data["state"].to_list()
guessed_state= []
while len(guessed_state) < 50:
    answer = screen.textinput(title=f" {len(guessed_state)}/50 Guess the State name ? " , prompt= "Enter The State name :  ").title()
    if answer == "Exit":
        missing_state=[state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        x = pd.DataFrame(missing_state)
        x.to_csv("learning.csv")
        break
    if answer in all_states:
        guessed_state.append(answer)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        cordinate = state_data[state_data.state == answer]
        t.goto(int(cordinate.x), int(cordinate.y))
        t.write(answer)
screen.exitonclick()



# to get coordinate in turtle library screen
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreen(get_mouse_click_coor)

# turtle.mainloop()
