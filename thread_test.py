# Basic multithreading example 
import threading 
import time 
def task(name): 
  print(f"Thread {name} starting") 
  time.sleep(1)  # Simulate work 
  print(f"Thread {name} finished") 
threads = [] 
for i in range(3): 
 t = threading.Thread(target=task, args=(i,)) 
t.start() 
threads.append(t) 
for t in threads: 
 t.join() 
print("All threads done")