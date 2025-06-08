# Main entry point for the NetPortKiller application.
# This script initializes and launches the application's graphical interface.

from netportkiller.gui import NetPortKillerApp


def main() -> None:
    """
    Main entry point for the NetPortKiller application.
    Initializes and launches the application's graphical interface.
    This function creates an instance of the graphical application and starts the main loop
    to display the user interface and handle user interactions.
    """
    # Create an instance of the NetPortKiller graphical application.
    app = NetPortKillerApp()
    # Start the application's main loop.
    app.run()


if __name__ == "__main__":
    main()
