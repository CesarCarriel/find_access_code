from src.types import Keylogs


class BytesGateway:
    @staticmethod
    def convert_keylogs_in_bytes_to_list(content: bytes) -> Keylogs:
        content_in_string = content.decode('UTF-8')

        return [[digit for digit in line] for line in content_in_string.strip().split('\n')]
