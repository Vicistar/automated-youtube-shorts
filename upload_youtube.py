from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

def upload_to_youtube(video_path, title, description, tags):
    # Authentication
    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', scopes=["https://www.googleapis.com/auth/youtube.upload"])
    credentials = flow.run_console()

    youtube = build('youtube', 'v3', credentials=credentials)

    # Upload
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=video_path
    )
    response = request.execute()
    return response.get('id')
