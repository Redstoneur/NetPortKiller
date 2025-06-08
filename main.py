# Point d'entrée principal de l'application NetPortKiller.
# Ce script initialise et lance l'interface graphique de l'application.

from netportkiller.gui import NetPortKillerApp


def main() -> None:
    """
    Point d'entrée principal de l'application NetPortKiller.
    Initialise et lance l'interface graphique de l'application.
    Cette fonction crée une instance de l'application graphique et démarre la boucle principale
    pour afficher l'interface utilisateur et gérer les interactions de l'utilisateur.
    """
    # Crée une instance de l'application graphique NetPortKiller.
    app = NetPortKillerApp()
    # Démarre la boucle principale de l'application.
    app.run()


if __name__ == "__main__":
    main()
