from tkinter import Tk, PhotoImage, Button, Label, messagebox, Menu, Menubutton, Toplevel


def configure_window():
    window.title("OXO Game")
    # Disabled resizing of the window.
    window.resizable(False, False)

    "Fixing geometry so that the window opens at the center"
    # Width and height of the window.
    width = 300
    height = 300

    # Screen width and height.
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Determines the change of coordinates.
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2 - 20)

    # Sets the screen position.
    window.geometry(f"{width}x{height}+{x}+{y}")


def create_buttons():
    global square, counter, oxo
    counter = 0
    oxo = [[None, None, None],
           [None, None, None],
           [None, None, None]]

    square[0] = Button(window, image=availableSquare, command=lambda: handle_button_click(0), width=100, height=100)
    square[0].place(x=0, y=0)

    square[1] = Button(window, image=availableSquare, command=lambda: handle_button_click(1), width=100, height=100)
    square[1].place(x=100, y=0)

    square[2] = Button(window, image=availableSquare, command=lambda: handle_button_click(2), width=100, height=100)
    square[2].place(x=200, y=0)

    square[3] = Button(window, image=availableSquare, command=lambda: handle_button_click(3), width=100, height=100)
    square[3].place(x=0, y=100)

    square[4] = Button(window, image=availableSquare, command=lambda: handle_button_click(4), width=100, height=100)
    square[4].place(x=100, y=100)

    square[5] = Button(window, image=availableSquare, command=lambda: handle_button_click(5), width=100, height=100)
    square[5].place(x=200, y=100)

    square[6] = Button(window, image=availableSquare, command=lambda: handle_button_click(6), width=100, height=100)
    square[6].place(x=0, y=200)

    square[7] = Button(window, image=availableSquare, command=lambda: handle_button_click(7), width=100, height=100)
    square[7].place(x=100, y=200)

    square[8] = Button(window, image=availableSquare, command=lambda: handle_button_click(8), width=100, height=100)
    square[8].place(x=200, y=200)


def handle_button_click(button_number):
    global counter
    if counter % 2 == 0:
        square[button_number].configure(image=player1, command=lambda: square_taken())
        player_number = 1
    else:
        square[button_number].configure(image=player2, command=lambda: square_taken())
        player_number = 2
    counter += 1

    update_move(button_number, player_number)


def square_taken():
    messagebox.showinfo(title="Square Taken", message="Sorry, This square is already taken")


def update_move(button_number, player_number):
    oxo[button_number // 3][button_number % 3] = player_number
    check_win()


def check_win():
    global winflag
    winflag = False

    won_game = [[oxo[0][0], oxo[1][1], oxo[2][2]],
                [oxo[0][2], oxo[1][1], oxo[2][0]],
                [oxo[0][0], oxo[0][1], oxo[0][2]],
                [oxo[1][0], oxo[1][1], oxo[1][2]],
                [oxo[2][0], oxo[2][1], oxo[2][2]],
                [oxo[0][0], oxo[1][0], oxo[2][0]],
                [oxo[0][1], oxo[1][1], oxo[2][1]],
                [oxo[0][2], oxo[1][2], oxo[2][2]]]

    for i in range(len(won_game)):

        if won_game[i] == [1, 1, 1]:
            win = Label(window, image=winner)
            win.place(x=150, y=150, anchor="center")
            window.after(2000, create_buttons)

            file = open("History.txt", "a")
            file.write("winner was Player 1\n")
            file.close()

            winflag = True

        if won_game[i] == [2, 2, 2]:
            win = Label(window, image=winner)
            win.place(x=150, y=150, anchor="center")
            window.after(2000, create_buttons)

            file = open("History.txt", "a")
            file.write("winner was Player 2\n")
            file.close()

            winflag = True

    if winflag:
        square[0].config(state="disabled")
        square[1].config(state="disabled")
        square[2].config(state="disabled")
        square[3].config(state="disabled")
        square[4].config(state="disabled")
        square[5].config(state="disabled")
        square[6].config(state="disabled")
        square[7].config(state="disabled")
        square[8].config(state="disabled")

    if counter == 9 and winflag == False:
        draw = Label(window, image=draaw)
        draw.place(x=150, y=150, anchor="center")
        window.after(2000, create_buttons)

        square[0].config(state="disabled")
        square[1].config(state="disabled")
        square[2].config(state="disabled")
        square[3].config(state="disabled")
        square[4].config(state="disabled")
        square[5].config(state="disabled")
        square[6].config(state="disabled")
        square[7].config(state="disabled")
        square[8].config(state="disabled")

        file = open("History.txt", "a")
        file.write("was a draw\n")
        file.close()


def win_history():
    global clear, top
    top = Toplevel()

    width = 400
    height = 600
    screen_Width = top.winfo_screenwidth()
    screen_Height = top.winfo_screenheight()

    x = screen_Width / 2 - width / 2
    y = screen_Height / 2 - height / 2

    top.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    top.title("Match History")
    label1 = Label(top, text="Match History:\n", font=40).pack(anchor="w", padx=20)

    file = open("History.txt", "r")
    lines = file.readlines()
    if len(lines) == 0:
        label2 = Label(top, text="Nothing to show here\n", ).pack(anchor="w", padx=20)
    else:
        for idx, val in enumerate(lines, start=1):
            Label(top, text=("Game " + str(idx) + " " + str(val))).pack(anchor="w", padx=20)
        clear = Button(top, text="Click to clear history", command=clear_history).pack()
    file.close()

    close = Button(top, text="Click to close", command=top.destroy).pack()


def clear_history():
    file = open("History.txt", "w")
    file.write("")
    file.close()

    top1 = Toplevel()

    width = 400
    height = 600
    screen_Width = top1.winfo_screenwidth()
    screen_Height = top1.winfo_screenheight()

    x = screen_Width / 2 - width / 2
    y = screen_Height / 2 - height / 2

    top1.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    top1.title("Match History")
    label1 = Label(top1, text="Match History:\n", font=40).pack(anchor="w", padx=20)
    label2 = Label(top1, text="Nothing to show here\n", ).pack(anchor="w", padx=20)
    top.destroy()

    close = Button(top1, text="Click to close", command=top1.destroy).pack()


def menu():
    menubar = Menu(window)
    window.config(menu=menubar)

    file_menu = Menu(menubar)
    menubar.add_cascade(label="File", menu=file_menu, underline=0)
    file_menu.add_command(label="Exit", command=window.destroy)

    history_menu = Menu(menubar)
    menubar.add_cascade(label="Match History", menu=history_menu, underline=0)
    history_menu.add_command(label="Match history", command=lambda: win_history())


window = Tk()
configure_window()
menu()

square = [None, None, None, None, None, None, None, None, None]

availableSquare = PhotoImage(file="myButton.png")
player1 = PhotoImage(file="myButtonP1.png")
player2 = PhotoImage(file="myButtonP2.png")
winner = PhotoImage(file="winner.png")
draaw = PhotoImage(file="Draw.png")

create_buttons()

window.mainloop()
