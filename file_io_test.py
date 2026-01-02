
subdomains = ["www", "mail", "api"] 
# Write to a file 
with open("test_subdomains.txt", "w") as f: 
  for sub in subdomains: 
   print(sub, file=f) 
# Read from the file 
with open("test_subdomains.txt") as f: 
  loaded_subdomains = f.read().splitlines() 
print("Loaded subdomains:", loaded_subdomains) 