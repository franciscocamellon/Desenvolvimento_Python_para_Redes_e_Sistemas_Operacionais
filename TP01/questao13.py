# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 13                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_13.py                                   *
***************************************************************************/
"""

import os
import sys
import subprocess


class Questao_13():
    """
    This program creates a process with subprocess module and prints your PID.
    """

    def __init__(self):
        """ Constructor """
        self.platform = sys.platform
        self.os_name = os.name
        self.pid = ''
        print('===' * 25, 'Questão 13'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """
        if self.platform.startswith('linux'):
            self.pid = os.getgid()
        elif self.platform.startswith('win32'):
            process = subprocess.Popen("notepad")
            self.pid = process.pid

    def print_result(self):
        """ This is a printer! It prints. """

        print('Sistema operacional: {}'.format('Windows' if self.platform == 'win32' else 'Linux'),
              'PID deste processo: {}'.format(self.pid),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_13().print_result()
