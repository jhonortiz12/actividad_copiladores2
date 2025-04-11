# CSVListenerCustom.py
from CSVListener import CSVListener
from CSVParser import CSVParser
from collections import Counter, defaultdict
import json

class CSVLoader(CSVListener):
    def __init__(self):
        self.rows = []
        self.header = []
        self.currentRowFieldValues = []
        self.emptyFieldCount = 0

    def exitText(self, ctx):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx):
        self.currentRowFieldValues.append(ctx.getText())

    def exitEmpty(self, ctx):
        self.currentRowFieldValues.append("")
        self.emptyFieldCount += 1

    def exitRow(self, ctx):
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            self.header = self.currentRowFieldValues
        else:
            if len(self.currentRowFieldValues) != len(self.header):
                print(f"Fila inválida: {self.currentRowFieldValues}")
            fila_dict = {self.header[i]: val for i, val in enumerate(self.currentRowFieldValues)}
            self.rows.append(fila_dict)
        self.currentRowFieldValues = []

    def limpiar_montos(self):
        for fila in self.rows:
            if "Cantidad" in fila:
                fila["Cantidad"] = fila["Cantidad"].replace('"', '').replace('$','').replace(',', '')

    def exportar_a_json(self, filename="output.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.rows, f, indent=2, ensure_ascii=False)

    def print_column_stats(self, column_name="Cantidad"):
        print(f"\nEstadísticas para columna '{column_name}':")
        for fila in self.rows:
            if column_name in fila:
                print(f"• {fila[column_name]}")

    def contar_meses(self):
        meses = [fila["Mes"] for fila in self.rows if "Mes" in fila]
        contador = Counter(meses)
        print("\nConteo de meses:")
        for mes, total in contador.items():
            print(f"{mes}: {total}")

    def detectar_duplicados(self):
        vistas = set()
        duplicadas = 0
        for fila in self.rows:
            f = tuple(fila.items())
            if f in vistas:
                duplicadas += 1
            vistas.add(f)
        print(f"\nFilas duplicadas: {duplicadas}")

    def verificar_cantidad(self):
        errores = 0
        for fila in self.rows:
            valor = fila.get("Cantidad", "").replace('"', '').replace('$','').replace(',', '')
            if not valor.strip().isdigit():
                errores += 1
        print(f"\nCampos 'Cantidad' vacíos o mal formateados: {errores}")

    def suma_por_mes(self):
        sumas = defaultdict(float)
        for fila in self.rows:
            mes = fila.get("Mes", "")
            try:
                monto = float(fila.get("Cantidad", "0").replace('"', '').replace('$','').replace(',', ''))
                sumas[mes] += monto
            except:
                pass
        print("\nMontos totales por mes:")
        for mes, total in sumas.items():
            print(f"{mes}: {total}")
