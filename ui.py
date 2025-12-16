#tkinter GUI lel lybarary to make the app (tk)
import tkinter as tk
from logic import calculate

def start_app():
    root = tk.Tk()
    root.title("Calcaholic")
    root.geometry("350x580")   # el3ard wel tol elmonaseb lel calculator
    root.configure(bg="#0A1A2F") #color background code
    root.resizable(False, False) #disable resize

    #eldisplay
    display = tk.Entry(root, font=("Arial", 18), justify="right") #4ashet eldiplay + size + entry of worrdes from right
    display.pack(padx=10, pady=10, fill="x") #size around the display

    #the names
    label = tk.Label(
        root,
        text="Calcaholic Calculator",
        font=("Arial", 14),
        bg="#0A1A2F",
        fg="white"#color text
    )
    label.pack(padx=10, pady=5, fill="x") #eltarteb

    # Functions
    def press(value):
        display.insert(tk.END, value)

    def clear():
        display.delete(0, tk.END)

    def equals():
        try:
            result = calculate(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    # Buttons frame
    frame = tk.Frame(root, bg="#0A1A2F")
    frame.pack(expand=True, fill="both")

    # Layout of buttons
    buttons = [
        ("7",0,0), ("8",0,1), ("9",0,2), ("÷",0,3),
        ("4",1,0), ("5",1,1), ("6",1,2), ("✖",1,3),
        ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
        ("0",3,0), (".",3,1), ("=",3,2), ("+",3,3),
        ("C",4,0), ("%",4,1), ("cos",4,2), ("tan",4,3)
    ]

    for (text, r, c) in buttons:
        if text == "C":
            cmd = clear
        elif text == "=":
            cmd = equals
        else:
            cmd = lambda t=text: press(t)

        tk.Button(
            frame,
            text=text,
            font=("Arial", 14),
            width=5,
            height=2,
            command=cmd,
            bg="#1C2C3C",
            fg="white"
        ).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    # Make grid cells expand
    for i in range(5):
        frame.rowconfigure(i, weight=1)
    for j in range(4):
        frame.columnconfigure(j, weight=1)

    # Keyboard
    root.bind("<Return>", lambda e: equals())
    root.bind("<BackSpace>", lambda e: display.delete(len(display.get())-1))

    root.mainloop()

if __name__ == "__main__":
    start_app()