import tkinter as tk
from tkinter import ttk, messagebox
from netportkiller.core import get_used_ports, kill_process

class NetPortKillerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NetPortKiller")
        self.build_ui()
        self.refresh_ports()

    def build_ui(self):
        self.tree = ttk.Treeview(self.root, columns=("Port", "Protocol", "PID", "Process"), show='headings', selectmode="extended")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Refresh", command=self.refresh_ports).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Kill Selected", command=self.kill_selected).pack(side=tk.LEFT, padx=5)

    def refresh_ports(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for entry in get_used_ports():
            self.tree.insert("", "end", values=(
                entry["port"],
                entry["protocol"],
                entry["pid"],
                entry["process"]
            ))

    def kill_selected(self):
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
