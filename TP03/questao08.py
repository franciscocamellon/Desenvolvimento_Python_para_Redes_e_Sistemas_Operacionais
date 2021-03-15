# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 08                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_08.py                                   *
***************************************************************************/
"""
import socket
import time
import pickle


class Questao_10():
    """ This is a UDP client program. """

    def __init__(self):
        """ Constructor """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_host = socket.gethostname()
        self.door = 9991
        
        try:
            self.client_socket.connect((self.client_host, self.door))
            msg = ''
            print('{:>8}'.format('%CPU')+'{:>8}'.format('%MEM'))
            for i in range(10):
                # Envia mensagem vazia apenas para indicar a requisição
                s.send(msg.encode('ascii'))
                bytes = s.recv(1024)
                # Converte os bytes para lista
                lista = pickle.loads(bytes)
                self.imprime(lista)
                time.sleep(2)
            msg = 'fim'
            s.send(msg.encode('ascii'))
        except Exception as erro:
            print(str(erro))

        # Fecha o socket
        s.close()

        input("Pressione qualquer tecla para sair...")
    
    def imprime(self, l):
      texto = ''
      for i in l:
         texto = texto + '{:>8.2f}'.format(i)
      print(texto) 


Questao_10()
