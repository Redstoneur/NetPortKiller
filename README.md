# NetPortKiller

---

![License](https://img.shields.io/github/license/Redstoneur/NetPortKiller)
![Top Language](https://img.shields.io/github/languages/top/Redstoneur/NetPortKiller)
![Python Version](https://img.shields.io/badge/python-3.13.0-blue)
![Size](https://img.shields.io/github/repo-size/Redstoneur/NetPortKiller)
![Contributors](https://img.shields.io/github/contributors/Redstoneur/NetPortKiller)
![Last Commit](https://img.shields.io/github/last-commit/Redstoneur/NetPortKiller)
![Issues](https://img.shields.io/github/issues/Redstoneur/NetPortKiller)
![Pull Requests](https://img.shields.io/github/issues-pr/Redstoneur/NetPortKiller)

---

![Forks](https://img.shields.io/github/forks/Redstoneur/NetPortKiller)
![Stars](https://img.shields.io/github/stars/Redstoneur/NetPortKiller)
![Watchers](https://img.shields.io/github/watchers/Redstoneur/NetPortKiller)

---

![Latest Release](https://img.shields.io/github/v/release/Redstoneur/NetPortKiller)
![Release Date](https://img.shields.io/github/release-date/Redstoneur/NetPortKiller)
[![Build Status](https://github.com/Redstoneur/NetPortKiller/actions/workflows/build.yml/badge.svg)](https://github.com/Redstoneur/NetPortKiller/actions/workflows/build.yml)

---

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

