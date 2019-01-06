import requests

class RequestOperations:
    '''Send HTTP/1.1 requests.'''

    def return_code(self, website):
        '''Returns the return code from server hosting the selected website.'''
        
        req = requests.get(website)
        print("Status code: " + str(req.status_code))
        # TODO: Display additional information about the code. More info can be found at https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200. 

        if req.history:  # Check for possible redirect codes. 
            for x in req.history:
                print("Redirects found: ")
                print("\t" + "Code " + str(x.status_code) + " to " + x.url + ".")
        else:
            print("No redirects found.")

    def header_information(self, website):
        '''Returns the headers of a request to the selected website.'''

        req = requests.head(website)
        
        # print("Status code: " + str(req.status_code))

        print("Response headers:")
        for x in req.headers:
            print("\t" + x + ": " + req.headers[x])
