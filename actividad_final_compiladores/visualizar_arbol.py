from antlr4 import *
from CSVQueryDSLLexer import CSVQueryDSLLexer
from CSVQueryDSLParser import CSVQueryDSLParser

def main():
    input_stream = FileStream("input.csvq", encoding='utf-8')
    lexer = CSVQueryDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CSVQueryDSLParser(token_stream)

    tree = parser.prog() 

    print(tree.toStringTree(recog=parser))  # Imprime árbol sintáctico plano

if __name__ == '__main__':
    main()
