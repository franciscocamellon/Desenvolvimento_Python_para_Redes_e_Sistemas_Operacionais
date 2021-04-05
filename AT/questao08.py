# -*- coding: utf-8 -*-
"""
/****************************** ASSESSMENT *********************************
*    Questao 08                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_08.py                                   *
***************************************************************************/
"""
import psutil
import time
from psutil._common import bytes2human

class Sequencial():
    vector_A = [10,15]
    vector_B = []

    def fatorial(n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)

    for item in vector_A:
        vector_B.append(fatorial(item))

    print(vector_B)

class Threading():

class Multiprocessing():