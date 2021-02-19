# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 06                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_06.py                                   *
***************************************************************************/
"""

import os
import errno


class Questao_06():
    """
    This program retrieves the file extension.
    """

    def __init__(self):
        """ Constructor """
        self.search_path = ''
        self.is_file, self.is_directory, self.error = '', '', ''
        self.file_name = 'questao06.py'
        self.file_path = '.\\'
        print('===' * 25, 'Questão 06'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        if os.path.exists(self.file_path):
            self.search_path = os.path.join(self.file_path, self.file_name)
            return self.search_path
        else:
            self.file_path = input(str('Digite o caminho de um arquivo: '))
            self.file_name = input('Digite o nome do arquivo: ')
            self.search_path = os.path.join(self.file_path, self.file_name)
            return self.search_path

    def process_data(self):
        """ This function process the input data from init_class. """
        if os.path.isfile(self.search_path):
            self.is_file = 'arquivo'
            self.file_extension = os.path.splitext(self.search_path)[1]
        elif os.path.isdir(self.search_path):
            self.is_directory = 'diretório'
        else:
            self.error = FileNotFoundError(errno.ENOENT, os.strerror(
                errno.ENOENT), os.path.basename(self.search_path))

    def print_result(self):
        """ This is a printer! It prints. """
        if self.error:
            print(self.error,
                  '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")
        else:
            print('\nA extensão do arquivo {}\n\t É {}!'.format(self.file_name,
                                                                self.file_extension),
                  '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_06().print_result()
