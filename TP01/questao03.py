# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 03                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_03.py                                   *
***************************************************************************/
"""

import os
import sys


class Questao_03():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.platform = sys.platform
        self.os_name = os.name
        self.pid = ''

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """
        if self.platform.startswith('linux'):
            self.pid = os.getgid()
        elif self.platform.startswith('win32'):
            self.pid = os.getpid()

    def print_result(self):
        """ This is a printer! It prints. """
        self.process_data()
        print('===' * 25, 'Questão 03'.center(75), '===' * 25, sep='\n')
        print('Sistema operacional: {}'.format('Windows' if self.platform == 'win32' else 'Linux'),
              'PID deste processo: {}'.format(self.pid),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_03().print_result()
