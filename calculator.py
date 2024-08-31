import ast
import operator as op

# Dictionary operator yang menghubungkan node AST dengan fungsi operator
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
}

def eval_expr(expr: str) -> float:
    """
    Mengevaluasi ekspresi matematika dari string menggunakan AST.

    :param expr: Ekspresi matematika dalam bentuk string
    :return: Hasil evaluasi sebagai float
    """
    # Parsing ekspresi menjadi AST
    tree = ast.parse(expr, mode='eval')

    def _eval(node):
        if isinstance(node, ast.Num):  # Jika node adalah angka
            return node.n
        elif isinstance(node, ast.BinOp):  # Jika node adalah operasi biner
            left = _eval(node.left)
            right = _eval(node.right)
            return operators[type(node.op)](left, right)
        else:
            raise TypeError(node)

    return _eval(tree.body)

# function untuk eksekusi program
def main():
    while True:
        expr = input("Masukkan ekspresi matematika (atau ketik 'exit' untuk keluar): ")
        if expr.lower() == 'exit':
            break
        try:
            result = eval_expr(expr)
            print(f"Hasil: {result}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
