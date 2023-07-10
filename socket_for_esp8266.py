import socket
from flask import Flask
import time

host = '0.0.0.0'  # Tüm ip adreslerinden veri kabul eder
port = 8080
data = '0'
# Soket oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print(f"Port {port} dinleniyor...")

app = Flask(__name__)

hareket_bilgisi = "Hareket bilgisi yok."

@app.route('/password/hareketbilgisi', methods=['GET'])
def hareketBilgisi():
	conn, addr = s.accept()
	
	data = conn.recv(1024).decode('utf-8')
	conn.close()

	if data == "1":
		return "Hareket Algılandı!!" + data
	elif data == "0":
		return "Hareket Algılanmadı" + data
	else:
		return "Hareket bilgisi yok" + str(data)


if __name__ == '__main__':
    app.run(port=8081)	
