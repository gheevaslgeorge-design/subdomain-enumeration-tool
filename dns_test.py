import socket 
domain = "youtube.com" 
try: 
   ip = socket.gethostbyname(domain) 
   print(f"IP address of {domain}: {ip}") 
except socket.gaierror: 
  print(f"Could not resolve {domain}") 