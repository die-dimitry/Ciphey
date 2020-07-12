from typing import Optional, Dict, Any

from loguru import logger

import ciphey
from ciphey.iface import registry


@registry.register
class Octal(ciphey.iface.Decoder[bytes, str]):
    @staticmethod
    def getTarget() -> str:
        return "octal"

    def decode(self, text: bytes) -> Optional[str]:
        print("Attempting octal")
        """
        It takes an octal string and return a string
            :octal_str: octal str like "110 145 154"
        """
        logger.trace("Attempting Octal")
        str_converted = ""
        for octal_char in text.split(" "):
            str_converted += chr(int(octal_char, 8))
        logger.trace(f"Octal returns {str_converted}")
        return str_converted

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def getName() -> str:
        return "Octal"

    @staticmethod
    def priority() -> float:
        return 0.025

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
