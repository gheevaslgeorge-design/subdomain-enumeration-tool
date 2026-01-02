import dns.resolver

target_domain = "youtube.com"
record_type = ["A","AAAA","MX","TXT","SOA"]
resolver = dns.resolver.Resolver()
for record_type in record_type:
  try:
       answer = resolver.resolve(target_domain,record_type)
  except dns.resolver.NoAnswer:
       continue
  print(f"{record_type} records for {target_domain}")
  for data in answer:
      print(f"{data}")