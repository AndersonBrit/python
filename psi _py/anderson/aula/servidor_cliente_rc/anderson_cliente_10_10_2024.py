import socket
import cv2
import numpy as np

# Configuração do socket do cliente
server_ip = '192.168.1.72'  # Coloque o IP do servidor
server_port = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    try:
        # Recebe os 8 bytes que representam o tamanho do arquivo da imagem (em binário)
        file_size_bytes = client_socket.recv(8)

        # Verifica se o tamanho foi recebido corretamente
        if not file_size_bytes:
            print("Nenhum tamanho de arquivo recebido. Fechando conexão.")
            break

        # Converte os 8 bytes recebidos para um número inteiro (representando o tamanho da imagem)
        file_size = int.from_bytes(file_size_bytes, byteorder='big')
        print(f"Tamanho da imagem recebido: {file_size} bytes")

        # Receber a imagem
        received_bytes = 0
        image_data = b''
        while received_bytes < file_size:
            packet = client_socket.recv(1024)

            if not packet:
                print("Nenhum dado recebido. Fechando conexão.")
                break

            image_data += packet
            received_bytes += len(packet)

        if received_bytes < file_size:
            print("Imagem incompleta recebida. Abortando.")
            break

        # Converte os bytes da imagem para um numpy array
        nparr = np.frombuffer(image_data, np.uint8)

        # Decodifica a imagem usando OpenCV
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Verifica se a imagem foi decodificada corretamente
        if image is None:
            print("Falha ao decodificar a imagem. Fechando conexão.")
            break

        # Exibe a imagem
        cv2.imshow('Tela Recebida', image)

        # Pressione 'q' para fechar a janela
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"Erro: {e}")
        break

# Fechar a conexão do cliente
client_socket.close()
cv2.destroyAllWindows()
