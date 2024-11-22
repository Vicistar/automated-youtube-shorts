from moviepy.editor import VideoFileClip, concatenate_videoclips
import sqlite3
import os

def compile_videos():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Fetch unused videos
    cursor.execute("SELECT file_path FROM videos WHERE status='unused'")
    video_paths = [row[0] for row in cursor.fetchall()]

    clips = [VideoFileClip(path).subclip(0, 30) for path in video_paths]  # Use first 30 secs of each
    final_clip = concatenate_videoclips(clips)

    output_path = "compiled/final_video.mp4"
    final_clip.write_videofile(output_path, codec="libx264", fps=24)

    # Update database
    for path in video_paths:
        cursor.execute("UPDATE videos SET status='used' WHERE file_path=?", (path,))
    conn.commit()
    conn.close()

    return output_path
