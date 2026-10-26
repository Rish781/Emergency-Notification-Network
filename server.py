import socket

SERVER_IP = "10.0.0.1"
SERVER_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print(f"[*] Emergency Server active on {SERVER_IP}:{SERVER_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode('utf-8')
    print(f"[RECEIVED from {addr}]: {message}")

    # Send delivery confirmation back to client
    ack_message = f"ACK: Emergency Alert Received ('{message}')"
    sock.sendto(ack_message.encode('utf-8'), addr)
