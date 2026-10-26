import socket
import sys

SERVER_IP = "10.0.0.1"
SERVER_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3.0)

message = sys.argv[1] if len(sys.argv) > 1 else "EMERGENCY_ALERT: Evacuate!"

try:
    print(f"[*] Sending alert to {SERVER_IP}:{SERVER_PORT}...")
    sock.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

    # Await delivery confirmation
    ack_data, _ = sock.recvfrom(1024)
    print(f"[CONFIRMATION RECEIPT]: {ack_data.decode('utf-8')}")

except socket.timeout:
    print("[ERROR]: Delivery confirmation timed out!")
finally:
    sock.close()
