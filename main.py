
import auth
from google.apps import meet_v2 as meet

def create_space(USER_CREDENTIALS) -> meet.Space:
    """Create a meeting space."""
    client = meet.SpacesServiceClient(credentials=USER_CREDENTIALS)
    request = meet.CreateSpaceRequest()
    return client.create_space(request=request)

def main():
    USER_CREDENTIALS = auth.get_credentials()
    create_space(USER_CREDENTIALS)

if __name__ == "__main__":
    main()
