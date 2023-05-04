#!/usr/bin/env python3

import os
import subprocess
import datetime

# Get the absolute path to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to your homebrew installation directory
HOMEBREW_DIR = '/usr/local/Homebrew'

# Path to the log file
LOG_FILE = os.path.join(SCRIPT_DIR, 'homebrew_updater.log')

# Run 'brew update' to update Homebrew itself
update_output = subprocess.check_output(['brew', 'update'], stderr=subprocess.STDOUT).decode('utf-8')

# Run 'brew upgrade' to update installed packages
upgrade_output = subprocess.check_output(['brew', 'upgrade'], stderr=subprocess.STDOUT).decode('utf-8')

# Write a log message
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
message = f'{timestamp}: Homebrew packages updated\n\n'
message += f'brew update output:\n{update_output}\n\n'
message += f'brew upgrade output:\n{upgrade_output}\n\n'
with open(LOG_FILE, 'a') as f:
    f.write(message)

# Generate a report
report = subprocess.check_output(['brew', 'list', '--versions']).decode('utf-8')

# Send a notification
title = 'Homebrew update complete'
body = 'The following packages have been updated:\n' + report
os.system(f"osascript -e 'display notification \"{body}\" with title \"{title}\"'")
