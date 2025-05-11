from antlr4 import *
from CSVQueryDSLLexer import CSVQueryDSLLexer
from CSVQueryDSLParser import CSVQueryDSLParser
from MyCSVVisitor import MyCSVVisitor

input_stream = FileStream("programa.dsl", encoding='utf-8')
lexer = CSVQueryDSLLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CSVQueryDSLParser(stream)

# Manejo de errores
tree = parser.prog()
visitor = MyCSVVisitor()
visitor.visit(tree)