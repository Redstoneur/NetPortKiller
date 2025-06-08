# Main entry point for the NetPortKiller application.
# This script initializes and launches the application's graphical interface.

from netportkiller.gui import NetPortKillerApp
import os


def main() -> None:
    """
    Main entry point for the NetPortKiller application.
    Initializes and launches the application's graphical interface.
    This function creates an instance of the graphical application and starts the main loop
    to display the user interface and handle user interactions.
    """
    icon_path = os.path.abspath("./assets/icon.ico")
    # Create an instance of the NetPortKiller graphical application with icons
    app = NetPortKillerApp(icon_path=icon_path)
    # Start the application's main loop.
    app.run()


if __name__ == "__main__":
    main()
