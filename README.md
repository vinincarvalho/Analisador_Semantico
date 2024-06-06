**Tabela de Símbolos e Analisador Semântico**

Este programa Python consiste em uma implementação de uma Tabela de Símbolos e um Analisador Semântico. A Tabela de Símbolos é uma estrutura de dados que mantém o controle das variáveis declaradas em um código, enquanto o Analisador Semântico verifica a semântica do código, identificando possíveis erros.

### Tabela de Símbolos

A classe `TabelaSimbolos` define métodos para manipular a tabela de símbolos:

- `abrir_escopo()`: Adiciona um novo escopo (dicionário vazio) na pilha.
- `fechar_escopo()`: Remove o escopo atual da pilha.
- `adicionar(lexema, tipo, valor=None)`: Adiciona uma variável à tabela de símbolos.
- `atualizar(lexema, valor)`: Atualiza o valor de uma variável na tabela de símbolos.
- `obter(lexema)`: Obtém as informações de uma variável na tabela de símbolos.
- `__str__()`: Retorna uma representação da tabela de símbolos.

### Analisador Semântico

A classe `AnalisadorSemantico` implementa a lógica de análise semântica:

- `__init__()`: Inicializa a tabela de símbolos e abre o escopo global.
- `analisar(comandos)`: Analisa os comandos fornecidos, verificando a semântica do código.
- `ler_comandos(arquivo)`: Lê os comandos a partir de um arquivo.

### Uso

Para usar o programa, é necessário fornecer um arquivo de comandos. Um exemplo de uso é fornecido no final do script:

```python
arquivo_comandos = 'exemplo1.txt'
comandos = ler_comandos(arquivo_comandos)

# Analisar comandos
analisador = AnalisadorSemantico()
analisador.analisar(comandos)
```

### Exemplo de Arquivo de Comandos

Um exemplo de arquivo de comandos (`exemplo1.txt`) pode conter uma série de comandos, como declarações de variáveis, blocos de código e operações de atribuição.

### Execução

Para executar o programa, basta fornecer um arquivo de comandos como entrada.

### Nota

Este é um exemplo básico de implementação. Para casos mais complexos ou específicos, podem ser necessárias modificações ou expansões no código.
