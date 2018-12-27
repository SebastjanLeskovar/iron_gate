# Iron Gate
A Python program for port scanning.

Initial push: 25.12.2018
Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

Link to repository: [https://github.com/SebastjanLeskovar/iron_gate](https://github.com/SebastjanLeskovar/iron_gate)

## Getting Started

### Prerequisites

As of version V1.0, the following prerequisites are necessary to run this program:
- Python 3.x

Please check the 'requirements.txt' file for an up-to-date list of prerequisites.

### Installation

1. Click the green button 'Clone or download' on the right, and 'Download ZIP'.

2. Extract the ZIP file to your computer.

### How to use

1. Use Command Prompt to navigate to the root of the unziped folder (e.g., cd ...\iron_gate). Launch the program with the folowing command:

```bash
py iron_gate.py
```

2. You can configure the variables "number_threads" and "number_jobs" in file "config.py".

The variable "number_jobs" will take into account how many ports would you like to scan, starting at 1. The total number of ports is 65.535 while the first 1024 ports are being reserved for privileged services and designed as well-known ports.

Caution: scanning a higher number of ports will take longer; scanning 2500 ports took approx. 11 seconds and 5000 ports took approx. 24 seconds on a home PC.
The default values are 100 for "number_threads" and 1024 for "number_jobs". 

3. Upon starting the program, you will be presented three options: 
- Scan any server, website or IP address. 
Please insert the website in the following form: "www.example.com", e.g. "www.hackthissite.org". 
If your input for was invalid, the program will close. 

- Scan your computer.
In this case, the program will scan open ports on 'localhost', thus IP address being 127.0.0.1. 
- Exit the scan.

## Versioning

### V2.0

* Implementation of UI.

### V1.0

* Creation of file port_scanner.py to find all open ports.

## Bugs and Issues

Spotted: 25.12.2018
Description: spoted in file "port_scanner.py", in function check_ports(). The port scanning does not stop when Ctrl+C is pressed.
It seems it is a common issue with Pytohn threading. 

## Author

Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
