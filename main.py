"""
Point d'entrée principal pour l'application NetPortKiller.
Ce script initialise et lance l'interface graphique de l'application.
"""

import os
import sys

from netportkiller.gui import NetPortKillerApp

if hasattr(sys, "_MEIPASS") and getattr(sys, "_MEIPASS"):
    # Exécution depuis l'exécutable PyInstaller
    icon_path = os.path.join(getattr(sys, "_MEIPASS"), "assets", "icon.ico")
else:
    # Exécution depuis le code source
    icon_path = os.path.abspath("./assets/icon.ico")


def main() -> None:
    """
    Main entry point for the NetPortKiller application.
    Initializes and launches the application's graphical interface.
    This function creates an instance of the graphical application and starts the main loop
    to display the user interface and handle user interactions.
    """
    # Create an instance of the NetPortKiller graphical application with icons
    app = NetPortKillerApp(icon_path=icon_path)
    # Start the application's main loop.
    app.run()


if __name__ == "__main__":
    main()
