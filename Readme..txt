1. Objective
Automate the creation of YouTube videos with the following features:

Scrape Instagram videos from 100+ usernames.
Save metadata and statuses in a database for management.
Compile videos into a single YouTube-ready format.
Upload compiled videos daily to YouTube.
Automatically clean up unused files.
2. Requirements
System Setup
OS: Linux terminal-based system.
Python Environment: Python 3.8+ with pip installed.
Key Libraries:
selenium, moviepy, ffmpeg-python, google-api-python-client, sqlite3.
Tools and Dependencies
Install Required Tools
Chrome (Headless) and ChromeDriver

bash
Copy code
sudo apt update
sudo apt install -y chromium-browser
wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/
Xvfb (GUI Emulation)

bash
Copy code
sudo apt install -y xvfb
FFmpeg (Video Processing)

bash
Copy code
sudo apt install -y ffmpeg
Python Libraries

bash
Copy code
pip install selenium moviepy google-api-python-client oauth2client requests sqlite3 schedule
3. Folder Structure
plaintext
Copy code
project/
├── database.db                # SQLite database
├── usernames.txt              # List of Instagram usernames
├── downloads/                 # Folder for downloaded Instagram videos
│   ├── username1/
│   ├── username2/
├── compiled/                  # Folder for compiled YouTube-ready videos
├── logs/                      # Log files for debugging
│   ├── scraper_log.txt
│   ├── activity_log.txt
├── scraper.py                 # Instagram video scraper script
├── compile_videos.py          # Video compilation script
├── upload_youtube.py          # YouTube uploader script
├── cleanup.py                 # Cleanup script
└── main.py                    # Main pipeline orchestrator




	WHEN DONE 

6. Automation
Use cron to schedule daily execution.
bash
Copy code
crontab -e
Add the following entry to run at 2 AM daily:

bash
Copy code
0 2 * * * xvfb-run python /path/to/main.py