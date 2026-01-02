
domain = "example.com" 
subdomains = ["www", "mail", "test"] 
for sub in subdomains: 
 url = f"http://{sub}.{domain}" 
print(f"Generated URL: {url}")  