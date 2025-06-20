"""
Interface graphique principale pour NetPortKiller.
Affiche les ports réseau utilisés et permet de tuer les processus associés.
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox

from netportkiller.core import get_used_ports, kill_process


class NetPortKillerApp(tk.Tk):
    """
    Main graphical application for NetPortKiller.

    This application displays the network ports in use on the machine,
    allows refreshing the list, and killing processes associated with selected ports.
    """

    def __init__(self, icon_path=None) -> None:
        """
        Initialize the main window, build the user interface,
        and display the list of used ports.

        :param icon_path: Path to the application icon file.
        """
        super().__init__()
        self.title("NetPortKiller")
        self.geometry("600x400")
        self.icon_path: str | None = os.path.abspath(icon_path) if icon_path else None
        self.set_icon()
        self.build_ui()
        self.refresh_ports()

    def set_icon(self) -> None:
        """
        Set the application icon if the icon path is valid.
        This method is called during initialization to set the window icon.
        """
        if self.icon_path and os.path.exists(self.icon_path):
            try:
                self.iconbitmap(self.icon_path)
            except tk.TclError:
                pass

    def build_ui(self) -> None:
        """
        Build the user interface:
        - A search bar to filter all columns.
        - A table (Treeview) listing ports, protocols, PID, and process.
        - Two buttons: 'Refresh' to update the list, 'Kill Selected' to terminate selected
          processes.
        """
        # Search bar
        search_frame = tk.Frame(self)
        search_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.on_search)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

        # Treeview
        self.tree = ttk.Treeview(self, columns=("Port", "Protocol", "PID", "Process"),
                                 show='headings', selectmode="extended")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Refresh", command=self.refresh_ports).pack(side=tk.LEFT, padx=5)
        tk.Button(
            btn_frame,
            text="Kill Selected",
            command=self.kill_selected
        ).pack(side=tk.LEFT, padx=5)

    def refresh_ports(self) -> None:
        """
        Refresh the list of ports displayed in the table by calling `get_used_ports`.
        Clears old entries before adding new ones.
        """
        self.all_ports = list(get_used_ports())  # Store all entries for filtering
        self.apply_filter()

    def apply_filter(self):
        """
        Filter the displayed ports based on the search bar.
        """
        search = self.search_var.get().lower() if hasattr(self, 'search_var') else ""
        for i in self.tree.get_children():
            self.tree.delete(i)
        for entry in getattr(self, 'all_ports', []):
            values = (
                str(entry["port"]),
                str(entry["protocol"].value),
                str(entry["pid"]),
                str(entry["process"])
            )
            if not search or any(search in str(v).lower() for v in values):
                self.tree.insert("", "end", values=values)

    def on_search(self, *_) -> None:
        """
        Callback for search bar changes.
        """
        self.apply_filter()

    def kill_selected(self) -> None:
        """
        Attempt to kill the processes associated with the ports selected in the table.
        Display a dialog indicating the number of processes terminated.
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
        Start the main Tkinter application loop.
        """
        self.mainloop()


if __name__ == "__main__":
    app = NetPortKillerApp()
    app.run()
