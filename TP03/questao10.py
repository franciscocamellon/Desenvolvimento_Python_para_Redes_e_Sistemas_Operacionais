# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 10                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_10.py                                   *
***************************************************************************/
"""


import socket

class Questao_10():
    """ This is a TCP server program. """

    def __init__(self):
        """ Constructor """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_host = socket.gethostname()
        self.door = 8881
        # self.server_socket.bind((self.server_host, self.door))
        # self.server_socket.listen()
        # print('Servidor de nome {} esperando conexão na porta {}'.format(self.server_host, self.door))

        try:
            # Tenta se conectar ao servidor
            self.client_socket.connect((self.client_host, self.door))
            msg = "Ola servidor!\n"
            # Envia mensagem codificada em bytes ao servidor
            self.client_socket.send(msg.encode('ascii'))
            # Fecha conexão com o servidor
            self.client_socket.close()
        except Exception as erro:
            print(str(erro))



Questao_10()
