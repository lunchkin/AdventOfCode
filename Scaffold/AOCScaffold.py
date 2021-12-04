import sys
import io
import pathlib
import logging
from typing import Optional


class AOCScaffold:
    input_count = 0

    @staticmethod
    def print_error(e):
        print(f"{e}", file=sys.stderr)

    @staticmethod
    def print_debug(d):
        logging.debug(f'{d}')

    def __init__(self, input_file: pathlib.Path):
        self.input_file = input_file
        self.read_input_file(input_file=input_file)

    def main(self):
        for part in [method for method in dir(self) if method.startswith('part')]:
            getattr(self, part)()
            self.print_debug('-' * 50)

    def stage_part(func):
        def inner(self):
            self.read_input_file(input_file=self.input_file)
            func(self)

        return inner

    def read_input_file(self, input_file: Optional[pathlib.Path]):
        if not input_file and not self.input_file:
            raise Exception(f"Must supply input file to stdin!")

        input_path = f"{(input_file if input_file else self.input_file).parent}" \
                          f"/{(input_file if input_file else self.input_file).stem}.txt"

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

        print(f"Piping {input_path} into stdin...")
        self.input_count = len(open(input_path, 'r').readlines())
        sys.stdin = io.StringIO(open(input_path, 'r').read())