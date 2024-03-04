# Cloudflare Access Group IP Update Script 
Updates an access group IP in Cloudflare from a DNS lookup.

# Use Case
1. You want to use Cloudflare Tunnel to securely access resouces in your local network remotely. https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/
2. Locally you want to bypass authentication. https://developers.cloudflare.com/cloudflare-one/policies/access/
3. Your ISP uses dynamic IP addresses.
4. You don't want to manage local DNS records separately from the external couldflare records.

# Requirements
1. You already have a dynamic DNS service setup, such as noip.com or duckdns.com
