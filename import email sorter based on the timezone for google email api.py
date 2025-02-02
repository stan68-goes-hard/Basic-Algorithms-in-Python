import pytz
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Function to authenticate and create a Gmail API service
def create_gmail_service():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    SERVICE_ACCOUNT_FILE = '/path/to/service_account.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('gmail', 'v1', credentials=credentials)
    return service

# Function to fetch emails from Gmail
def fetch_emails(service, user_id='me'):
    results = service.users().messages().list(userId=user_id, labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])

    emails = []
    for message in messages:
        msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
        payload = msg['payload']
        headers = payload['headers']
        subject = next(header['value'] for header in headers if header['name'] == 'Subject')
        date = next(header['value'] for header in headers if header['name'] == 'Date')
        emails.append({"subject": subject, "date": date})
    return emails

# Create Gmail API service
service = create_gmail_service()

# Fetch emails
emails = fetch_emails(service)
# Sample email data
emails = [
    {"subject": "Meeting in PST", "body": "Let's meet at 10 AM PST", "date": "2023-10-01 10:00:00"},
    {"subject": "Meeting in EST", "body": "Let's meet at 10 AM EST", "date": "2023-10-01 10:00:00"},
    {"subject": "Meeting in GMT", "body": "Let's meet at 10 AM GMT", "date": "2023-10-01 10:00:00"},
]

# Function to extract timezone from subject
def extract_timezone(subject):
    timezones = {
        "PST": "US/Pacific",
        "EST": "US/Eastern",
        "GMT": "GMT",
    }
    for tz in timezones:
        if tz in subject:
            return timezones[tz]
    return None

# Function to convert email date to UTC
def convert_to_utc(email):
    tz = extract_timezone(email["subject"])
    if tz:
        local_tz = pytz.timezone(tz)
        local_dt = local_tz.localize(datetime.strptime(email["date"], "%Y-%m-%d %H:%M:%S"))
        utc_dt = local_dt.astimezone(pytz.utc)
        email["utc_date"] = utc_dt
    else:
        email["utc_date"] = datetime.strptime(email["date"], "%Y-%m-%d %H:%M:%S")
    return email

# Convert all emails to UTC
emails = [convert_to_utc(email) for email in emails]

# Sort emails by UTC date
sorted_emails = sorted(emails, key=lambda x: x["utc_date"])

# Print sorted emails
for email in sorted_emails:
    print(f"Subject: {email['subject']}, Date: {email['utc_date']}")
    # Updated timezones to Russian timezones
    timezones = {
        "MSK": "Europe/Moscow",
        "SAMT": "Europe/Samara",
        "YEKT": "Asia/Yekaterinburg",
        "VLAT": "Asia/Vladivostok",
    }

    # Function to extract timezone from subject
    def extract_timezone(subject):
        for tz in timezones:
            if tz in subject:
                return timezones[tz]
        return None

    # Function to convert email date to UTC
    def convert_to_utc(email):
        tz = extract_timezone(email["subject"])
        if tz:
            local_tz = pytz.timezone(tz)
            local_dt = local_tz.localize(datetime.strptime(email["date"], "%Y-%m-%d %H:%M:%S"))
            utc_dt = local_dt.astimezone(pytz.utc)
            email["utc_date"] = utc_dt
        else:
            email["utc_date"] = datetime.strptime(email["date"], "%Y-%m-%d %H:%M:%S")
        return email

    # Convert all emails to UTC
    emails = [convert_to_utc(email) for email in emails]

    # Sort emails by UTC date
    sorted_emails = sorted(emails, key=lambda x: x["utc_date"])

    # Print sorted emails
    for email in sorted_emails:
        print(f"Subject: {email['subject']}, Date: {email['utc_date']}")