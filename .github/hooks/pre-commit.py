#!/usr/bin/env python3

import subprocess
import sys

def run_gitleaks():
    command = ['gitleaks', '--verbose', '--redact']
    process = subprocess.run(command, capture_output=True, text=True)
    return process.stdout

def check_secrets():
    output = run_gitleaks()
    if output:
        print("Помилка: Знайдено секрети в коді:")
        print(output)
        sys.exit(1)

if __name__ == '__main__':
    check_secrets()
