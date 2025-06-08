# NetPortKiller

NetPortKiller is a simple graphical tool for listing and terminating processes that are using network ports on your
machine. It is useful for developers and system administrators who need to quickly identify and free up occupied TCP/UDP
ports.

## Features

- List all currently used TCP and UDP ports.
- Display process name and PID for each port.
- Search/filter ports by any column.
- Terminate (kill) processes directly from the interface.
- Cross-platform (Windows, Linux, macOS).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Redstoneur/NetPortKiller.git
   cd NetPortKiller
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with:

```bash
python main.py
```

The graphical interface will open, displaying all listening ports. Use the search bar to filter, and select one or more
entries to terminate their associated processes.

## Packaging as Executable

To build a standalone executable (requires [PyInstaller](https://pyinstaller.org/)):

```bash
pyinstaller --onefile --icon=assets/icon.ico --noconsole --name NetPortKiller --add-data "assets/icon.ico;assets" main.py
```

## Running Tests

To run unit tests:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

