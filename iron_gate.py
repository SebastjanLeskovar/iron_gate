import re
import requests
import os
import sys
import socket
import urllib.request
import urllib.error
from src import port_scan, request_operations, host_system

class UI:
    '''UI menu for the user to define operations.'''

    '''Instructions'''

    instructions_1 = "==== IRON GATE ====\n \
    What would you like to do?\n \
    --- Analyse websites ---\n \
    1. Scan open ports.\n \
    2. Send GET request.\n \
    3. Request response header.\n \
    --- Own system operations ---\n \
    4. Scan open ports on localhost.\n \
    5. Show Windows IP and MAC addresses.\n \
    6. Show public IP.\n \
    7. Exit."

    option_1 = "Please enter a website you would like to scan. The input should contain the complete URL as in 'http://www.example.com'. You can cancel this operation with 'Ctrl+C' anytime." 

    option_2 = "Please enter a website you would like to send a GET request to. The input should contain the complete URL as in 'http://www.example.com'. You can cancel this operation with 'Ctrl+C' anytime."

    option_3 = "Please enter a website from which would you like to request a response header. The input should contain the complete URL as in 'http://www.example.com'. You can cancel this operation with 'Ctrl+C' anytime."

    def main_menu(self):
        
        clear = lambda: os.system('cls')
        clear()

        print(self.instructions_1)

        while True: 
            input_1 = input("Please enter a number from 1 to 7: ")

            if input_1 == "1":
                self.website_input(self.option_1)
                scan = port_scan.PortScan()
                scan.main(self.stripped_selected_host, self.stripped_selected_host_ip)
                break

            elif input_1 == "2":
                self.website_input(self.option_2)
                request = request_operations.RequestOperations()
                request.return_code(self.selected_website)
                break

            elif input_1 == "3":
                self.website_input(self.option_3)
                request = request_operations.RequestOperations()
                request.header_information(self.selected_website)
                break

            elif input_1 == "4":
                host = "localhost"
                host_ip = "127.0.0.1"
                scan = port_scan.PortScan()
                scan.main(host, host_ip)
                break

            elif input_1 == '5':
                h = host_system.HostSystem()
                h.get_windows_ip()
                h.get_mac()
                break

            elif input_1 == '6':
                p = host_system.HostSystem()
                p.get_public_ip()
                break

            elif input_1 == "7":
                print("The program was closed.")
                sys.exit()

            else:
                print("ERROR: Wrong input.")

    def website_input(self, option):
        '''Function to enter the host name.'''
        # TODO: Enable input of an IP address, not only website. 
        
        print(option)

        while True:
            user_input = input("Website: ")

            if self.check_url_input(user_input) == True:

                if self.check_website_exists(user_input) == True:

                    if user_input.endswith('/'):
                        user_input = user_input[:-1]

                    self.selected_website = user_input
                    self.stripped_selected_host = user_input.replace('https://', '').replace('http://', '')
                    
                    try:
                        self.stripped_selected_host_ip = socket.gethostbyname(self.stripped_selected_host)
                        break
                    except socket.gaierror as error:
                        print("ERROR: ", error)




    def check_url_input(self, input):
        '''Check if the user's input contains a complete URL.'''
        
        if input.startswith(('http://', 'https://')):
            return True
        else:
            print("Please enter a website starting with 'http://' or 'https://.'")
            return False

    def check_website_exists(self, input):
        '''Check if the entered website exists.'''

        try:
            urllib.request.urlopen(input)
            return True
        except urllib.error.HTTPError as error:
            print("ERROR: ", error)
            return False
        except urllib.error.URLError as error:
            print("ERROR: ", error)
            return False


if __name__ == '__main__':
    try:
        auto_start = UI()
        auto_start.main_menu()
    except KeyboardInterrupt:
        print("\nThe program was closed by user.")
