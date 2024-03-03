import requests
import json
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Cloudflare API token and email configurations
CF_API_TOKEN = ''
CF_ACCOUNT_ID = ''
CF_ACCESS_GROUP_ID = ''

# Domain Lookup
DOMAIN1_COM = 'your_site.freeddns.org'

# SMTP Settings
EMAIL_TO = 'user@example.com'
EMAIL_FROM = 'user@example.com'
EMAIL_SUBJECT = 'Cloudflare API Error'
SMTP_SERVER = 'smtp.server.net'
SMTP_PORT = '587'
SMTP_USERNAME = ''
SMTP_PASSWORD = ''

# Function to get the IP address of a domain
def get_domain_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to update Cloudflare access group with new IP
def update_access_group_ip(ip):
    headers = {
        'Authorization': f'Bearer {CF_API_TOKEN}',
        'Content-Type': 'application/json',
    }

    data = {
        "include": [{"ip": {"ip": ip}}]
    }

    url = f'https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/access/groups/{CF_ACCESS_GROUP_ID}'
    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Access group updated successfully!")
    else:
        print("Failed to update access group. Error:" + response.text)
        send_email(EMAIL_TO, f"Failed to update access group. Error: {response.text}")

# Function to send email notification
def send_email(to_email, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            msg = MIMEMultipart()
            msg['From'] = EMAIL_FROM
            msg['To'] = EMAIL_TO
            msg['Subject'] = EMAIL_SUBJECT
            msg.attach(MIMEText(message, 'plain'))
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Email sending failed: {e}")

# Main function
def main():
    current_ip = get_domain_ip(DOMAIN1_COM)
    if current_ip:
        current_ip += "/32"  # Append "/32" to the IP address
        print(f"IP address of {DOMAIN1_COM}: {current_ip}")

        headers = {
            'Authorization': f'Bearer {CF_API_TOKEN}',
            'Content-Type': 'application/json',
        }

        url = f'https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/access/groups/{CF_ACCESS_GROUP_ID}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            access_group_ip = data['result']['include'][0]['ip']['ip']
            if current_ip != access_group_ip:
                print("IP addresses are different. Updating access group.")
                update_access_group_ip(current_ip)
            else:
                print("IP addresses are the same. No action needed.")
        else:
            print("Failed to fetch access group.")
            send_email(EMAIL_TO, f"Failed to fetch access group. Error: {response.text}")
    else:
        print("Failed to retrieve IP address of the domain.")

if __name__ == "__main__":
    main()
