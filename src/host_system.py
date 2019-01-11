import socket
import uuid
import urllib.request
import urllib.error

class HostSystem:
    '''Obtain the public IP, Windows IP and MAC addresses.'''

    def get_windows_ip(self):
        '''Obtain the Windows host IP address.'''

        windows_ip = socket.gethostbyname(socket.gethostname())
        print("Your Windows IP address is %s." % windows_ip)

    def get_mac(self):
        '''Obtain the Windows MAC address.'''

        mac_address = uuid.getnode()
        mac_address = ':'.join(('%012X' % mac_address)[i:i+2] for i in range(0, 12, 2))
        
        print("Your Windows MAC address is %s." % mac_address)

    def get_public_ip(self):
        '''Obtain the public IP address.'''

        try:
            public_ip = urllib.request.urlopen('http://ip.42.pl/raw').read()
        except urllib.error.HTTPError as error:
            print("The following error occured: ", error)
        except urllib.error.URLError as error:
            print("The following error occured: ", error)

        if public_ip:
            print("Your public IP address is: %s." % public_ip)
        else:
            print("ERROR: Your public IP address was not found.")

