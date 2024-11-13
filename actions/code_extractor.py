import re

def extract_verification_code(messages):
    """
        Extract the 6-digit verification code from Udemy email messages.
    """
    for message in messages:
        if 'Udemy' in message.get('subject', ''):
            body = message.get('body', {}).get('content', '')

            # Regex to match the 6-digit code
            match = re.search(r'\b\d{6}\b', body)
            if match:
                verification_code = match.group()
                print(f"Verification code found: {verification_code}")
                return verification_code

    print("No Udemy verification code found.")
    return None
