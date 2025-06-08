import unittest
from typing import Any, List

from netportkiller import core


class TestCoreFunctions(unittest.TestCase):
    """
    Unit test class for the main functions of the netportkiller core module.
    """

    def test_get_used_ports(self) -> None:
        """
        Test the get_used_ports function from the core module.
        Checks that the returned list contains dictionaries with the expected keys:
        'port', 'protocol', 'pid', and 'process'.
        """
        ports: List[Any] = core.get_used_ports()
        self.assertIsInstance(ports, list)
        for port in ports:
            self.assertIn('port', port)
            self.assertIn('protocol', port)
            self.assertIn('pid', port)
            self.assertIn('process', port)

    def test_kill_process_invalid(self) -> None:
        """
        Test the kill_process function from the core module with an invalid PID (0).
        Checks that the function returns False, since PID 0 is generally not killable.
        """
        # PID 0 is generally not killable
        result: bool = core.kill_process(0)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
