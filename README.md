# Iron Gate
A network analysis program written in Python. 

Initial push: 25.12.2018
Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

Link to repository: [https://github.com/SebastjanLeskovar/iron_gate](https://github.com/SebastjanLeskovar/iron_gate)

## Getting Started

### Prerequisites

As of version V1.0, the following prerequisites are necessary to run this program:
- Python 3.x

The program utilizes the following standard libraries: os, queue, requests, socket, sys, uuid, urllib.error and urllib.request. 

### Installation

1. Click the green button 'Clone or download' on the right, and 'Download ZIP'.

2. Extract the ZIP file to your computer.

### How to use

Use Command Prompt to navigate to the root of the unziped folder (e.g., cd ...\iron_gate). Launch the program with the folowing command:

```bash
py iron_gate.py
```

Upon starting the program, you will be presented with seven options: 

1. Scan open ports on a server, website or IP address.

This operation will show open ports on any server, website or other IP address. On the next step, the program will ask the user to usert chosen the website or IP address. The input format should be 'www.example.com' or '137.74.187.104'.

2. Scan open ports on localhost.

The same operation as above, only the port scan is performed on the user's system. 

3. Send GET request.

Send a GET request to any website. The program will display the HTTP response code. It will also check if any redirects to the website are set. 

4. Request response header.

The program will send a HEAD request to the selected website and display the response header. 

5. Show Windows IP and MAC addresses.

[to be updated]

6. Show public IP.

[to be updated]

7. Exit.

Exits the program. You can also exit the program at any time by pressing keys Ctrl + C.


#### config.json

You can configure the variables "number_threads" and "number_jobs" in file "config.py".

The variable "number_jobs" will take into account how many ports would you like to scan, starting at 1. The total number of ports is 65.535 while the first 1024 ports are being reserved for privileged services and designed as well-known ports.

Caution: scanning a higher number of ports will take longer; scanning 2500 ports took approx. 11 seconds and 5000 ports took approx. 24 seconds on a home PC.
The default values are 100 for "number_threads" and 1024 for "number_jobs". 

## Versioning

* Implementation of GUI.

### V6.0

* Option to prepare a full network analysis report.
* The report should be exported to PDF format. 

### V5.0

* Implementation of resources discovery.

### V4.5

* Re-structure the program (move data input to a different file in 'src').
* Update the 'README.md' file.

### V4.0

* Option to obtain the public IP of the host.
* Option to obtain the Windows IP and MAC addresses of the host.

### V3.0

* Option to send a GET reguest.
* Obtaining Header information from a request. 

### V2.0

* Implementation of UI.

### V1.0

* Creation of file port_scanner.py to find all open ports.

## Bugs and Issues

Spoted: 01.01.2019
Description: When running function 'host_input' after previously entering wrong address and selecting 'yes' afterwards, this function is run three times.
Level: Error 

Spotted: 25.12.2018
Description: spoted in file "port_scanner.py", in function check_ports(). The port scanning does not stop when Ctrl+C is pressed.
It seems it is a common issue with Python threading. 
Level: Error

## Author

Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
