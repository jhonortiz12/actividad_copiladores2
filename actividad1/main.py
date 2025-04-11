# main.py
import sys
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListenerCustom import CSVLoader

def main(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    loader = CSVLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    # Procesos
    loader.limpiar_montos()
    loader.print_column_stats("Cantidad")
    loader.contar_meses()
    loader.detectar_duplicados()
    loader.verificar_cantidad()
    loader.suma_por_mes()
    loader.exportar_a_json("resultado_limpio.json")
    print(f"\nTotal de campos vacíos: {loader.emptyFieldCount}")

if __name__ == '__main__':
    main(sys.argv[1])
