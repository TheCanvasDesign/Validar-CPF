Validador de CPF em Python
Este script em Python tem como objetivo validar números de Cadastro de Pessoas Físicas (CPF). 
Ele solicita o número ao usuário, limpa a formatação e executa o cálculo matemático para verificar a autenticidade dos dígitos verificadores.

🚀 Funcionalidades

Entrada Simples: Solicita a entrada de dados do usuário através do terminal.  

Limpeza de Dados: Remove automaticamente quaisquer caracteres que não sejam numéricos (como pontos ou traços) usando a função filter.  

Validação de Formato: Realiza uma validação inicial para garantir que o número possua exatamente 11 dígitos e bloqueia CPFs formados por uma sequência de números repetidos.

⚙️ Como Funciona o Algoritmo
O código utiliza uma função dedicada chamada digito_verificador para realizar a etapa matemática de validação. O fluxo principal opera da seguinte forma:  

Processamento e Acúmulo: A função prepara uma variável de soma (iniciando em 0), realiza o alinhamento dos dígitos com seus pesos usando zip, converte o dígito para inteiro (int(dig)) e acumula a multiplicação.  

Lógica do Resto: Após somar tudo, o script aplica a operação de módulo 11 (soma % 11). A entrega final (return) da função é 0 caso o resto seja menor que 2, ou a diferença 11 - resto para os demais casos.  

Pesos Regressivos: O script gera duas listas de pesos diferentes: pesos1 (de 10 até 2) e pesos2 (de 11 até 2).  

Cálculo dos Dígitos: O primeiro dígito verificador (digito1) é calculado avaliando os 9 primeiros números do CPF com a primeira lista de pesos, e o segundo (digito2) usando os 10 primeiros números com a segunda lista.  

Verificação Final: O script compara a junção dos dois dígitos calculados com os dois últimos dígitos do CPF informado.  

Resultado: O console exibirá CPF válido! caso a comparação seja exata , ou imprimirá CPF inválido! caso a verificação dos dígitos ou as regras iniciais de formatação falhem.

💻 Como Executar
Certifique-se de ter o Python instalado no seu sistema.

Salve o código em um arquivo com a extensão .py (exemplo: validar_cpf.py).

Abra o terminal na pasta do arquivo e rode o comando:

Bash
python validar_cpf.py
Quando aparecer a instrução "Digite seu número de CPF: ", insira o número desejado.  

Pressione Enter e confira o resultado validado na tela.
