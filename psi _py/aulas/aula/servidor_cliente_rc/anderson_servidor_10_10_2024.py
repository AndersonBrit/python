import pyscreenshot as ImageGrab
import socket
import cv2
import numpy as np
import time
import traceback
import threading

# Função que lida com o envio das capturas de tela para o cliente
def handle_client(client_socket, client_address):
    print(f"Conexão estabelecida com {client_address}")
    try:
        while True:
            # Captura a tela usando pyscreenshot
            screenshot = ImageGrab.grab()

            # Converte a imagem para um array numpy
            screenshot_np = np.array(screenshot)

            # Converte de RGB para BGR (OpenCV usa BGR)
            screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

            # Redimensiona a imagem para 680x480 usando interpolação para melhor qualidade
            screenshot_bgr_resized = cv2.resize(screenshot_bgr, (1024, 768), interpolation=cv2.INTER_AREA)

            # Comprime a imagem para o formato JPEG com alta qualidade (por exemplo, 90 em vez de 80)
            ret, jpeg_image = cv2.imencode('.jpg', screenshot_bgr_resized, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

            if not ret:
                print("Falha ao codificar a imagem.")
                continue

            # Converte o buffer da imagem para bytes
            image_bytes = jpeg_image.tobytes()

            # Envia o tamanho da imagem primeiro (8 bytes, big-endian)
            client_socket.send(len(image_bytes).to_bytes(8, byteorder='big'))

            # Envia a imagem em pacotes de 1024 bytes
            client_socket.sendall(image_bytes)

            # Pausa entre capturas (ajustável para controlar o "frame rate")
            time.sleep(0.05)  # 50ms para ~20fps

    except (ConnectionResetError, BrokenPipeError):
        print(f"Conexão com {client_address} encerrada.")
    except Exception as e:
        print(f"Erro com {client_address}: {e}")
        traceback.print_exc()
    finally:
        # Fechar o socket do cliente
        client_socket.close()
        print(f"Cliente {client_address} desconectado.")

# Configuração do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5001))
server_socket.listen(5)

print("Aguardando conexões...")

while True:
    try:
        # Aceitar uma nova conexão
        client_socket, client_address = server_socket.accept()

        # Criar uma nova thread para lidar com o cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))

        # Iniciar a thread
        client_thread.start()

    except Exception as e:
        print(f"Erro no servidor: {e}")
        traceback.print_exc()

# Fechar o servidor (se sair do loop principal)
server_socket.close()
