import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    return ip

def get_location(ip):
    url = f'https://ipinfo.io/{ip}/json'
    response = requests.get(url)
    data = response.json()
    return data

def main():
    print("Finding your location...")
    ip = get_public_ip()
    location_data = get_location(ip)
    
    print("\nYour IP Address:", ip)
    print("City:", location_data.get("city"))
    print("Region:", location_data.get("region"))
    print("Country:", location_data.get("country"))
    print("Location (Lat,Long):", location_data.get("loc"))
    print("ISP / Org:", location_data.get("org"))

if __name__ == "__main__":
    main()
