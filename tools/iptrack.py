import requests

def iptrack(ip):
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()
        
        if 'bogon' in data:
            print(f"The IP {ip} is a bogon (private or reserved IP address).")
        else:
            city = data.get('city', 'Unknown')
            region = data.get('region', 'Unknown')
            country = data.get('country', 'Unknown')
            print(f"IP from {ip} is located in {city}, {region}, {country}")
    except Exception as e:
        print(f"Could not perform Geo-IP lookup for IP {ip}: {e}")