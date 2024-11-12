import msal
import re
import requests
from config import CLIENT_ID, TENANT_ID, SCOPE

AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'

def get_oauth2_token():
    """
       Authenticate and retrieve an OAuth2 access token.
       """

    #  Authenticate and retrieve an OAuth2 access token.
    app = msal.PublicClientApplication(CLIENT_ID,authority=AUTHORITY)
    print("Requesting OAuth2 token...")

    # Attempt to acquire a token
    result = None
    accounts = app.get_accounts()

    if accounts:
        # If accounts exist, try to acquire the token silently (without prompting user)
        result = app.acquire_token_silent(scopes = SCOPE, account=accounts[0])

    if not result:
        # If no token is available or silent token acquisition failed, request interactive login
        result = app.acquire_token_interactive(scopes = SCOPE)

    #  Check if the token acquisition was successful
    if "access_token" in result:
        print("Access Token:", result["access_token"])
        return result["access_token"]
    else:
        print("Error acquiring token:", result.get("error"))
        print("Description:", result.get("error_description"))
        return None


def get_email_messages():
    """
    Retrieve email messages from Microsoft Graph using the access token.
    """

    """Fetch recent email messages using Microsoft Graph API."""
    access_token = get_oauth2_token()
    if not access_token:
        return None

    headers = {"Authorization": f"Bearer {access_token}"}
    graph_url = "https://graph.microsoft.com/v1.0/me/messages"
    response = requests.get(graph_url, headers=headers)

    if response.status_code == 200:
        print("Successfully retrieved email messages.")
        return response.json().get('value', [])
    else:
        print(f"Failed to retrieve messages: {response.status_code}")
        print(f"Error Message: {response.text}")
        return None





