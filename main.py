from netportkiller.gui import NetPortKillerApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = NetPortKillerApp(root)
    root.geometry("600x400")
    root.mainloop()
