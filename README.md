# Homebrew updater

Updates all installed homebrew packages, writes a log file and runs an apple script to produce a notification.

I use this in combination with a crontab entry to update all my packages every day at 9:00 am.
To do this just run ``` crontab -e ``` and add the following line: ``` 0 9 * * * /path/to/python/ /path/to/script/homebrew_update.py ```

## Requirements

* macOS
* python