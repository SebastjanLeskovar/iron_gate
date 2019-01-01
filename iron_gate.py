import os
import sys
import socket
from src import port_scanner, request_operations

class ui:
    '''UI menu for the user to define operations.'''
    
    def main_menu(self):
        
        clear = lambda: os.system('cls')
        clear()
    
        print("==== IRON GATE PROGRAM ====")

        while True:
            input_1 = input("What would you like to do?\n1. Scan open ports on a server, website or IP address.\n2. Scan open ports on localhost.\n3. Send GET request.\n4. Request response header.\n5. Exit.\nPlease enter 1, 2, 3, 4 or 5: ")

            if input_1 == "1":
                self.host_input()

                scan = port_scanner.port_scan()
                scan.main(self.chosen_host, self.chosen_host_ip)
                break

            elif input_1 == "2":
                self.chosen_host = "localhost"
                self.chosen_host_ip = "127.0.0.1"
                
                scan = port_scanner.port_scan()
                scan.main(self.chosen_host, self.chosen_host_ip)
                break

            elif input_1 == "3":
                self.website_input()
                request = request_operations.request_operations()
                request.return_code(self.chosen_website)
                break

            elif input_1 == "4":
                self.website_input()
                request = request_operations.request_operations()
                request.header_information(self.chosen_website)
                break
            
            elif input_1 == "5":
                print("The program was closed.")
                sys.exit()

            else:
                print("ERROR: Wrong input.")

    def host_input(self):
            '''Function to enter the host name. It also checks if the host input is valid.'''
            
            self.chosen_host = input("Please enter a website, server or IP address you would like to scan. The format should be 'www.hackthissite.org' or '137.74.187.104'.\nWhat would you like to scan? ")

            try:    # Check if server input is valid.
                self.chosen_host_ip = socket.gethostbyname(self.chosen_host)
            except socket.gaierror:
                print("ERROR: You did not enter a proper a website, server or IP address.\nWould you like to start the scan again?")
                
                while True:
                    self.input_2 = input("Please enter 'yes' to restart scanning or 'no' to cancel: ")

                    if self.input_2 in ("yes", "y", "1"):
                        self.host_input()
                        break
                    elif self.input_2 in ('no', 'n', '2'):
                        print("The program was cancelled.")
                        sys.exit()
                    else:
                        print("ERROR: Wrong input.")

    def website_input(self):
        '''Enter a website address to which you would like to send a request.'''

        while True:
            input_3 = input("Enter a website to send a request to. The format should be 'http://www.hackthissite.org' or '137.74.187.104'.\nAddress: ")

            if input_3.startswith(('http://www', 'https://www')):   # Check if input is in correct format.
                self.chosen_website = input_3
                break
            
            # TODO: In addition to the verification above, create another verification to check user's input.
            # TODO: Ask the user to add 'http://' or /http://www' automatically.

            else:
                print("ERROR: Your input did not start with 'htttp(s)://www'.\nWould you like to start the scan again?")

                while True:
                    input_4 = input("Please enter 'yes' to restart sending a request or 'no' to cancel: ")

                    if input_4 in ("yes", "y", "1"):
                        self.website_input()
                        break
                    elif input_4 in ('no', 'n', '2'):
                        print("The program was cancelled.")
                        sys.exit()
                    else:
                        print("ERROR: Wrong input.")


auto_start = ui()
auto_start.main_menu()
