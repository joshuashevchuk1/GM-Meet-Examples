from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload

# If modifying these SCOPES, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def download_google_doc(file_id, export_mime='application/pdf', output_file='output.pdf'):
    creds = None

    # Load credentials (or get new ones)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'oauth.json', SCOPES)  # You need to download this from Google Cloud
        creds = flow.run_local_server(port=0)

    service = build('drive', 'v3', credentials=creds)

    request = service.files().export_media(fileId=file_id,
                                           mimeType=export_mime)

    fh = io.FileIO(output_file, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

    print(f"Downloaded '{output_file}' successfully.")

# Replace with your file's ID
file_id = '1_CLDXIbUf3b42WNtzcVIEk09wrcc9ILqrfw1gjdmHN4'
download_google_doc(file_id, export_mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document', output_file='Transcript_test.docx')
