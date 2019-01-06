import os
import sys
import socket
from src import port_scanner, request_operations, host

class UI:
    '''UI menu for the user to define operations.'''
    
    def main_menu(self):
        
        clear = lambda: os.system('cls')
        clear()
    
        print("==== IRON GATE ====")

        while True:
            input_1 = input("What would you like to do?\n1. Scan open ports on a server, website or IP address.\n2. Scan open ports on localhost.\n3. Send GET request.\n4. Request response header.\n5. Show Windows IP and MAC addresses.\n6. Show public IP.\n7. Exit.\nPlease enter 1, 2, 3, 4, 5, 6 or 7: ")

            if input_1 == "1":
                self.host_input()

                scan = port_scanner.PortScan()
                scan.main(self.chosen_host, self.chosen_host_ip)
                break

            elif input_1 == "2":
                self.chosen_host = "localhost"
                self.chosen_host_ip = "127.0.0.1"
                
                scan = port_scanner.PortScan()
                scan.main(self.chosen_host, self.chosen_host_ip)
                break

            elif input_1 == "3":
                self.website_input()
                request = request_operations.RequestOperations()
                request.return_code(self.chosen_website)
                break

            elif input_1 == "4":
                self.website_input()
                request = request_operations.RequestOperations()
                request.header_information(self.chosen_website)
                break

            elif input_1 == '5':
                
                h = host.Host()
                h.get_windows_ip()
                h.get_mac()
                break

            elif input_1 == '6':
                public_ip = host.Host()
                public_ip.get_public_ip()
                break

            elif input_1 == "7":
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
                    input_2 = input("Please enter 'yes' to restart scanning or 'no' to cancel: ")

                    if input_2 in ("yes", "y", "1"):
                        self.host_input()
                        break
                    elif input_2 in ('no', 'n', '2'):
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


auto_start = UI()
auto_start.main_menu()

# TODO: Start the program by using the standard formulation 'if __name__ == '__main__'.
