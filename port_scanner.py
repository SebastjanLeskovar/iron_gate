import os
import socket
import threading
import time
import config
import sys
import queue
import subprocess

class port_scanner:
    '''A class to seach for open ports.'''

    lock = threading.Lock() # Prevent double modification of shared variables.
    queue = queue.Queue()

    open_ports_list = []

    def server_input(self):
        '''Function to enter server name. It also checks if the server input is valid.'''
        self.server = input("Please enter website, server or IP address (format: 'www.hackthissite.org'): ")

        try:    # Check if server input is valid.
            self.server_IP = socket.gethostbyname(self.server)  # Get server IP
        except socket.gaierror:
            print("You did not enter a website, server or IP address.")
            sys.exit()
        
    def main(self):
        '''The main function for this class.'''

        clear = lambda: os.system('cls')
        clear()
        
        print("==== IRON GATE PROGRAM ====")

        self.server_input()

        print("---- Scanning server '%s' (IP: %s) ----." % (self.server, self.server_IP))
        
        start_time = time.time()    # Start time

        for _ in range(config.number_threads):
            thread = threading.Thread(target=self.threader)
            thread.daemon = True
            thread.start()

        for worker in range(1, config.number_jobs + 1):
            self.queue.put(worker)

        self.queue.join()    # Wait for thread to end

        total_time = round((time.time() - start_time), 2)

        print("---- Scan completed. ----")  # Finish info
        print("Entire scan took %s seconds." % total_time)  # Time spent info
        print("The following ports are open: %s." % self.open_ports_list)

    def check_ports(self, port):
        '''Check for open ports.'''
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        try:
            con = s.connect((self.server_IP, port))
            with self.lock:
                self.open_ports_list.append(port)
                print("Port", port, "is open.")
            con.close()
        except KeyboardInterrupt:
            print("Operation cancelled with Ctrl+C.")
            sys.exit()
        except:
            print("Port", port, "is closed.")

    def threader(self):
        '''Threader function.'''
        while True:
            worker = self.queue.get()   # Get the worker from queue
            self.check_ports(worker)    # Run the worker on port scanner
            self.queue.task_done()      # Complete the job


scan = port_scanner()
scan.main()