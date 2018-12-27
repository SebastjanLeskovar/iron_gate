import port_scanner
import os
import sys
import socket

class ui:
    '''UI menu for the user to define operations.'''
    
    def main_menu(self):
        
        clear = lambda: os.system('cls')
        clear()
    
        print("==== IRON GATE PROGRAM ====")

        while True:
            input_1 = input("What would you like to do?\n1. Scan open ports on a server, website or IP address.\n2. Scan open ports on localhost.\n3. Exit.\nPlease enter 1, 2 or 3: ")

            if input_1 not in ("1", "2", "3"):
                clear()
                print("Wrong input.")
                continue
            else:
                break

        if input_1 == "1":
            
            self.host_input()
            
            scan = port_scanner.port_scan()
            scan.main(self.chosen_host, self.chosen_host_ip)

        if input_1 == "2":
            self.chosen_host = "localhost"
            self.chosen_host_ip = "127.0.0.1"
            
            scan = port_scanner.port_scan()
            scan.main(self.chosen_host, self.chosen_host_ip)

        if input_1 == "3":
            print("The program was closed.")
            sys.exit()

    def host_input(self):
            '''Function to enter the host name. It also checks if the host input is valid.'''
            
            self.chosen_host = input("Please enter a website, server or IP address you would like to scan. The format should be 'www.hackthissite.org' or '137.74.187.104'.\nWhat would you like to scan? ")

            try:                                                                # Check if server input is valid.
                self.chosen_host_ip = socket.gethostbyname(self.chosen_host)    # Get server IP
            except socket.gaierror:
                print("ERROR: You did not enter a proper a website, server or IP address.\nWould you like to start the scan again?")
                
                while True:
                    self.input_2 = input("Please enter 'yes' to restart scanning or 'no' to cancel: ")

                    if self.input_2.lower() not in ("yes", "y", "1", "no", "n", "2"):
                        print("Wrong input.")
                        continue
                    else:
                        break                    

                if (self.input_2 == "yes") or (self.input_2 == "y") or (self.input_2 == "1"):
                    self.host_input()

                else:
                    print("The program was cancelled.")
                    sys.exit()

start = ui()
start.main_menu()
