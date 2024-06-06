class TabelaSimbolos:
    def __init__(self):
        self.tabela = []

    def abrir_escopo(self):
        self.tabela.append({})  # Adiciona um novo escopo (dicionário vazio) na pilha

    def fechar_escopo(self):
        if self.tabela:
            self.tabela.pop()  # Remove o escopo atual da pilha

    def adicionar(self, lexema, tipo, valor=None):
        if lexema in self.tabela[-1]:
            return f"Erro: Variável {lexema} já declarada no escopo atual."
        self.tabela[-1][lexema] = {"tipo": tipo, "valor": valor}

    def atualizar(self, lexema, valor):
        for escopo in reversed(self.tabela):
            if lexema in escopo:
                if escopo[lexema]["tipo"] == "NUMERO" and not isinstance(valor, (int, float)):
                    return f"Erro: Tipos não compatíveis para {lexema}."
                elif escopo[lexema]["tipo"] == "CADEIA" and not isinstance(valor, str):
                    return f"Erro: Tipos não compatíveis para {lexema}."
                escopo[lexema]["valor"] = valor
                return
        return f"Erro: Variável {lexema} não declarada."

    def obter(self, lexema):
        for escopo in reversed(self.tabela):
            if lexema in escopo:
                return escopo[lexema]
        return f"Erro: Variável {lexema} não declarada."

    def __str__(self):
        return str(self.tabela)


class AnalisadorSemantico:
    def __init__(self):
        self.tabela_simbolos = TabelaSimbolos()
        self.tabela_simbolos.abrir_escopo()  # Abre o escopo global

    def analisar(self, comandos):
        for i, comando in enumerate(comandos):
            linha = i + 1  # Incrementa o número da linha
            partes = comando.split()
            if not partes:
                continue
            cmd = partes[0].upper()  # Convertendo o comando para maiúsculas
            if cmd == "BLOCO":
                self.tabela_simbolos.abrir_escopo()  # Abre um novo escopo
            elif cmd == "FIM":
                self.tabela_simbolos.fechar_escopo()  # Fecha o escopo atual
            elif cmd == "NUMERO" or cmd == "CADEIA":
                tipo = cmd
                declaracoes = " ".join(partes[1:]).split(", ")
                for dec in declaracoes:
                    if "=" in dec:
                        id, valor = dec.split("=")
                        id = id.strip()
                        valor = valor.strip()
                        if tipo == "NUMERO":
                            try:
                                valor = float(valor)
                            except ValueError:
                                print(f"Erro linha {linha}: Valor inválido para {id}")
                                continue
                        elif tipo == "CADEIA":
                            valor = valor.strip('"')
                        erro = self.tabela_simbolos.adicionar(id, tipo, valor)
                        if erro:
                            print(f"Erro linha {linha}: {erro}")
                    else:
                        id = dec.strip()
                        erro = self.tabela_simbolos.adicionar(id, tipo)
                        if erro:
                            print(f"Erro linha {linha}: {erro}")
            elif cmd == "PRINT":
                id = partes[1].strip()
                resultado = self.tabela_simbolos.obter(id)
                if "Erro" in resultado:
                    print(f"Erro linha {linha}: {resultado}")
                else:
                    print(resultado["valor"] if resultado["valor"] is not None else 0)
            elif "=" in comando:
                id, valor = comando.split("=")
                id = id.strip()
                valor = valor.strip()
                if valor.replace('.', '', 1).isdigit() or (valor[0] == '-' and valor[1:].replace('.', '', 1).isdigit()):
                    valor = float(valor)
                elif valor.startswith('"') and valor.endswith('"'):
                    valor = valor.strip('"')
                else:
                    ref = self.tabela_simbolos.obter(valor)
                    if "Erro" in ref:
                        print(f"Erro linha {linha}: {ref}")
                        continue
                    valor = ref["valor"]
                erro = self.tabela_simbolos.atualizar(id, valor)
                if erro:
                    print(f"Erro linha {linha}: {erro}")
            else:
                print(f"Comando desconhecido linha {linha}: {comando}")

def ler_comandos(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    # Não remover linhas vazias
    comandos = [linha.rstrip() for linha in linhas]
    return comandos

# Leitura de comandos a partir de um arquivo
arquivo_comandos = 'exemplo1.txt'
comandos = ler_comandos(arquivo_comandos)

# Analisar comandos
analisador = AnalisadorSemantico()
analisador.analisar(comandos)