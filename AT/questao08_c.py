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

import multiprocessing
import time
import random

vector_B = []

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calc_fatorial(q1, q2):
    factorial_list = q1.get()
    vector = []
    for item in factorial_list:
        factorial = fatorial(item)
        vector.append(factorial)
    q2.put(vector)


if __name__ == "__main__":

    vector_size = int(input("Entre com o tamanho do vetor(0-20): "))

    vector_A = []
    for i in range(vector_size):
        vector_A.append(random.randint(0, 20))

    process_number = 4

    queue_in = multiprocessing.Queue()
    queue_out = multiprocessing.Queue()

    lista_proc = []
    for i in range(process_number):
        start = i * int(vector_size/process_number)
        end = (i + 1) * int(vector_size/process_number)
        queue_in.put(vector_A[start:end])
        m = multiprocessing.Process(target=calc_fatorial, args=(queue_in,
                                                           queue_out))
        m.start()
        lista_proc.append(m)

    for m in lista_proc:
        m.join()

    for i in range(0, process_number):
        for item in queue_out.get():
            vector_B.append(item)

    print(vector_B)

