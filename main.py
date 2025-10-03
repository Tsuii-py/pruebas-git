"""CLI simple que usa el paquete `miniapp`.

Uso:
  python main.py add 1 2
  python main.py div 4 2
"""
import argparse
from miniapp import add, sub, mul, div


def build_parser():
    p = argparse.ArgumentParser(description='Mini app demo: operaciones aritméticas')
    p.add_argument('operation', choices=['add', 'sub', 'mul', 'div'], help='Operación a realizar')
    p.add_argument('a', type=float, help='Primer número')
    p.add_argument('b', type=float, help='Segundo número')
    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    ops = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
    func = ops[args.operation]
    try:
        result = func(args.a, args.b)
    except Exception as e:
        print(f'Error: {e}')
        return 1
    print(result)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
print("Hola Mundo 2")