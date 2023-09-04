from __future__ import annotations
from crcmod.predefined import PredefinedCrc


class Catlifier:
    def __init__(self, base_text: str):
        self.base_text = base_text
        self.crc_calculator = PredefinedCrc("crc-ccitt-false")

    def catlify(self) -> str:
        """"Catlify a gven string. Also updated internal CRC calculator with
        catlified data."""
        catlified = self.base_text + "🐈"
        self.crc_calculator.new()
        self.crc_calculator.update(catlified.encode())
        return catlified
    
    @classmethod
    def uncatlify(cls, catlified_text: str) -> Catlifier:
        stripped_text = catlified_text.rstrip("🐈")
        instance = cls(stripped_text)
        instance.crc_calculator.update(catlified_text)
        return instance
