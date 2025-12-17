# core/logger.py
import os
from termcolor import colored # pip install termcolor

class Logger:
    @staticmethod
    def info(message):
        print(colored(f"[*] {message}", "blue"))

    @staticmethod
    def success(message):
        print(colored(f"[+] {message}", "green", attrs=['bold']))

    @staticmethod
    def error(message):
        print(colored(f"[!] ERROR: {message}", "red", attrs=['bold']))

    @staticmethod
    def banner():
        # Your cool ASCII art for 1NFERNO goes here
        print(colored("1NFERNO OBFUSCATOR v1.0", "red", attrs=['bold', 'blink']))
