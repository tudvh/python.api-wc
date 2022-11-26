import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def get():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyALr9to_aOjni6cDvMf13g8Wdb-zqpwfRM"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q="world cup 2022"
    )
    response = request.execute()

    return response
