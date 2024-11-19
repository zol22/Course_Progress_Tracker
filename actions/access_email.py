import msal
import requests
from config import CLIENT_ID, TENANT_ID, SCOPE
import time

class EmailHandler:
    AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
    REDIRECT_URI = 'https://www.udemy.com/join/passwordless-auth/'

    def __init__(self, driver):
        self.driver = driver

    def get_oauth2_token(self):
        """Authenticate and retrieve an OAuth2 access token."""
        app = msal.PublicClientApplication(CLIENT_ID, authority=self.AUTHORITY)

        # Attempt to acquire a token
        auth_request = None
        accounts = app.get_accounts()

        if accounts:
            # If accounts exist, try to acquire the token silently (without prompting user)
            auth_request = app.acquire_token_silent(SCOPE, account=accounts[0])

        if not auth_request:
            # If no token is available or silent token acquisition failed, request interactive login
            auth_request = app.acquire_token_interactive(SCOPE)

        if "access_token" in auth_request:
            print("Access Token acquired successfully.")
            return auth_request["access_token"]
        else:
            print("Error acquiring token:", auth_request.get("error"))
            print("Description:", auth_request.get("error_description"))
            return None



    def get_email_messages(self):
        """Retrieve email messages using Microsoft Graph API."""
        access_token = self.get_oauth2_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        graph_url = "https://graph.microsoft.com/v1.0/me/messages"

        response = requests.get(graph_url, headers=headers)

        print(response)

        if response.status_code == 200:
            return response.json().get("value", [])
        else:
            raise RuntimeError(f"Failed to fetch messages: {response.text}")
