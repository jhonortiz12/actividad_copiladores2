from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from JSONListener import JSONListener


class XMLEmitter(JSONListener):
    def __init__(self):
        self.xml_map = {}
        self.indent_level = 0

    def indent(self):
        return "  " * self.indent_level

    def getXML(self, ctx):
        return self.xml_map.get(ctx, '')

    def setXML(self, ctx, value):
        self.xml_map[ctx] = value

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitString(self, ctx):
        self.setXML(ctx, ctx.getText().strip('"'))

    def exitObjectValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.jsonObject()))

    def exitPair(self, ctx):
        tag = ctx.STRING().getText().strip('"')
        val = self.getXML(ctx.value())
        if '\n' in val:
            val = f"\n{val}{self.indent()}"
        self.setXML(ctx, f"{self.indent()}<{tag}>{val}</{tag}>\n")

    def exitAnObject(self, ctx):
        self.indent_level += 1
        content = ''.join(self.getXML(p) for p in ctx.pair())
        self.indent_level -= 1
        self.setXML(ctx, content)

    def exitEmptyObject(self, ctx):
        self.setXML(ctx, '')

    def exitArrayOfValues(self, ctx):
        self.indent_level += 1
        body = ''.join(f"{self.indent()}<element>{self.getXML(v)}</element>\n" for v in ctx.value())
        self.indent_level -= 1
        self.setXML(ctx, f"\n{body}{self.indent()}")

    def exitEmptyArray(self, ctx):
        self.setXML(ctx, '')

    def exitJson(self, ctx):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))


# === Main execution ===

def main():
    input_stream = FileStream("input.json", encoding='utf-8')
    lexer = JSONLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    tree = parser.json()

    emitter = XMLEmitter()
    walker = ParseTreeWalker()
    walker.walk(emitter, tree)

    print(emitter.getXML(tree))


if __name__ == "__main__":
    main()
