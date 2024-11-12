import imaplib
import msal
import re
import email

import requests

# Define constants

# Azure App Registration Details
CLIENT_ID # Get this from your Azure app registration
CLIENT_SECRET  # Get this from your Azure app registration
#TENANT_ID =  # Get this from your Azure app registration
TENANT_ID = 'common'  # Get this from your Azure app registration
AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
#SCOPE = ["https://outlook.office.com/IMAP.AccessAsUser.All"]
SCOPE = ["https://graph.microsoft.com/.default"]


# IMAP Server Details
IMAP_SERVER = "imap-mail.outlook.com"

# Function to get the OAuth2 token
def get_oauth2_token():

    # Step 1: Initialize the MSAL ConfidentialClientApplication instance
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY    )

    print("Requesting OAuth2 token...")

    # Step 2: Attempt to acquire a token
    # Get the access token interactively
    result = None
    accounts = app.get_accounts()

    if accounts:
        # If accounts exist, try to acquire the token silently (without prompting user)
        result = app.acquire_token_silent(scopes = SCOPE, account=accounts[0])

    if not result:
        # If no token is available or silent token acquisition failed, request interactive login
        result = app.acquire_token_interactive(scopes = SCOPE)

    # Step 4: Check if the token acquisition was successful
    if "access_token" in result:
        print("Access Token:", result["access_token"])

        # Step 5: Use the access token to make a request to Microsoft Graph
        headers = {"Authorization": f"Bearer {result['access_token']}"}
        # Replace "user_email@example.com" with the target user's email address
        graph_url =  "https://graph.microsoft.com/v1.0/me/messages"

        response = requests.get(graph_url, headers=headers)

        if response.status_code == 200:
            # Print the list of email messages
            messages = response.json().get('value', [])
            for message in messages:
                print(f"From: {message['from']['emailAddress']['address']}")
                print(f"Subject: {message['subject']}")
                print("Body:", message['bodyPreview'])
                print("-" * 50)
        else:
            print(f"Failed to retrieve messages: {response.status_code}")
            print(f"Error Message: {response.text}")
    else:
        # Step 6: Handle errors if token acquisition fails
        print("Error acquiring token:", result.get("error"))
        print("Description:", result.get("error_description"))

get_oauth2_token()



