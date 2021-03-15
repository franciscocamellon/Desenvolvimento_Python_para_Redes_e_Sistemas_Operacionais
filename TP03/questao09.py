# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 09                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_09.py                                   *
***************************************************************************/
"""
import socket
import psutil
import pickle


class Questao_09():
    """ This is a UDP server program. """

    def __init__(self):
        """ Constructor """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_host = socket.gethostname()
        self.door = 9991
        self.server_socket.bind((self.server_host, self.door))
        self.server_socket.listen()
        print('Servidor de nome {} esperando conexão na porta {}'.format(self.server_host, self.door))

        (socket_cliente, addr) = self.server_socket.accept()
        print("Conectado a:", str(addr))

        while True:
            # Recebe pedido do cliente:
            msg = socket_cliente.recv(4)
            if msg.decode('ascii') == 'fim':
                break
            # Gera a lista de resposta
            resposta = []
            resposta.append(psutil.cpu_percent())
            mem = psutil.virtual_memory()
            mem_percent = mem.used/mem.total
            resposta.append(mem_percent)
            # Prepara a lista para o envio
            bytes_resp = pickle.dumps(resposta)
            # Envia os dados
            socket_cliente.send(bytes_resp)

        # Fecha socket do servidor e cliente
        socket_cliente.close()
        self.server_socket.close()


Questao_09()
