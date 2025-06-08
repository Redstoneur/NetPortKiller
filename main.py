# Point d'entrée principal de l'application NetPortKiller.
# Ce script initialise et lance l'interface graphique de l'application.

from netportkiller.gui import NetPortKillerApp

if __name__ == "__main__":
    # Crée une instance de l'application graphique NetPortKiller.
    app = NetPortKillerApp()
    # Démarre la boucle principale de l'application.
    app.run()
