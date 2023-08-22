import socket
from flask import Flask
import time

host = '0.0.0.0'  # Tüm ip adreslerinden veri kabul eder
port = 8080
data = '0'
"""
# Soket oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
"""
print(f"Port {port} listening...")

app = Flask(__name__)

hareket_bilgisi = "None movement info."

@app.route('/password/movementinfo', methods=['GET'])
def hareketBilgisi():
	# Soket oluştur
	time.sleep(2)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(1)

	conn, addr = s.accept()
	
	data = conn.recv(1024).decode('utf-8')
	conn.close()

	if data == "1":
		return str(data)
	elif data == "0":
		return str(data)
	else:
		return "No movement info" + str(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)	
