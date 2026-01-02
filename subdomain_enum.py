import requests
import threading
import sys
import os


file_lock = threading.Lock() 

BASELINE_SIZE = 0

def load_subdomains(filename="subdomains.txt"):
    """
    Loads a list of potential subdomains from the specified file.
    """
    try:
        with open(filename, 'r') as f:
           
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: The input file '{filename}' was not found.")
        print("Please create 'subdomains.txt' with one potential subdomain per line.")
        return []


def check_subdomain(subdomain, target_domain, output_file="discovered_subdomains.txt"):
    """
    Constructs the URL and checks for an active subdomain using Content-Length filtering.
    
    This logic filters out generic responses where non-existent subdomains redirect 
    or proxy back to the main domain, resulting in identical page content.
    """
   
    url = f"http://{subdomain}.{target_domain}"
    
    try:
  
        response = requests.get(url, timeout=5, allow_redirects=True)

        response_size = len(response.content)
        
        
        if BASELINE_SIZE == 0 or not (0.9 < (response_size / BASELINE_SIZE) < 1.1):
            
            
            print(f"[+] DISCOVERED (Unique Size: {response_size} bytes): {url}")

            with file_lock:
                with open(output_file, 'a') as f:
                    f.write(url + '\n')
            
       
    except requests.exceptions.RequestException:
       
        pass 
        

def run_enumeration(domain, input_file="subdomains.txt", output_file="discovered_subdomains.txt"):
    """
    Orchestrates the enumeration process using multiple threads, including a baseline check.
    """
    global BASELINE_SIZE
    
    potential_subdomains = load_subdomains(input_file)
    if not potential_subdomains:
        return

    
    print(f"--- Establishing baseline response size for {domain} ---")
    try:
        
        main_url = f"http://{domain}"
        response = requests.get(main_url, timeout=5)
        BASELINE_SIZE = len(response.content)
        print(f"--- Baseline established: {BASELINE_SIZE} bytes ---")
    except requests.exceptions.RequestException:
        print("Warning: Could not establish baseline size. Scanning without content filtering.")
        BASELINE_SIZE = 1

    open(output_file, 'w').close() 
    
    print(f"--- Starting Subdomain Enumeration for {domain} ---")
    print(f"Checking {len(potential_subdomains)} potential subdomains concurrently...")
    
    threads = []
    
   
    for subdomain in potential_subdomains:
        t = threading.Thread(
            target=check_subdomain, 
            args=(subdomain, domain, output_file)
        )
        threads.append(t)
        t.start() # Start the concurrent check
        

    for t in threads:
        t.join() 
        
    print("\n--- Enumeration Complete ---")
    print(f"Results saved to {output_file}.")


if __name__ == "__main__":
 
    try:
        import requests
    except ImportError:
        print("The 'requests' library is required. Please run: pip install requests")
        sys.exit(1)
        
  
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(sys.argv[0])} <target_domain>")
        print("Example: python subdomain_enum.py example.com")
        sys.exit(1)
        
    target_domain = sys.argv[1]
    run_enumeration(target_domain)
