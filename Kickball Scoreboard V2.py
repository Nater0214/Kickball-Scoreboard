from tkinter import *

display_window = Tk()
display_window.title("Display")
display_window.geometry("250x100")

main_frame = Frame(display_window)
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
display_window.columnconfigure(0, weight=1)
display_window.rowconfigure(0, weight=1)
display_window.columnconfigure(0, weight=1)
display_window.rowconfigure(0, weight=1)

scoreboard_display_elements = {
    "team1": Label(main_frame, text="Aj:", font=("Comfotaa Regular", 20), width=5, anchor="e", justify=LEFT).grid(column=1, row=1),
    "team2": Label(main_frame, text="Sky:", font=("Comfotaa Regular", 20), width=5, anchor="e").grid(column=1, row=2),
    "score1": Label(main_frame, text="5", font=("Comfotaa Regular", 20), width=2, anchor="w").grid(column=2, row=1),
    "score2": Label(main_frame, text="3", font=("Comfotaa Regular", 20), width=2, anchor="w").grid(column=2, row=2)
    
}

display_window.mainloop()