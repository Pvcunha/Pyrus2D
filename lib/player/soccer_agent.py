from lib.parser.cmd_line_parser import CmdLineParser
from lib.player.templates import BasicClient


class SoccerAgent:
    def __init__(self):
        self._client = BasicClient()

    def init(self,
             client: BasicClient,
             argv: list) -> bool:
        pass

    def init_impl(self,
                  cmd_parser: CmdLineParser) -> bool:
        pass

    def handle_start(self) -> bool:
        pass

    def handle_message(self):
        pass

    def handle_exit(self):
        pass
