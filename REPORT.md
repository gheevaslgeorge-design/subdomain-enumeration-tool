Subdomain Enumeration Tool (Python & Threading)

1. Project Overview and Objective

This project, developed as part of the Inlighn Tech curriculum, implements an automated Python script to perform subdomain enumeration. This is a crucial step in the reconnaissance phase of cybersecurity assessments.

Objective: To efficiently identify active subdomains of a given target domain by testing a list of potential names concurrently using multithreading, incorporating advanced filtering techniques to handle evasive server responses.

Key Concepts Demonstrated:

Python Automation: Using Python for cybersecurity tasks.

Multithreading: Optimizing tool speed by checking multiple targets simultaneously.

Networking Basics: Utilizing HTTP requests to verify host accessibility.

Advanced Reconnaissance: Implementing Content-Length Filtering to accurately distinguish between active subdomains and generic server error responses (like Wildcard DNS entries).

Thread Synchronization: Implementing a lock (threading.Lock) to safely manage shared resources (the output file).

2. Technical Implementation Details

The script is contained in subdomain_enum.py and uses the requests and threading libraries.

Files Required

File Name                                        Purpose

subdomain_enum.py            The main script containing the enumeration and advanced filtering logic.

subdomains.txt                Input file containing a list of potential subdomain prefixes .

discovered_subdomains.txt     Output file where all active, unique URLs are logged.

Advanced Filtering (Content-Length Logic)

To overcome a common defensive measure (Wildcard DNS), the script uses a two-step approach in the run_enumeration function:

Baseline Establishment: The script first checks the main domain (http://<domain>) to determine the default response size (e.g., 4958 bytes for testphp.vulnweb.com). This size represents the typical error/redirect page.

Filtering: The check_subdomain function then compares the response size of every tested subdomain against this baseline. Only if the response size is significantly different (outside a 90% to 110% tolerance band) is the subdomain considered unique and recorded as discovered.

3. Usage Guide

To run the tool, you must provide the target domain as a command-line argument.

Usage Command:

python subdomain_enum.py <target_domain>


Example Run (Console Output):

--- Establishing baseline response size for testphp.vulnweb.com ---
--- Baseline established: 4958 bytes ---
--- Starting Subdomain Enumeration for testphp.vulnweb.com ---
Checking 19 potential subdomains concurrently...
...
--- Enumeration Complete ---
Results saved to discovered_subdomains.txt.


4. Final Project Summary 

The Project is Complete and Functional. For the target testphp.vulnweb.com and the provided wordlist, the final result was that no unique subdomains were discovered. This outcome is correct and demonstrates the effectiveness of the Content-Length filter, confirming the target server uses robust error handling that makes simple subdomain testing ineffective. The script successfully filtered out all non-existent hosts.