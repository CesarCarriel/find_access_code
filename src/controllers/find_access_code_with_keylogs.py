from typing import List

from src.gateways import BytesGateway
from src.types import Keylogs


class FindAccessCodeWithKeyLogsController:
    def __init__(self):
        self.bytes_gateway = BytesGateway()

    def execute(self, file_content: bytes) -> str:
        keylogs = self.bytes_gateway.convert_keylogs_in_bytes_to_list(file_content)

        if not self.validated_keylogs(keylogs=keylogs):
            raise Exception('Keylogs format invalid.')

        access_code = self.find_access_code_in_keylogs(keylogs=keylogs)

        return access_code

    @staticmethod
    def validated_keylogs(keylogs: Keylogs) -> bool:
        for keylog in keylogs:
            keylog_is_not_valid = len(keylog) != 3

            if keylog_is_not_valid:
                return False

        return True

    @staticmethod
    def find_access_code_in_keylogs(keylogs: Keylogs) -> str:
        def switch_the_order_of_the_items(list_to_switch: List[int], index_a: int, index_b: int) -> List[int]:
            value_a = list_to_switch[index_a]
            value_b = list_to_switch[index_b]

            list_to_switch[index_a] = value_b
            list_to_switch[index_b] = value_a

            return list_to_switch

        access_code = keylogs[0]

        for keylog in keylogs:
            for index, value in enumerate(keylog):
                already_exists_in_access_code = value in access_code
                is_the_first = index == 0

                if already_exists_in_access_code:
                    if is_the_first:
                        next_value = keylog[index + 1]

                        if next_value in access_code:
                            order_of_values_is_incorrect = access_code.index(value) > access_code.index(next_value)

                            if order_of_values_is_incorrect:
                                access_code = switch_the_order_of_the_items(
                                    list_to_switch=access_code,
                                    index_a=access_code.index(value),
                                    index_b=access_code.index(next_value)
                                )

                    else:
                        previous_value = keylog[index - 1]

                        order_of_values_is_incorrect = access_code.index(value) < access_code.index(previous_value)

                        if order_of_values_is_incorrect:
                            access_code = switch_the_order_of_the_items(
                                list_to_switch=access_code,
                                index_a=access_code.index(value),
                                index_b=access_code.index(previous_value)
                            )

                else:
                    if is_the_first:
                        next_index_in_access_code = None

                        for posicao in range(1, len(keylog)):
                            next_value = keylog[index + posicao]

                            if next_value in access_code:
                                next_index_in_access_code = access_code.index(next_value)
                                break

                        if next_index_in_access_code:
                            access_code.insert(next_index_in_access_code, value)

                        else:
                            last_index = len(access_code)
                            access_code.insert(last_index, value)

                    else:
                        previous_value = keylog[index - 1]
                        index_previous_value_in_access_code = access_code.index(previous_value)

                        access_code.insert(index_previous_value_in_access_code + 1, value)

        return ''.join(map(str, access_code))
