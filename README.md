# Cloudflare Access Group IP Update Script 
Updates an access group IP in Cloudflare from a DNS lookup.

# Use Case
1. You want to use Cloudflare Tunnel to securely access resouces in your local network remotely. https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/
2. Locally you want to bypass authentication. https://developers.cloudflare.com/cloudflare-one/policies/access/
3. Your ISP uses dynamic IP addresses.
4. You don't want to manage local DNS records separately from the external couldflare records.

# Requirements
1. You already have a dynamic DNS service setup, such as noip.com or duckdns.com

# Notes
To run the script, you may need to install 'requests' via
```
pip install requests
```

# Running as a cron job on Ubuntu
To run this script every 5 minutes, for example, using crontab, you need to add an entry to your crontab file.

Open your crontab file for editing using the command crontab -e.
Add the following line to the end of the file:
```
*/5 * * * * /usr/bin/python3 /path/to/your/cloudflare_accessgroup_update.py
```
This line tells cron to run the specified Python3 script every 5 minutes. Make sure to replace /path/to/your/script.py with the actual path to the script.
