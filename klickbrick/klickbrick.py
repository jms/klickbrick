import argparse


def main():
    parser = argparse.ArgumentParser(prog="klickbrick", usage="%(prog)s [options]")

    parser.add_argument("hello", type=str)
    parser.add_argument("--name", type=str)

    args = parser.parse_args()

    if args.hello and not args.name:
        print("Hello World")

    if args.name:
        print(f"Hello {args.name}")
