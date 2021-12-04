# To generate this, type 'AOC' - Must be in all caps to show prompt
from Scaffold import AOCScaffold
import pathlib


class Solution(AOCScaffold.AOCScaffold):
    def __init__(self):
        super().__init__(pathlib.Path(__file__))

    @AOCScaffold.AOCScaffold.stage_part
    def part1(self):
        for _ in range(int(self.input_count)):
            pass
        self.print_debug(f"Solution: {None}")

    @AOCScaffold.AOCScaffold.stage_part
    def part2(self):
        for _ in range(int(self.input_count)):
            pass
        self.print_debug(f"Solution: {None}")