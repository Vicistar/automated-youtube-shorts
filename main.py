from scraper import scrape_instagram
from compile_videos import compile_videos
from upload_youtube import upload_to_youtube
from cleanup import cleanup_files

if __name__ == "__main__":
    with open("usernames.txt") as f:
        usernames = f.read().splitlines()

    for username in usernames:
        scrape_instagram(username)

    compiled_video = compile_videos()
    upload_to_youtube(compiled_video, "Daily Compilation", "Daily Instagram Highlights", ["instagram", "highlights"])
    cleanup_files()
