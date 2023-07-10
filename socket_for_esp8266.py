import socket


host = '0.0.0.0'  # Tüm ip adreslerinden veri kabul eder
port = 8080

# Soket oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print(f"Port {port} dinleniyor...")

while True:
    conn, addr = s.accept()
    print('Bağlantı:', addr)
    data = conn.recv(1024).decode('utf-8') # recv(1024) alacağı maksimum byte sayısını gösterir decode(utf-8) ise hangi türde karakter çözümlemesi yapacağını gösterir
    print('Gelen veri:', data)
    
    if data == '1':
        response = 'Hareket algılandı!'
    elif data == '0':
        response = 'Hareket yok!'
    else:
        response = 'Geçersiz veri!'
    
    # Sunucuya response yolla
    conn.sendall(response.encode('utf-8'))
    
    conn.close()

