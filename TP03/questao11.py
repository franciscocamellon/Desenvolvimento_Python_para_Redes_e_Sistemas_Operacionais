# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 11                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_11.py                                   *
***************************************************************************/
"""
import socket

class Questao_11():
    """ This is a TCP server program. """

    def __init__(self):
        """ Constructor """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_host = socket.gethostname()
        self.door = 8881
        self.server_socket.bind((self.server_host, self.door))
        self.server_socket.listen()
        print('Servidor de nome {} esperando conexão na porta {}'.format(self.server_host, self.door))

        while True:
            # Aceita alguma conexão
            (socket_cliente, addr) = self.server_socket.accept()
            print("Conectado a:", str(addr))
            msg = socket_cliente.recv(1024)
            # Decodifica mensagem em ASCII
            print (msg.decode('ascii'))
            socket_cliente.close()



Questao_11()