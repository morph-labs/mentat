import asyncio
from collections import deque
import logging
import re

from termcolor import colored


class StreamingPrinter:
    def __init__(self):
        self.strings_to_print = deque([])
        self.chars_remaining = 0
        self.shutdown = False

    def add_string(self, string, end="\n", color=None):
        # logging.getLogger().info(f"{string=}")
        if len(string) == 0:
            return
        string += end

        # # colored_string = colored(string, color) if color is not None else string
        # colored_string = string

        # index = colored_string.index(string)
        # characters = list(string)
        # characters[0] = colored_string[:index] + characters[0]
        # characters[-1] = characters[-1] + colored_string[index + len(string) :]

        # self.strings_to_print.extend(characters)
        # self.chars_remaining += len(characters)
        print(string, end="", flush=True)

    def sleep_time(self):
        max_finish_time = 1.0
        required_sleep_time = max_finish_time / (self.chars_remaining + 1)
        max_sleep = 0.0002 if self.shutdown else 0.0006
        min_sleep = 0.0002
        return max(min(max_sleep, required_sleep_time), min_sleep)

    async def print_lines(self):
        # def strip_ansi_codes(s):
        #     return re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K]?', '', s)        
        # while True:
        #     if self.strings_to_print:
        #         next_string = self.strings_to_print.popleft()
        #         # logging.getLogger().info(f"{next_string=}")
        #         next_string = strip_ansi_codes(next_string)
        #         print(next_string, end="", flush=True)
        #         self.chars_remaining -= 1
        #     elif self.shutdown:
        #         break
        #     await asyncio.sleep(self.sleep_time())
        pass

    def wrap_it_up(self):
        self.shutdown = True
