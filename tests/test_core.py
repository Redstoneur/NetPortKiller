import unittest
from netportkiller import core


class TestCoreFunctions(unittest.TestCase):
    def test_get_used_ports(self):
        ports = core.get_used_ports()
        self.assertIsInstance(ports, list)
        for port in ports:
            self.assertIn('port', port)
            self.assertIn('protocol', port)
            self.assertIn('pid', port)
            self.assertIn('process', port)

    def test_kill_process_invalid(self):
        # PID 0 est généralement non tuable
        result = core.kill_process(0)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
