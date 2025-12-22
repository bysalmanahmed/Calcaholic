import tkinter as tk
from logic import calculate, get_history_data

def start_app():
    root = tk.Tk()
    root.title("Calcaholic")
    root.geometry("350x620") # kbert elwindow shwaya 3ashan elH button
    root.configure(bg="#0A1A2F") 
    root.resizable(False, False) 

    # eldisplay
    display = tk.Entry(root, font=("Arial", 18), justify="right") 
    display.pack(padx=10, pady=10, fill="x") 

    # ellabel
    label = tk.Label(
        root,
        text="Calcaholic Calculator",
        font=("Arial", 14),
        bg="#0A1A2F",
        fg="white"
    )
    label.pack(padx=10, pady=5, fill="x") 

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

    # window elhistory elly btzhr lama ndos "H"
    def open_history():
        h_win = tk.Toplevel(root)
        h_win.title("History")
        h_win.geometry("280x400")
        h_win.configure(bg="#1C2C3C")
        
        data = get_history_data()
        if not data:
            tk.Label(h_win, text="No history yet!", bg="#1C2C3C", fg="white").pack(pady=20)
        else:
            for item in data:
                txt = f"{item['op']} = {item['res']}"
                tk.Label(h_win, text=txt, bg="#1C2C3C", fg="white", font=("Arial", 10)).pack(pady=5, padx=10)

    # Buttons frame
    frame = tk.Frame(root, bg="#0A1A2F")
    frame.pack(expand=True, fill="both")

    # Layout elbuttons
    buttons = [
        ("7",0,0), ("8",0,1), ("9",0,2), ("÷",0,3),
        ("4",1,0), ("5",1,1), ("6",1,2), ("✖",1,3),
        ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
        ("0",3,0), (".",3,1), ("=",3,2), ("+",3,3),
        ("C",4,0), ("%",4,1), ("cos",4,2), ("tan",4,3),
        ("H",5,0) # zorar el-history el-gdyd
    ]

    for (text, r, c) in buttons:
        if text == "C":
            cmd = clear
        elif text == "=":
            cmd = equals
        elif text == "H":
            cmd = open_history
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

    # grid configuration
    for i in range(6): 
        frame.rowconfigure(i, weight=1)
    for j in range(4):
        frame.columnconfigure(j, weight=1)

    # Keyboard binding
    root.bind("<Return>", lambda e: equals())
    root.bind("<BackSpace>", lambda e: display.delete(len(display.get())-1))

    root.mainloop()

if __name__ == "__main__":
    start_app()