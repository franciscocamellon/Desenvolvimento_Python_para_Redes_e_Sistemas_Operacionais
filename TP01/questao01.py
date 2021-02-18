# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 01                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_01.py                                   *
***************************************************************************/
"""

import os


class Questao_01():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.user = ''
        self.username = ''

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """
        if hasattr(os, 'getlogin'):
            try:
                self.user = os.getlogin()
                if self.user:
                    return self.user
            except OSError:
                pass
        if hasattr(os, 'getuid'):
            try:
                self.user = os.getuid()
                if self.user:
                    return self.user
            except OSError:
                pass
        self.username = os.environ.get("USERNAME")
        if self.username:
            return self.username
        return None

    def print_result(self):
        """ This is a printer! It prints. """
        self.process_data()
        print('===' * 25, 'Questão 01'.center(75), '===' * 25, sep='\n')
        print('Nome do usuário logado: {}'.format(self.user if self.user else self.username),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_01().print_result()
