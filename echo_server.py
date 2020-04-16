import socket
import ultrasonic_sensor as sensor
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            encoded_data = conn.recv(1024)
            choice=encoded_data.decode()
            if choice.isdigit():
                if choice=='5':
                    conn.close()
                    break
                thrown, thrown_string = sensor.sensor_choice(int (choice))
                print (thrown)
            if not encoded_data:
                s.listen(1)
                conn, addr = s.accept()
                continue
            conn.sendall(thrown_string.encode())
        conn.close()
