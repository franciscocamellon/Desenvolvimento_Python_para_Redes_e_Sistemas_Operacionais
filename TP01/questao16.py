# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 16                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_16.py                                   *
***************************************************************************/
"""

import os
import psutil
import time


class Questao_16():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.error = ''
        self.times_cpu = list()
        print('===' * 25, 'Questão 16'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass
        

    def process_data(self):
        """ This function process the input data from init_class. """
        self.times_cpu = psutil.cpu_times_percent(interval=0.1, percpu=True)

    def print_result(self):
        """ This is a printer! It prints. """
        
        if self.error:
            print(self.error,
                  '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep='\n')
        else:
            print('Número de núcleos: {}\n'.format(len(self.times_cpu)))
            for core in range(len(self.times_cpu)):
                print('{}Núcleo {}: user={} system={} idle={}'.format(
                    ' '*3,
                    core,
                    self.times_cpu[core][0],
                    self.times_cpu[core][1],
                    self.times_cpu[core][2]))
            print('---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep='\n')


Questao_16().print_result()
