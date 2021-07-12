import argparse
import sys
from typing import List, Any

from klickbrick.script import greeting


class Klickbrick:
    def __init__(self, arguments: List[Any]):
        self.parser = argparse.ArgumentParser(prog="klickbrick", usage="%(prog)s [options]")
        self.subparsers = self.parser.add_subparsers(help="sub-command help")
        self.subparsers.dest = "hello"
        self.subparsers.required = True

        hello_parser = self.subparsers.add_parser(name="hello", description="A friendly Hello World")
        hello_parser.add_argument("-n", "--name", type=str, default="World")

        options = self.parser.parse_args(arguments)  # type: argparse.Namespace
        getattr(self, arguments[0])(options.name)

    def hello(self, name: str):
        print(greeting(name))


def main():
    Klickbrick(sys.argv[1:])


if __name__ == '__main__':
    main()
