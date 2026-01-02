# Test HTTP requests with requests library 
import requests 
url = "http://example.com" 
try: 
    response = requests.get(url) 
    print(f"Status code for {url}: {response.status_code}") 
except requests.ConnectionError: 
    print(f"Failed to connect to {url}") 