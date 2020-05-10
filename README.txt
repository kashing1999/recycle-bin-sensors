1. Ensure that 'ultrasonic_sensor.py' and 'echo_server.py' are in the same folder, file path does not matter much
2. Programs have to be run with Python 3.+

3. Python files can be run as program, from Terminal (python3 'filepath'/'file name')
4. ultrasonic_sensor.py is the program used to test the sensors, will return true if sensor detects something passing in front; can be closed with a Keyboard Interrupt (Ctrl+C) (python3 'filepath'/ultrasonic_sensor.py)
5. Assuming not already running, can also be run from Terminal (python3 'filepath'/echo_server.py )
6. 'echo_client.py' can be run independently, for testing 'echo_server.py', though can be integrated to webserver for sensor-server communication

7. Ensure that 'ssh.sh' file is placed in this file path : '/home/pi' for connection to webserver; note that IP address and server name is variable to server, and must be changed accordingly
8. For scripts to run at boot copy from crontab_script.txt and paste into crontab editor
9. crontab editor can be accessed through Terminal, typing 'crontab -e'