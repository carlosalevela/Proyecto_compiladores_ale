from antlr4 import *
from CSVQueryDSLLexer import CSVQueryDSLLexer

def main():
    input_stream = FileStream("consulta.csvq", encoding='utf-8')
    lexer = CSVQueryDSLLexer(input_stream)

    for token in lexer.getAllTokens():
        print(f"Token: {token.text}\tTipo: {token.type}\tLínea: {token.line}")

if __name__ == "__main__":
    main()