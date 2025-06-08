import tkinter as tk
from tkinter import ttk, messagebox

from netportkiller.core import get_used_ports, kill_process


class NetPortKillerApp(tk.Tk):
    """
    Application graphique principale pour NetPortKiller.

    Cette application permet d'afficher les ports réseau utilisés sur la machine,
    d'actualiser la liste et de tuer les processus associés à des ports sélectionnés.
    """

    def __init__(self) -> None:
        """
        Initialise la fenêtre principale, construit l'interface utilisateur
        et affiche la liste des ports utilisés.
        """
        super().__init__()
        self.title("NetPortKiller")
        self.geometry("600x400")
        self.build_ui()
        self.refresh_ports()

    def build_ui(self) -> None:
        """
        Construit l'interface utilisateur :
        - Un tableau (Treeview) listant les ports, protocoles, PID et processus.
        - Deux boutons : 'Refresh' pour actualiser la liste, 'Kill Selected' pour tuer les processus sélectionnés.
        """
        self.tree = ttk.Treeview(self, columns=("Port", "Protocol", "PID", "Process"),
                                 show='headings', selectmode="extended")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Refresh", command=self.refresh_ports).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Kill Selected", command=self.kill_selected).pack(side=tk.LEFT,
                                                                                    padx=5)

    def refresh_ports(self) -> None:
        """
        Rafraîchit la liste des ports affichés dans le tableau en appelant `get_used_ports`.
        Efface les anciennes entrées avant d'ajouter les nouvelles.
        """
        for i in self.tree.get_children():
            self.tree.delete(i)

        for entry in get_used_ports():
            self.tree.insert("", "end", values=(
                entry["port"],
                entry["protocol"],
                entry["pid"],
                entry["process"]
            ))

    def kill_selected(self) -> None:
        """
        Tente de tuer les processus associés aux ports sélectionnés dans le tableau.
        Affiche une boîte de dialogue indiquant le nombre de processus terminés.
        """
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select one or more ports.")
            return

        killed = 0
        for item in selected:
            pid = int(self.tree.item(item)["values"][2])
            if kill_process(pid):
                killed += 1

        messagebox.showinfo("Done", f"{killed} process(es) terminated.")
        self.refresh_ports()

    def run(self) -> None:
        """
        Lance la boucle principale de l'application Tkinter.
        """
        self.mainloop()


if __name__ == "__main__":
    app = NetPortKillerApp()
    app.run()
