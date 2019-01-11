import os
import queue
import socket
import sys
import subprocess
import threading
import time
import config

class PortScan:
    '''A class to seach for open ports.'''

    lock = threading.Lock() # Prevent double modification of shared variables.
    queue = queue.Queue()

    open_ports_list = []    # List of open ports

    def main(self, host, host_ip):
        '''The main function for this class.'''

        self.host_ip = host_ip

        print("---- Scanning server '%s' (IP: %s) ----" % (host, host_ip))
        
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
        print("The following ports are open: %s. \nEntire scan of %s ports took %s seconds." % (self.open_ports_list, config.number_jobs, total_time))

    def check_ports(self, port):
        '''Check for open ports.'''
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        try:
            con = s.connect((self.host_ip, port))
            with self.lock:
                self.open_ports_list.append(port)
                print("Port %s is open." % port)
            con.close()
        except KeyboardInterrupt:   # BUG: Keyboard interrupt occasionally not working.
            print("Operation cancelled with Ctrl+C.")
            sys.exit()
        except:
            pass
            # print("Port %s is closed." % port)

    def threader(self):
        '''Threader function.'''
        while True:
            worker = self.queue.get()   # Get the worker from queue
            self.check_ports(worker)    # Run the worker on port scanner
            self.queue.task_done()      # Complete the job
