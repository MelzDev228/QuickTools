import os
import sys
import time
import json
import random
import string
import shutil
import socket
import platform
import subprocess
import urllib.request
import zipfile
from pathlib import Path
from datetime import datetime


# ============================================================
# QUICKTOOLS
# Version 1.1.0
# One-file utility program
# Works on Windows, Linux, macOS and Termux
# ============================================================


APP_NAME = "QuickTools"
VERSION = "1.1.0"

CONFIG_DIR = Path.home() / ".quicktools"
CONFIG_FILE = CONFIG_DIR / "config.json"
NOTES_FILE = CONFIG_DIR / "notes.json"

LANGUAGE = None


# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {
    "ru": {
        "subtitle": "Полезные инструменты в одном месте",
        "choose_language": "Выберите язык",
        "russian": "Русский",
        "english": "English",
        "invalid": "Неверный выбор.",
        "press_enter": "Нажмите Enter, чтобы продолжить...",
        "loading": "Загрузка",
        "welcome": "Добро пожаловать в QuickTools!",
        "main_menu": "Главное меню",
        "select": "Выберите действие",

        "files": "Работа с файлами",
        "search": "Поиск файлов",
        "password": "Генератор паролей",
        "internet": "Проверка интернета",
        "system": "Информация о системе",
        "zip": "Работа с ZIP",
        "converter": "Конвертер",
        "notes": "Заметки",
        "settings": "Настройки",
        "ping": "Ping / проверка сервера",
        "exit": "Выход",

        "back": "Назад",

        # Files
        "file_tools": "Файловые инструменты",
        "file_info": "Информация о файле",
        "rename": "Переименовать",
        "create_folder": "Создать папку",
        "delete_file": "Удалить файл",
        "copy_file": "Копировать файл",
        "move_file": "Переместить файл",
        "list_folder": "Показать содержимое папки",

        "path": "Путь",
        "source": "Источник",
        "destination": "Назначение",
        "file": "Файл",
        "folder": "Папка",
        "new_name": "Новое имя",
        "empty_path": "Путь не указан.",
        "not_found": "Файл или папка не найдены.",
        "folder_not_found": "Папка не найдена.",
        "success": "Готово!",
        "deleted": "Файл удалён.",
        "copied": "Файл скопирован.",
        "moved": "Файл перемещён.",
        "folder_created": "Папка создана.",
        "renamed": "Файл переименован.",
        "operation_error": "Не удалось выполнить операцию",

        # Search
        "search_files": "Поиск файлов",
        "search_folder": "Папка для поиска",
        "search_query": "Имя или часть имени",
        "searching": "Идёт поиск",
        "nothing_found": "Ничего не найдено.",
        "found": "Найдено",

        # Passwords
        "password_generator": "Генератор паролей",
        "password_length": "Длина пароля",
        "upper": "Заглавные буквы",
        "lower": "Строчные буквы",
        "numbers": "Цифры",
        "symbols": "Специальные символы",
        "yes_no": "[y/n]",
        "generated": "Сгенерированный пароль",

        # Internet
        "internet_check": "Проверка интернета",
        "checking": "Проверяем подключение",
        "internet_available": "Интернет доступен.",
        "internet_unavailable": "Не удалось подключиться к интернету.",
        "ping_menu": "Ping / проверка сервера",
        "host": "Адрес сайта или IP",

        # System
        "system_info": "Информация о системе",
        "os": "Операционная система",
        "computer": "Компьютер",
        "hostname": "Имя устройства",
        "architecture": "Архитектура",
        "python": "Python",
        "processor": "Процессор",
        "cores": "Ядер CPU",
        "ram": "Оперативная память",
        "disk": "Свободное место",
        "current_dir": "Текущая папка",

        # ZIP
        "zip_tools": "ZIP инструменты",
        "create_zip": "Создать ZIP",
        "extract_zip": "Распаковать ZIP",
        "archive_source": "Что добавить в архив",
        "archive_output": "Куда сохранить архив",
        "zip_file": "ZIP файл",
        "extract_to": "Куда распаковать",
        "archive_created": "Архив создан.",
        "archive_extracted": "Архив распакован.",

        # Converter
        "converter": "Конвертер",
        "bytes_mb": "Байты → MB",
        "mb_bytes": "MB → байты",
        "gb_mb": "GB → MB",
        "mb_gb": "MB → GB",
        "c_f": "Цельсий → Фаренгейт",
        "f_c": "Фаренгейт → Цельсий",
        "value": "Значение",

        # Notes
        "notes": "Заметки",
        "create_note": "Создать заметку",
        "view_notes": "Показать заметки",
        "delete_note": "Удалить заметку",
        "no_notes": "Заметок пока нет.",
        "note_title": "Название",
        "note_text": "Текст",
        "note_number": "Номер заметки",
        "note_created": "Заметка создана.",
        "note_deleted": "Заметка удалена.",

        # Settings
        "settings": "Настройки",
        "change_language": "Сменить язык",
        "reset_language": "Сбросить сохранённый язык",
        "version": "Версия",

        # Ending
        "goodbye": "До новой встречи...",
        "saved": "Настройки сохранены.",

        # Examples
        "example": "Пример",
        "current": "Текущая папка",
        "press_enter_default": "Enter = использовать значение по умолчанию",

        # Confirmations
        "confirm_delete": "Удалить этот файл? [y/n]",
        "confirm": "Подтверждение",
    },

    "en": {
        "subtitle": "Useful tools in one place",
        "choose_language": "Choose language",
        "russian": "Русский",
        "english": "English",
        "invalid": "Invalid choice.",
        "press_enter": "Press Enter to continue...",
        "loading": "Loading",
        "welcome": "Welcome to QuickTools!",
        "main_menu": "Main menu",
        "select": "Select an option",

        "files": "File tools",
        "search": "File search",
        "password": "Password generator",
        "internet": "Internet check",
        "system": "System information",
        "zip": "ZIP tools",
        "converter": "Converter",
        "notes": "Notes",
        "settings": "Settings",
        "ping": "Ping / server check",
        "exit": "Exit",

        "back": "Back",

        "file_tools": "File tools",
        "file_info": "File information",
        "rename": "Rename",
        "create_folder": "Create folder",
        "delete_file": "Delete file",
        "copy_file": "Copy file",
        "move_file": "Move file",
        "list_folder": "List folder contents",

        "path": "Path",
        "source": "Source",
        "destination": "Destination",
        "file": "File",
        "folder": "Folder",
        "new_name": "New name",
        "empty_path": "No path specified.",
        "not_found": "File or folder not found.",
        "folder_not_found": "Folder not found.",
        "success": "Done!",
        "deleted": "File deleted.",
        "copied": "File copied.",
        "moved": "File moved.",
        "folder_created": "Folder created.",
        "renamed": "File renamed.",
        "operation_error": "Operation failed",

        "search_files": "File search",
        "search_folder": "Folder to search",
        "search_query": "File name or part of name",
        "searching": "Searching",
        "nothing_found": "Nothing found.",
        "found": "Found",

        "password_generator": "Password generator",
        "password_length": "Password length",
        "upper": "Uppercase letters",
        "lower": "Lowercase letters",
        "numbers": "Numbers",
        "symbols": "Special characters",
        "yes_no": "[y/n]",
        "generated": "Generated password",

        "internet_check": "Internet check",
        "checking": "Checking connection",
        "internet_available": "Internet is available.",
        "internet_unavailable": "Could not connect to the internet.",
        "ping_menu": "Ping / server check",
        "host": "Website or IP address",

        "system_info": "System information",
        "os": "Operating system",
        "computer": "Computer",
        "hostname": "Hostname",
        "architecture": "Architecture",
        "python": "Python",
        "processor": "Processor",
        "cores": "CPU cores",
        "ram": "RAM",
        "disk": "Free disk space",
        "current_dir": "Current directory",

        "zip_tools": "ZIP tools",
        "create_zip": "Create ZIP",
        "extract_zip": "Extract ZIP",
        "archive_source": "What to add to archive",
        "archive_output": "Where to save archive",
        "zip_file": "ZIP file",
        "extract_to": "Where to extract",
        "archive_created": "Archive created.",
        "archive_extracted": "Archive extracted.",

        "converter": "Converter",
        "bytes_mb": "Bytes → MB",
        "mb_bytes": "MB → bytes",
        "gb_mb": "GB → MB",
        "mb_gb": "MB → GB",
        "c_f": "Celsius → Fahrenheit",
        "f_c": "Fahrenheit → Celsius",
        "value": "Value",

        "notes": "Notes",
        "create_note": "Create note",
        "view_notes": "View notes",
        "delete_note": "Delete note",
        "no_notes": "No notes yet.",
        "note_title": "Title",
        "note_text": "Text",
        "note_number": "Note number",
        "note_created": "Note created.",
        "note_deleted": "Note deleted.",

        "settings": "Settings",
        "change_language": "Change language",
        "reset_language": "Reset saved language",
        "version": "Version",

        "goodbye": "See you next time...",
        "saved": "Settings saved.",

        "example": "Example",
        "current": "Current folder",
        "press_enter_default": "Enter = use default value",

        "confirm_delete": "Delete this file? [y/n]",
        "confirm": "Confirmation",
    }
}


def t(key):
    return TEXT.get(LANGUAGE, TEXT["en"]).get(key, key)


# ============================================================
# PATHS FOR TERMUX
# ============================================================

def detect_shared_storage():
    """
    Detects Android/Termux shared storage if available.
    """
    possible_paths = [
        Path.home() / "storage" / "shared",
        Path("/storage/emulated/0"),
    ]

    for path in possible_paths:
        if path.exists() and path.is_dir():
            return path

    return Path.home()


SHARED_STORAGE = detect_shared_storage()


# ============================================================
# BASIC FUNCTIONS
# ============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def sleep(seconds):
    time.sleep(seconds)


def pause():
    input(f"\n{DIM}{t('press_enter')}{RESET}")


def strip_ansi(text):
    codes = [
        RESET,
        BOLD,
        DIM,
        CYAN,
        BLUE,
        GREEN,
        YELLOW,
        RED,
        MAGENTA,
        WHITE,
    ]

    for code in codes:
        text = text.replace(code, "")

    return text


def loading(seconds=1.0, message=None):
    if message is None:
        message = t("loading")

    frames = [
        "   ",
        ".  ",
        ".. ",
        "...",
    ]

    end_time = time.time() + seconds

    while time.time() < end_time:
        for frame in frames:
            if time.time() >= end_time:
                break

            print(
                f"\r{CYAN}{message}{frame}{RESET}",
                end="",
                flush=True
            )
            time.sleep(0.12)

    print("\r" + " " * 50 + "\r", end="")


def progress_bar(duration=1.2, width=30):
    start = time.time()

    while True:
        elapsed = time.time() - start
        progress = min(elapsed / duration, 1)

        filled = int(width * progress)

        bar = "█" * filled + "░" * (width - filled)
        percent = int(progress * 100)

        print(
            f"\r{CYAN}[{bar}] {percent:>3}%{RESET}",
            end="",
            flush=True
        )

        if progress >= 1:
            break

        time.sleep(0.035)

    print()


def type_text(text, speed=0.018):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)

    print()


def header(title):
    clear_screen()

    width = max(58, len(strip_ansi(title)) + 12)

    print()
    print(f"{CYAN}{BOLD}╔{'═' * width}╗{RESET}")
    print(
        f"{CYAN}{BOLD}║{RESET}"
        f"{WHITE}{BOLD}{title.center(width)}{RESET}"
        f"{CYAN}{BOLD}║{RESET}"
    )
    print(f"{CYAN}{BOLD}╚{'═' * width}╝{RESET}")
    print()


def box(lines, width=58):
    print(f"{CYAN}╭{'─' * width}╮{RESET}")

    for line in lines:
        visible = len(strip_ansi(line))
        content_width = width - 2

        if visible > content_width:
            clean_line = strip_ansi(line)
            line = clean_line[:content_width]

        visible = len(strip_ansi(line))
        spaces = max(0, content_width - visible)

        print(
            f"{CYAN}│ {RESET}"
            f"{line}"
            f"{' ' * spaces}"
            f"{CYAN} │{RESET}"
        )

    print(f"{CYAN}╰{'─' * width}╯{RESET}")


# ============================================================
# CONFIG
# ============================================================

def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config():
    global LANGUAGE

    ensure_config_dir()

    if not CONFIG_FILE.exists():
        LANGUAGE = None
        return

    try:
        data = json.loads(
            CONFIG_FILE.read_text(encoding="utf-8")
        )

        saved_language = data.get("language")

        if saved_language in ("ru", "en"):
            LANGUAGE = saved_language
        else:
            LANGUAGE = None

    except Exception:
        LANGUAGE = None


def save_config():
    ensure_config_dir()

    data = {
        "language": LANGUAGE,
        "version": VERSION,
    }

    CONFIG_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


# ============================================================
# LANGUAGE
# ============================================================

def choose_language(first_start=True):
    global LANGUAGE

    header(APP_NAME)

    print(f"{BOLD}{t('choose_language')}{RESET}\n")

    print(f"{CYAN}[1]{RESET} {t('russian')}")
    print(f"{CYAN}[2]{RESET} {t('english')}")
    print()

    while True:
        choice = input("> ").strip()

        if choice == "1":
            LANGUAGE = "ru"
            break

        if choice == "2":
            LANGUAGE = "en"
            break

        print(f"{RED}{t('invalid')}{RESET}")

    save_config()

    print()
    progress_bar(0.8, 28)

    if first_start:
        sleep(0.3)


# ============================================================
# LOGO
# ============================================================

def show_logo():
    print(f"{CYAN}{BOLD}")
    print(" ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗")
    print("██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝")
    print("██║   ██║██║   ██║██║██║     █████╔╝ ")
    print("██║▄▄ ██║██║   ██║██║██║     ██╔═██╗ ")
    print("╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗")
    print(" ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝")
    print(f"{RESET}")

    print(f"{DIM}{t('subtitle')}{RESET}")
    print(f"{DIM}v{VERSION}{RESET}")
    print()


def startup_animation():
    clear_screen()

    print()

    show_logo()

    type_text(
        f"{GREEN}{t('welcome')}{RESET}",
        0.025
    )

    print()
    progress_bar(1.0, 32)

    sleep(0.3)


# ============================================================
# INPUT HELPERS
# ============================================================

def show_path_example(label, example, default=None):
    print()
    print(f"{DIM}{label}{RESET}")

    if example:
        print(f"{DIM}{t('example')}: {example}{RESET}")

    if default is not None:
        print(
            f"{DIM}{t('press_enter_default')}: "
            f"{default}{RESET}"
        )


def ask_path(label, example=None, default=None):
    show_path_example(label, example, default)

    value = input(f"{BOLD}> {RESET}").strip().strip('"')

    if not value and default is not None:
        return Path(default)

    if not value:
        return None

    return Path(value).expanduser()


def ask_yes_no(question):
    while True:
        answer = input(
            f"{question} "
        ).strip().lower()

        if answer in (
            "y",
            "yes",
            "д",
            "да"
        ):
            return True

        if answer in (
            "n",
            "no",
            "н",
            "нет"
        ):
            return False

        print(f"{RED}{t('invalid')}{RESET}")


def format_bytes(value):
    value = float(value)

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
        "PB",
    ]

    for unit in units:
        if abs(value) < 1024:
            return f"{value:.2f} {unit}"

        value /= 1024

    return f"{value:.2f} EB"


def safe_relative(path):
    try:
        return path.resolve().relative_to(Path.cwd().resolve())
    except Exception:
        return path


# ============================================================
# FILE TOOLS
# ============================================================

def files_menu():
    while True:
        header(t("file_tools"))

        box([
            f"{GREEN}1{RESET}  {t('file_info')}",
            f"{GREEN}2{RESET}  {t('rename')}",
            f"{GREEN}3{RESET}  {t('create_folder')}",
            f"{GREEN}4{RESET}  {t('delete_file')}",
            f"{GREEN}5{RESET}  {t('copy_file')}",
            f"{GREEN}6{RESET}  {t('move_file')}",
            f"{GREEN}7{RESET}  {t('list_folder')}",
            f"{RED}0{RESET}  {t('back')}",
        ])

        print()

        choice = input(f"{BOLD}{t('select')}: {RESET}").strip()

        if choice == "0":
            return

        if choice == "1":
            file_info()

        elif choice == "2":
            rename_file()

        elif choice == "3":
            create_folder()

        elif choice == "4":
            delete_file()

        elif choice == "5":
            copy_file()

        elif choice == "6":
            move_file()

        elif choice == "7":
            list_folder()

        else:
            print(f"{RED}{t('invalid')}{RESET}")
            sleep(0.8)


def file_info():
    header(t("file_info"))

    print(
        f"{DIM}{t('current')}: "
        f"{Path.cwd()}{RESET}"
    )

    path = ask_path(
        t("path"),
        str(Path.cwd() / "example.txt")
    )

    if path is None:
        print(f"{RED}{t('empty_path')}{RESET}")
        pause()
        return

    if not path.exists():
        print(f"{RED}{t('not_found')}{RESET}")
        pause()
        return

    print()

    if path.is_file():
        stat = path.stat()

        print(f"{BOLD}{t('file')}{RESET}: {path.name}")
        print(f"{t('path')}: {path.resolve()}")
        print(f"Size: {format_bytes(stat.st_size)}")
        print(f"Extension: {path.suffix or '-'}")
        print(
            "Modified:",
            datetime.fromtimestamp(
                stat.st_mtime
            ).strftime("%Y-%m-%d %H:%M:%S")
        )

    elif path.is_dir():
        try:
            items = list(path.iterdir())
        except Exception:
            items = []

        print(f"{BOLD}{t('folder')}{RESET}: {path.name}")
        print(f"{t('path')}: {path.resolve()}")
        print(f"Items: {len(items)}")

    pause()


def rename_file():
    header(t("rename"))

    path = ask_path(
        t("path"),
        str(Path.cwd() / "old_name.txt")
    )

    if path is None or not path.exists():
        print(f"{RED}{t('not_found')}{RESET}")
        pause()
        return

    show_path_example(
        t("new_name"),
        path.name
    )

    new_name = input("> ").strip()

    if not new_name:
        print(f"{RED}{t('empty_path')}{RESET}")
        pause()
        return

    destination = path.parent / new_name

    try:
        path.rename(destination)
        print(f"{GREEN}{t('renamed')}{RESET}")

    except Exception as error:
        print(
            f"{RED}{t('operation_error')}: "
            f"{error}{RESET}"
        )

    pause()


def create_folder():
    header(t("create_folder"))

    default = SHARED_STORAGE / "NewFolder"

    path = ask_path(
        t("path"),
        str(SHARED_STORAGE / "MyFolder"),
        default
    )

    if path is None:
        print(f"{RED}{t('empty_path')}{RESET}")
        pause()
        return

    try:
        path.mkdir(
            parents=True,
            exist_ok=True
        )

        print(f"{GREEN}{t('folder_created')}{RESET}")

    except Exception as error:
        print(
            f"{RED}{t('operation_error')}: "
            f"{error}{RESET}"
        )

    pause()


def delete_file():
    header(t("delete_file"))

    path = ask_path(
        t("path"),
        str(Path.cwd() / "example.txt")
    )

    if path is None or not path.exists():
        print(f"{RED}{t('not_found')}{RESET}")
        pause()
        return

    if not path.is_file():
        print(
            f"{RED}This function only deletes files."
            f"{RESET}"
        )
        pause()
        return

    print()
    print(f"{YELLOW}{path.resolve()}{RESET}")

    if not ask_yes_no(t("confirm_delete")):
        print(f"{DIM}Cancelled.{RESET}")
        pause()
        return

    try:
        path.unlink()
        print(f"{GREEN}{t('deleted')}{RESET}")

    except Exception as error:
        print(
            f"{RED}{t('operation_error')}: "
            f"{error}{RESET}"
        )

    pause()


def copy_file():
    header(t("copy_file"))

    source = ask_path(
        t("source"),
        str(Path.cwd() / "example.txt")
    )

    if source is None or not source.exists():
        print(f"{RED}{t('not_found')}{RESET}")
        pause()
        return

    destination = ask_path(
        t("destination"),
        str(Path.cwd() / "backup")
    )

    if destination is None:
        print(f"{RED}{t('empty_path')}{RESET}")
        pause()
        return

    try:
        if destination.exists() and destination.is_dir():
            destination = destination / source.name

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            source,
            destination
        )

        print(f"{GREEN}{t('copied')}{RESET}")

    except Exception as error:
        print(
            f"{RED}{t('operation_error')}: "
            f"{error}{RESET}"
        )

    pause()


def move_file():
    header(t("move_file"))

    source = ask_path(
        t("source"),
        str(Path.cwd() / "example.txt")
    )

    if source is None or not source.exists():
        print(f"{RED}{t('not_found')}{RESET}")
        pause()
        return

    destination = ask_path(
        t("destination"),
        str(Path.cwd() / "new_folder")
    )

    if destination is None:
        print(f"{RED}{t('empty_path')}{RESET}")
        pause()
        return

    try:
        if destination.exists() and destination.is_dir():
            destination = destination / source.name
        else:
            destination.parent.mkdir(
                parents=True,
                exist_ok=True
            )

        shutil.move(
            str(source),
            str(destination)
        )

        print(f"{GREEN}{t('moved')}{RESET}")

    except Exception as error:
        print(
            f"{RED}{t('operation_error')}: "
            f"{error}{RESET}"
        )

    pause()


def list_folder():
    header(t("list_folder"))

    path = ask_path(
        t("path"),
        str(Path.cwd())
    )

    if path is None:
        path = Path.cwd()

    if not path.exists() or not path.is_dir():
        print(f"{RED}{t('folder_not_found')}{RESET}")
        pause()
        return

    try:
        items = sorted(
            path.iterdir(),
            key=lambda item: (
                not item.is_dir(),
                item.name.lower()
            )
        )

        print(
            f"{DIM}{path.resolve()}{RESET}\n"
        )

        if not items:
            print("Empty.")

        for item in items:
            if item.is_dir():
                print(
                    f"{CYAN}📁 {item.name}{RESET}"
                )
            else:
                print(
                    f"{WHITE}📄 {item.name}{RESET}"
                )

    except Exception as error:
        print(
            f"{RED}{t('operation_error')}: "
            f"{error}{RESET}"
        )

    pause()


# ============================================================
# SEARCH
# ============================================================

def search_files():
    header(t("search_files"))

    root = ask_path(
        t("search_folder"),
        str(Path.cwd())
    )

    if root is None:
        root = Path.cwd()

    if not root.exists() or not root.is_dir():
        print(f"{RED}{t('folder_not_found')}{RESET}")
        pause()
        return

    show_path_example(
        t("search_query"),
        "photo"
    )

    query = input("> ").strip()

    if not query:
        print(f"{RED}{t('empty_path')}{RESET}")
        pause()
        return

    print()

    found = []

    end_text = time.time() + 0.4

    while time.time() < end_text:
        for dots in [".  ", ".. ", "..."]:
            print(
                f"\r{CYAN}{t('searching')}{dots}{RESET}",
                end="",
                flush=True
            )
            time.sleep(0.1)

    print()

    try:
        for item in root.rglob("*"):
            try:
                if query.lower() in item.name.lower():
                    found.append(item)

                if len(found) >= 300:
                    break

            except PermissionError:
                continue

    except Exception as error:
        print(
            f"{RED}{t('operation_error')}: "
            f"{error}{RESET}"
        )
        pause()
        return

    if not found:
        print(f"{YELLOW}{t('nothing_found')}{RESET}")

    else:
        print(
            f"{GREEN}{t('found')}: "
            f"{len(found)}{RESET}\n"
        )

        for index, item in enumerate(
            found,
            start=1
        ):
            icon = (
                "📁"
                if item.is_dir()
                else "📄"
            )

            print(
                f"{index:>3}. "
                f"{icon} {item}"
            )

    pause()


# ============================================================
# PASSWORD GENERATOR
# ============================================================

def password_generator():
    header(t("password_generator"))

    while True:
        try:
            length = int(
                input(
                    f"{t('password_length')} "
                    f"(4-500): "
                )
            )

            if 4 <= length <= 500:
                break

        except ValueError:
            pass

        print(f"{RED}{t('invalid')}{RESET}")

    use_upper = ask_yes_no(
        f"{t('upper')} {t('yes_no')}"
    )

    use_lower = ask_yes_no(
        f"{t('lower')} {t('yes_no')}"
    )

    use_numbers = ask_yes_no(
        f"{t('numbers')} {t('yes_no')}"
    )

    use_symbols = ask_yes_no(
        f"{t('symbols')} {t('yes_no')}"
    )

    chars = ""

    if use_upper:
        chars += string.ascii_uppercase

    if use_lower:
        chars += string.ascii_lowercase

    if use_numbers:
        chars += string.digits

    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{};:,.?/"

    if not chars:
        print(
            f"{RED}Choose at least one option."
            f"{RESET}"
        )
        pause()
        return

    generator = random.SystemRandom()

    password = "".join(
        generator.choice(chars)
        for _ in range(length)
    )

    print()
    print(f"{GREEN}{BOLD}{t('generated')}:{RESET}")
    print()
    print(
        f"{YELLOW}{password}{RESET}"
    )

    pause()


# ============================================================
# INTERNET
# ============================================================

def internet_check():
    header(t("internet_check"))

    loading(
        1.2,
        t("checking")
    )

    try:
        with urllib.request.urlopen(
            "https://www.google.com",
            timeout=5
        ) as response:

            if response.status:
                print(
                    f"{GREEN}"
                    f"✓ {t('internet_available')}"
                    f"{RESET}"
                )

            else:
                print(
                    f"{RED}"
                    f"✗ {t('internet_unavailable')}"
                    f"{RESET}"
                )

    except Exception:
        print(
            f"{RED}"
            f"✗ {t('internet_unavailable')}"
            f"{RESET}"
        )

    pause()


# ============================================================
# PING
# ============================================================

def ping_host():
    header(t("ping_menu"))

    show_path_example(
        t("host"),
        "1.1.1.1"
    )

    host = input("> ").strip()

    if not host:
        host = "1.1.1.1"

    print()

    try:
        resolved = socket.gethostbyname(host)

        print(
            f"{DIM}IP: {resolved}{RESET}"
        )

    except Exception:
        print(
            f"{YELLOW}"
            f"DNS: unable to resolve host"
            f"{RESET}"
        )

    if os.name == "nt":
        command = [
            "ping",
            "-n",
            "4",
            host
        ]
    else:
        command = [
            "ping",
            "-c",
            "4",
            host
        ]

    try:
        subprocess.run(command)

    except FileNotFoundError:
        print(
            f"{RED}"
            f"Ping command is not available."
            f"{RESET}"
        )

    except Exception as error:
        print(
            f"{RED}{error}{RESET}"
        )

    pause()


# ============================================================
# SYSTEM INFORMATION
# ============================================================

def get_ram():
    meminfo = Path("/proc/meminfo")

    if meminfo.exists():
        try:
            text = meminfo.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            total = None
            available = None

            for line in text.splitlines():

                if line.startswith("MemTotal:"):
                    total = (
                        int(line.split()[1])
                        * 1024
                    )

                if line.startswith(
                    "MemAvailable:"
                ):
                    available = (
                        int(line.split()[1])
                        * 1024
                    )

            if total and available:
                used = total - available

                return (
                    f"{format_bytes(used)} / "
                    f"{format_bytes(total)}"
                )

        except Exception:
            pass

    return "N/A"


def system_info():
    header(t("system_info"))

    print(
        f"{BOLD}{t('os')}:{RESET} "
        f"{platform.system()} "
        f"{platform.release()}"
    )

    print(
        f"{BOLD}{t('computer')}:{RESET} "
        f"{platform.node() or 'N/A'}"
    )

    print(
        f"{BOLD}{t('hostname')}:{RESET} "
        f"{socket.gethostname()}"
    )

    print(
        f"{BOLD}{t('architecture')}:{RESET} "
        f"{platform.machine()}"
    )

    print(
        f"{BOLD}{t('python')}:{RESET} "
        f"{platform.python_version()}"
    )

    print(
        f"{BOLD}{t('processor')}:{RESET} "
        f"{platform.processor() or platform.machine()}"
    )

    print(
        f"{BOLD}{t('cores')}:{RESET} "
        f"{os.cpu_count() or 'N/A'}"
    )

    print(
        f"{BOLD}{t('ram')}:{RESET} "
        f"{get_ram()}"
    )

    try:
        disk = shutil.disk_usage(
            Path.cwd()
        )

        disk_text = (
            f"{format_bytes(disk.free)} free / "
            f"{format_bytes(disk.total)}"
        )

    except Exception:
        disk_text = "N/A"

    print(
        f"{BOLD}{t('disk')}:{RESET} "
        f"{disk_text}"
    )

    print(
        f"{BOLD}{t('current_dir')}:{RESET} "
        f"{Path.cwd()}"
    )

    pause()


# ============================================================
# ZIP TOOLS
# ============================================================

def zip_menu():
    while True:
        header(t("zip_tools"))

        box([
            f"{GREEN}1{RESET}  {t('create_zip')}",
            f"{GREEN}2{RESET}  {t('extract_zip')}",
            f"{RED}0{RESET}  {t('back')}",
        ])

        print()

        choice = input(
            f"{BOLD}{t('select')}: {RESET}"
        ).strip()

        if choice == "0":
            return

        elif choice == "1":
            create_zip()

        elif choice == "2":
            extract_zip()

        else:
            print(
                f"{RED}{t('invalid')}{RESET}"
            )
            sleep(0.8)


def create_zip():
    header(t("create_zip"))

    source = ask_path(
        t("archive_source"),
        str(
            SHARED_STORAGE / "MyFolder"
        )
    )

    if source is None or not source.exists():
        print(
            f"{RED}{t('not_found')}{RESET}"
        )
        pause()
        return

    output = ask_path(
        t("archive_output"),
        str(
            SHARED_STORAGE / "archive.zip"
        )
    )

    if output is None:
        output = Path.cwd() / "archive.zip"

    if output.suffix.lower() != ".zip":
        output = output.with_suffix(".zip")

    try:
        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with zipfile.ZipFile(
            output,
            "w",
            compression=zipfile.ZIP_DEFLATED
        ) as archive:

            if source.is_file():
                archive.write(
                    source,
                    arcname=source.name
                )

            else:
                for item in source.rglob("*"):
                    if item.is_file():
                        archive.write(
                            item,
                            arcname=item.relative_to(
                                source.parent
                            )
                        )

        print()
        print(
            f"{GREEN}"
            f"✓ {t('archive_created')}"
            f"{RESET}"
        )

        print(
            f"{DIM}{output.resolve()}{RESET}"
        )

    except Exception as error:
        print(
            f"{RED}"
            f"{t('operation_error')}: "
            f"{error}"
            f"{RESET}"
        )

    pause()


def extract_zip():
    header(t("extract_zip"))

    zip_path = ask_path(
        t("zip_file"),
        str(
            SHARED_STORAGE / "archive.zip"
        )
    )

    if (
        zip_path is None
        or not zip_path.exists()
        or not zip_path.is_file()
    ):
        print(
            f"{RED}{t('not_found')}{RESET}"
        )
        pause()
        return

    destination = ask_path(
        t("extract_to"),
        str(
            SHARED_STORAGE / "Extracted"
        )
    )

    if destination is None:
        destination = (
            Path.cwd() / "Extracted"
        )

    try:
        destination.mkdir(
            parents=True,
            exist_ok=True
        )

        with zipfile.ZipFile(
            zip_path,
            "r"
        ) as archive:

            archive.extractall(
                destination
            )

        print()
        print(
            f"{GREEN}"
            f"✓ {t('archive_extracted')}"
            f"{RESET}"
        )

        print(
            f"{DIM}{destination.resolve()}{RESET}"
        )

    except Exception as error:
        print(
            f"{RED}"
            f"{t('operation_error')}: "
            f"{error}"
            f"{RESET}"
        )

    pause()


# ============================================================
# CONVERTER
# ============================================================

def converter():
    while True:
        header(t("converter"))

        box([
            f"{GREEN}1{RESET}  {t('bytes_mb')}",
            f"{GREEN}2{RESET}  {t('mb_bytes')}",
            f"{GREEN}3{RESET}  {t('gb_mb')}",
            f"{GREEN}4{RESET}  {t('mb_gb')}",
            f"{GREEN}5{RESET}  {t('c_f')}",
            f"{GREEN}6{RESET}  {t('f_c')}",
            f"{RED}0{RESET}  {t('back')}",
        ])

        print()

        choice = input(
            f"{BOLD}{t('select')}: {RESET}"
        ).strip()

        if choice == "0":
            return

        try:
            value = float(
                input(
                    f"{t('value')}: "
                )
            )

        except ValueError:
            print(
                f"{RED}{t('invalid')}{RESET}"
            )
            sleep(0.8)
            continue

        if choice == "1":
            result = value / (1024 ** 2)
            unit = "MB"

        elif choice == "2":
            result = value * (1024 ** 2)
            unit = "bytes"

        elif choice == "3":
            result = value * 1024
            unit = "MB"

        elif choice == "4":
            result = value / 1024
            unit = "GB"

        elif choice == "5":
            result = (
                value * 9 / 5
            ) + 32

            unit = "°F"

        elif choice == "6":
            result = (
                value - 32
            ) * 5 / 9

            unit = "°C"

        else:
            print(
                f"{RED}{t('invalid')}{RESET}"
            )
            sleep(0.8)
            continue

        print()
        print(
            f"{GREEN}{BOLD}"
            f"{result:.6f} {unit}"
            f"{RESET}"
        )

        pause()


# ============================================================
# NOTES
# ============================================================

def ensure_notes():
    ensure_config_dir()

    if not NOTES_FILE.exists():
        NOTES_FILE.write_text(
            "[]",
            encoding="utf-8"
        )


def load_notes():
    ensure_notes()

    try:
        return json.loads(
            NOTES_FILE.read_text(
                encoding="utf-8"
            )
        )

    except Exception:
        return []


def save_notes(notes):
    ensure_notes()

    NOTES_FILE.write_text(
        json.dumps(
            notes,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


def notes_menu():
    while True:
        header(t("notes"))

        box([
            f"{GREEN}1{RESET}  {t('create_note')}",
            f"{GREEN}2{RESET}  {t('view_notes')}",
            f"{GREEN}3{RESET}  {t('delete_note')}",
            f"{RED}0{RESET}  {t('back')}",
        ])

        print()

        choice = input(
            f"{BOLD}{t('select')}: {RESET}"
        ).strip()

        if choice == "0":
            return

        elif choice == "1":
            create_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            delete_note()

        else:
            print(
                f"{RED}{t('invalid')}{RESET}"
            )
            sleep(0.8)


def create_note():
    header(t("create_note"))

    print(
        f"{DIM}{t('note_title')}{RESET}"
    )

    title = input("> ").strip()

    if not title:
        return

    print(
        f"{DIM}{t('note_text')}{RESET}"
    )

    text = input("> ").strip()

    notes = load_notes()

    next_id = 1

    if notes:
        next_id = max(
            note.get("id", 0)
            for note in notes
        ) + 1

    notes.append({
        "id": next_id,
        "title": title,
        "text": text,
        "created": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    })

    save_notes(notes)

    print(
        f"{GREEN}{t('note_created')}{RESET}"
    )

    pause()


def view_notes():
    header(t("view_notes"))

    notes = load_notes()

    if not notes:
        print(
            f"{YELLOW}{t('no_notes')}{RESET}"
        )
        pause()
        return

    for note in notes:
        print(
            f"{CYAN}"
            f"[{note.get('id', '?')}]"
            f"{RESET} "
            f"{BOLD}"
            f"{note.get('title', '')}"
            f"{RESET}"
        )

        print(
            f"    {note.get('text', '')}"
        )

        print(
            f"    {DIM}"
            f"{note.get('created', '')}"
            f"{RESET}"
        )

        print()

    pause()


def delete_note():
    header(t("delete_note"))

    notes = load_notes()

    if not notes:
        print(
            f"{YELLOW}{t('no_notes')}{RESET}"
        )
        pause()
        return

    for note in notes:
        print(
            f"{CYAN}"
            f"[{note.get('id', '?')}]"
            f"{RESET} "
            f"{note.get('title', '')}"
        )

    print()

    try:
        note_id = int(
            input(
                f"{t('note_number')}: "
            )
        )

    except ValueError:
        print(
            f"{RED}{t('invalid')}{RESET}"
        )
        pause()
        return

    found = False

    new_notes = []

    for note in notes:
        if note.get("id") == note_id:
            found = True
        else:
            new_notes.append(note)

    if not found:
        print(
            f"{RED}{t('invalid')}{RESET}"
        )
        pause()
        return

    save_notes(new_notes)

    print(
        f"{GREEN}{t('note_deleted')}{RESET}"
    )

    pause()


# ============================================================
# SETTINGS
# ============================================================

def settings():
    global LANGUAGE

    while True:
        header(t("settings"))

        box([
            f"{GREEN}1{RESET}  {t('change_language')}",
            f"{GREEN}2{RESET}  {t('reset_language')}",
            f"{GREEN}3{RESET}  {t('version')}: {VERSION}",
            f"{RED}0{RESET}  {t('back')}",
        ])

        print()

        choice = input(
            f"{BOLD}{t('select')}: {RESET}"
        ).strip()

        if choice == "0":
            return

        elif choice == "1":
            old_language = LANGUAGE

            print()
            print(
                f"{CYAN}[1]{RESET} "
                f"{t('russian')}"
            )
            print(
                f"{CYAN}[2]{RESET} "
                f"{t('english')}"
            )

            new_language = input(
                "> "
            ).strip()

            if new_language == "1":
                LANGUAGE = "ru"
                save_config()
                print(
                    f"{GREEN}{t('saved')}{RESET}"
                )

            elif new_language == "2":
                LANGUAGE = "en"
                save_config()
                print(
                    f"{GREEN}{t('saved')}{RESET}"
                )

            else:
                LANGUAGE = old_language

                print(
                    f"{RED}{t('invalid')}{RESET}"
                )

            sleep(0.7)

        elif choice == "2":
            if CONFIG_FILE.exists():
                try:
                    CONFIG_FILE.unlink()
                except Exception:
                    pass

            print(
                f"{GREEN}{t('saved')}{RESET}"
            )

            pause()
            return

        elif choice == "3":
            print()
            print(
                f"QuickTools "
                f"v{VERSION}"
            )
            pause()

        else:
            print(
                f"{RED}{t('invalid')}{RESET}"
            )
            sleep(0.7)


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():
    header(APP_NAME)

    show_logo()

    box([
        f"{GREEN}1{RESET}   {t('files')}",
        f"{GREEN}2{RESET}   {t('search')}",
        f"{GREEN}3{RESET}   {t('password')}",
        f"{GREEN}4{RESET}   {t('internet')}",
        f"{GREEN}5{RESET}   {t('system')}",
        f"{GREEN}6{RESET}   {t('zip')}",
        f"{GREEN}7{RESET}   {t('converter')}",
        f"{GREEN}8{RESET}   {t('notes')}",
        f"{GREEN}9{RESET}   {t('settings')}",
        f"{MAGENTA}10{RESET}  {t('ping')}",
        f"{RED}0{RESET}   {t('exit')}",
    ])

    print()

    return input(
        f"{BOLD}{t('select')}: {RESET}"
    ).strip()


# ============================================================
# EXIT ANIMATION
# ============================================================

def goodbye_animation():
    clear_screen()

    print()

    type_text(
        f"{CYAN}QuickTools v{VERSION}{RESET}",
        0.035
    )

    print()

    messages = [
        f"{DIM}Закрываем программу...{RESET}"
        if LANGUAGE == "ru"
        else f"{DIM}Closing QuickTools...{RESET}",

        f"{DIM}Сохраняем настройки...{RESET}"
        if LANGUAGE == "ru"
        else f"{DIM}Saving settings...{RESET}",

        f"{GREEN}{t('goodbye')}{RESET}",
    ]

    for message in messages:
        type_text(message, 0.025)
        sleep(0.35)

    print()


# ============================================================
# STARTUP
# ============================================================

def startup():
    global LANGUAGE

    load_config()

    if LANGUAGE is None:
        # Temporary language for first screen.
        LANGUAGE = "ru"

        choose_language(first_start=True)

    else:
        # Already saved.
        clear_screen()

        print()
        show_logo()

        print(
            f"{DIM}"
            f"{t('welcome')}"
            f"{RESET}"
        )

        print()

        progress_bar(
            0.8,
            32
        )

        sleep(0.25)


# ============================================================
# MAIN LOOP
# ============================================================

def run():
    startup()

    while True:
        try:
            choice = main_menu()

            if choice == "1":
                files_menu()

            elif choice == "2":
                search_files()

            elif choice == "3":
                password_generator()

            elif choice == "4":
                internet_check()

            elif choice == "5":
                system_info()

            elif choice == "6":
                zip_menu()

            elif choice == "7":
                converter()

            elif choice == "8":
                notes_menu()

            elif choice == "9":
                settings()

            elif choice == "10":
                ping_host()

            elif choice == "0":
                goodbye_animation()
                break

            else:
                print(
                    f"{RED}{t('invalid')}{RESET}"
                )
                sleep(0.8)

        except KeyboardInterrupt:
            print()
            goodbye_animation()
            break

        except Exception as error:
            print()
            print(
                f"{RED}"
                f"Unexpected error: {error}"
                f"{RESET}"
            )
            pause()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run()