# server.py
import socket

# تنظیمات سرور
SERVER_HOST = '0.0.0.0'  # گوش دادن به همه آدرس‌های موجود
SERVER_PORT = 12345       # شماره پورت سرور

# ایجاد سوکت TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

# پذیرش اتصال کلاینت
client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}")

# دریافت و ارسال پیام‌ها
try:
    while True:
        # دریافت پیام از کلاینت
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            print("Client disconnected.")
            break
        print("Client:", message)
       
        # ارسال پاسخ به کلاینت
        response = input("You: ")
        client_socket.send(response.encode())
        if response.lower() == 'exit':
            print("Chat ended.")
            break
finally:
    # بستن سوکت‌ها
    client_socket.close()
    server_socket.close()

