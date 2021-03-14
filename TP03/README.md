# Desenvolvimento Python para Redes e Sistemas Operacionais

## Teste de Performance 03

Neste TP há questões discursivas e de implementação.

#### 1. O que é um processo cliente?

#### 2. O que é um processo servidor?

#### 3. A função socket() do módulo ‘socket’ de Python é responsável por criar um socket no processo tanto para protocolo TCP, quanto UDP. Como diferenciar se o socket a ser criado é TCP e UDP?

#### 4. Para sockets TCP, responda:

1. Que sequência de chamadas de funções em Python deve ser realizada pelo cliente? (Não precisa especificar os parâmetros)
1. Que sequência de chamadas de funções em Python deve ser realizada pelo servidor? (Não precisa especificar os parâmetros)
1. Quais destas funções são bloqueantes, isto é, o processo fica esperando?

#### 5. Para sockets UDP, responda:

1. Que sequência de chamadas de funções em Python deve ser realizada pelo cliente? (Não precisa especificar os parâmetros)
1. Que sequência de chamadas de funções em Python deve ser realizada pelo servidor? (Não precisa especificar os parâmetros)
1. Quais destas funções são bloqueantes, isto é, o processo fica esperando?

#### 6. Para que serve o comando _socket.bind()_?

#### 7. Em sockets Python, como é representado um endereço de um processo remoto?

#### 8. Crie um programa cliente que:

1. Conecte-se a um servidor via UDP de mesmo IP e porta 9991.
1. Peça ao servidor que envie a quantidade total e disponível de armazenamento do disco principal.
1. Receba e exiba a informação.

![gif](/gifs/questao08.gif)

[Código](https://github.com/franciscocamellon/Francisco_Camello_DR2_AT/questao_08.py)

#### 9. Associado à questão anterior, crie um programa servidor que:

1. Espere conexões UDP de processos na porta 9991.
1. Aguarde indefinidamente conexão de clientes.
1. Sirva cada cliente com a informação da quantidade total e disponível de armazenamento do disco principal (diretório corrente que o processo servidor está executando).

![gif](/gifs/questao09.gif)

[Código](https://github.com/franciscocamellon/Francisco_Camello_DR2_AT/questao_09.py)

#### 10. Crie um programa cliente que:

1. Conecte-se a um servidor via TCP de mesmo IP e porta 8881.
1. Envie ao servidor o nome de um arquivo para que ele transmita este arquivo para o cliente.
1. Receba o tamanho do arquivo.
1. Se o tamanho for válido, receba o arquivo. Caso contrário, avise ao usuário que o arquivo não foi encontrado.

![gif](/gifs/questao10.gif)

[Código](https://github.com/franciscocamellon/Francisco_Camello_DR2_AT/questao_10.py)

#### 11. Associado à questão anterior, crie um programa servidor que:

1. Espere conexões TCP de processos na porta 8881.
1. Aguarde indefinidamente conexão de clientes.
1. Receba a requisição do arquivo do cliente e envie o seu tamanho, caso o tenha encontrado. Em caso negativo, envie um valor inválido -1.
1. Envie o arquivo para o cliente, caso o encontre.

![gif](/gifs/questao11.gif)

[Código](https://github.com/franciscocamellon/Francisco_Camello_DR2_AT/questao_11.py)
