import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestAirbnbConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_instance(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("created", output)

    def test_show_instance(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("instance id missing", output)

    def test_destroy_instance(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("instance id missing", output)

    def test_all_instances(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_update_instance(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("instance id missing", output)

    def test_default_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("unknown_command")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** NO COMMAND FOR unknown_command **", output)

    def test_count_instances(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("0", output)

    def test_quit_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit):
                self.console.onecmd("quit")

    def test_EOF_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit):
                self.console.onecmd("EOF")


if __name__ == '__main__':
    unittest.main()
