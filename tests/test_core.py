import unittest

from netportkiller import core


class TestCoreFunctions(unittest.TestCase):
    """
    Classe de tests unitaires pour les fonctions principales du module core de netportkiller.
    """

    def test_get_used_ports(self):
        """
        Teste la fonction get_used_ports du module core.
        Vérifie que la liste retournée contient des dictionnaires avec les clés attendues :
        'port', 'protocol', 'pid', et 'process'.
        """
        ports = core.get_used_ports()
        self.assertIsInstance(ports, list)
        for port in ports:
            self.assertIn('port', port)
            self.assertIn('protocol', port)
            self.assertIn('pid', port)
            self.assertIn('process', port)

    def test_kill_process_invalid(self):
        """
        Teste la fonction kill_process du module core avec un PID invalide (0).
        Vérifie que la fonction retourne False, car le PID 0 n'est généralement pas tuable.
        """
        # PID 0 est généralement non tuable
        result = core.kill_process(0)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
