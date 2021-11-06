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

        toolchain_parser = self.subparsers.add_parser(name="onboard", description="Toolchain commands")

        toolchain_parser.add_argument("--dry-run", type=str)
        toolchain_parser.add_argument("--name", type=str, required=True)
        toolchain_parser.add_argument("--email", type=str, required=True)
        toolchain_parser.add_argument("--commit-template", type=str)

        options = self.parser.parse_args(arguments)  # type: argparse.Namespace
        getattr(self, arguments[0])(options.name)

    @staticmethod
    def hello(name: str):
        print(greeting(name))

    @staticmethod
    def onboard(name: str, email: str):
        """
        git tasks:

        git config --global user.name "John Doe"
        git config --global user.email johndoe@example.com
        git config --global init.defaultBranch main
        git config --global commit.template ~/.gitmessage.txt

        :param name:
        :param email:
        :return:
        """
        commit_template: str = "~/.gitmessage.txt"
        pass


def main():
    Klickbrick(sys.argv[1:])


if __name__ == '__main__':
    main()
