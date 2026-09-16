# QuickTools

QuickTools is a simple and lightweight command-line utility written in Python.

It is designed to work on:

- Windows
- Linux
- macOS
- Android with Termux

QuickTools provides useful everyday tools in one program.


## Features

QuickTools currently includes:

1. File Tools
2. File Search
3. Password Generator
4. Internet Check
5. System Information
6. ZIP Tools
7. Converter
8. Notes
9. Settings
10. Ping / Server Check
11. Language Selection

Supported languages:

- Russian
- English

The selected language is saved automatically.


# Requirements

You need:

- Python 3.9 or newer
- A terminal or command prompt

QuickTools currently uses only Python's standard library.

**No third-party Python packages are required.**

You do not need to install additional Python libraries with `pip`.


# Installation

## Windows

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

During installation, make sure to enable:

```text
Add Python to PATH

2. Download QuickTools

Download the QuickTools repository from GitHub.

You can use:

Code → Download ZIP

Extract the ZIP archive.

The folder should look like:

QuickTools/
├── main.py
└── README.md

3. Open the terminal

Open Command Prompt or PowerShell.

Go to the QuickTools folder.

Example:

cd C:\Users\YourName\Desktop\QuickTools

4. Start QuickTools

Run:

python main.py

If python does not work, try:

py main.py



Linux

1. Check Python

Open your terminal and run:

python3 --version

You should see something similar to:

Python 3.x.x

If Python is not installed, install it using your distribution's package manager.

For Debian or Ubuntu:

sudo apt update
sudo apt install python3

2. Download QuickTools

You can download the ZIP archive from GitHub.

Or clone the repository using Git:

git clone https://github.com/YOUR_USERNAME/QuickTools.git

Enter the project directory:

cd QuickTools

3. Start QuickTools

Run:

python3 main.py



macOS

1. Check Python

Open Terminal and run:

python3 --version

If Python is not installed, download it from:

https://www.python.org/downloads/

2. Open the QuickTools directory

For example:

cd ~/Desktop/QuickTools

3. Start QuickTools

Run:

python3 main.py



Android / Termux

QuickTools can run on Android using Termux.

1. Install Termux

Download Termux from the official GitHub repository:

https://github.com/termux/termux-app

2. Update Termux

Open Termux and run:

pkg update
pkg upgrade

3. Install Python

Run:

pkg install python

Check that Python was installed:

python --version

You should see something similar to:

Python 3.x.x

4. Give Termux access to phone storage

Run:

termux-setup-storage

Android will ask for permission to access your files.

Allow the permission.

Your shared phone storage will normally become available at:

~/storage/shared

5. Open the QuickTools folder

For example, if QuickTools is located in your phone's main storage:

Internal storage/QuickTools

run:

cd ~/storage/shared/QuickTools

Check the files:

ls

You should see:

main.py
README.md

6. Start QuickTools

Run:

python main.py



First Start

When QuickTools starts, it will ask you to choose a language.

You can select:

1. Russian
2. English

After selecting the language, the main menu will appear.

Use the number shown next to each feature.

Example:

1. File Tools
2. File Search
3. Password Generator
4. Internet Check
5. System Information
6. ZIP Tools
7. Converter
8. Notes
9. Settings
10. Ping / Server Check
0. Exit

Enter the number of the feature you want to use and press Enter.



Language

QuickTools supports two languages:

Russian

English


You can change the language from the main menu.

The selected language is saved automatically.

You do not need to select the language again every time you start QuickTools.



File Tools

The File Tools section provides several operations for working with files and folders.

Available operations include:

File information

Rename files

Create folders

Delete files

Copy files

Move files

List folder contents


QuickTools will ask you for the required path.

Windows example:

C:\Users\YourName\Documents

Linux/macOS example:

/home/user/Documents

Android / Termux example:

/storage/emulated/0/Download



File Search

The File Search feature allows you to search for files inside a folder.

For example, you can search for:

photo

or:

main.py

QuickTools can also search through subfolders.



Password Generator

The Password Generator creates random passwords.

You can choose the desired password length.

Example:

Generated password:
X7!kP2@mQ9#z

Do not share your passwords with other people.



Internet Check

The Internet Check feature checks whether your device can connect to the internet.

This can be useful for basic network troubleshooting.

Example:

Checking internet connection...
Internet connection: OK



Ping / Server Check

The Ping feature allows you to check whether a host is reachable.

For example:

1.1.1.1

or:

example.com

The exact behavior of ping depends on your operating system and network.

You can also test ping directly in your terminal:

ping 1.1.1.1



System Information

The System Information section can display information about your device.

It may include:

Operating system

Machine information

Python version

CPU information

Memory information

Disk usage




ZIP Tools

The ZIP Tools section allows you to:

Create ZIP archives

Extract ZIP archives


QuickTools will ask you for the required files, folders, and destination paths.

Example:

/home/user/Documents/archive.zip

Android / Termux example:

~/storage/shared/Download/archive.zip



Converter

The Converter provides simple unit conversions.

Depending on the current version, available conversions may include:

Length

Weight

Temperature

Data size

Other supported units


Select the Converter from the main menu and follow the instructions displayed by QuickTools.



Notes

QuickTools includes a simple notes system.

You can create and manage notes directly from the program.

Notes are saved automatically.

They remain available after restarting QuickTools.



Settings

The Settings section contains QuickTools configuration options.

You can use it to manage application settings, including the language.



File Paths

Some QuickTools features ask you for a file or folder path.

You can enter:

An absolute path

A relative path

A path using the current directory


Windows example:

C:\Users\YourName\Documents

Linux/macOS example:

/home/user/Documents

Android / Termux example:

/storage/emulated/0/Download

You can also use:

~/storage/shared/Download

If QuickTools shows an example path, use the format appropriate for your operating system.



Configuration Files

QuickTools stores its configuration separately from the project files.

The configuration directory is:

~/.quicktools

The main configuration file is:

~/.quicktools/config.json

Notes are stored in:

~/.quicktools/notes.json

You normally do not need to edit these files manually.

Termux

The directory is normally located at:

/data/data/com.termux/files/home/.quicktools/



Dependencies

QuickTools currently uses only Python's standard library.

This means there are no external packages that need to be installed.

You do not need to run:

pip install -r requirements.txt

because the project does not currently require a requirements.txt file.

After installing Python, you can simply run:

python main.py

On Linux or macOS:

python3 main.py



Troubleshooting

Python is not recognized

If you see an error such as:

'python' is not recognized

try:

python3 main.py

On Windows, also try:

py main.py

If Python is not installed, download it from:

https://www.python.org/downloads/

On Windows, make sure that:

Add Python to PATH

is enabled during installation.



No module named ...

QuickTools does not require external Python packages.

If you see a missing-module error, make sure you are using a supported Python version and that main.py has not been modified incorrectly.



Permission denied

Some file operations require permission to access a file or folder.

Check that:

The path exists

You have permission to access it

The file is not being used by another program


On Android / Termux, run:

termux-setup-storage

and allow storage access.



Ping does not work

Some operating systems or networks may restrict the ping command.

You can test it directly in your terminal:

ping 1.1.1.1

If the command is unavailable or restricted, the Ping feature may not work correctly.



Updating QuickTools

When a new version is released, download the latest version from GitHub.

If you cloned the repository using Git, run:

git pull

Then start QuickTools again:

python main.py

On Linux or macOS:

python3 main.py



Project Structure

The project is intentionally simple.

QuickTools/
├── main.py
└── README.md

main.py

Contains the complete QuickTools application.

README.md

Contains installation, usage, and troubleshooting instructions.



GitHub Installation

After the project is published on GitHub, users will be able to install it with:

git clone https://github.com/YOUR_USERNAME/QuickTools.git
cd QuickTools
python main.py

On Linux or macOS:

git clone https://github.com/YOUR_USERNAME/QuickTools.git
cd QuickTools
python3 main.py

Replace:

YOUR_USERNAME

with the GitHub username that owns the repository.



Contributing

Contributions are welcome.

You can:

Report bugs

Suggest new features

Improve the documentation

Improve the interface

Submit code improvements


For large changes, it is recommended to discuss the idea before submitting it.



Version

Current version:

QuickTools v1.1.0


License

QuickTools is an open-source project.

A license can be added to the repository to define how other people can use, modify, and redistribute the project.



Author

QuickTools is an independent open-source project.

Made with Python.



Support

If you find a bug or have an idea for QuickTools, open an issue on GitHub.

Thank you for using QuickTools! 🚀