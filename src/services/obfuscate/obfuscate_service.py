# Standard
from typing import Callable, Dict, Union
import hashlib

# Third Party
from decouple import config

# Local
from src.core.services.obfuscate.i_obfuscate_service import (
    IObfuscateService,
)


class ObfuscateService(IObfuscateService):
    _hash_key = config("HASH_KEY")
    _digest_size = int(config("DIGEST_SIZE"))

    @classmethod
    def _hash_value(cls, value: Union[float, int, str]) -> str:
        hash_input = (cls._hash_key + str(value)).encode()
        encoded_value = hashlib.blake2b(
            digest_size=cls._digest_size, key=hash_input
        ).hexdigest()

        return encoded_value

    @classmethod
    def _obfuscate_list(cls, input_element: list) -> list:
        encoded_list = list()

        for index in input_element:
            obfuscate_method = cls._get_method_by_type(input=index)

            if obfuscate_method:
                encoded_value = obfuscate_method(input_element=index)
                encoded_list.append(encoded_value)

        return encoded_list

    @classmethod
    def _obfuscate_dict(cls, input_element: dict) -> dict:
        encoded_dict = dict()

        for key in input_element:
            value = input_element.get(key)
            obfuscate_method = cls._get_method_by_type(input=value)

            if obfuscate_method:
                encoded_value = obfuscate_method(input_element=value)
                encoded_dict[key] = encoded_value

        return encoded_dict

    @classmethod
    def _obfuscate_value(
        cls, input_element: Union[float, int, str]
    ) -> Union[float, int, str]:
        encoded_value = cls._hash_value(value=input_element)

        return encoded_value

    @classmethod
    def _get_method_by_type(cls, input: Union[dict, float, int, list, str]) -> Callable:
        obfuscate_methods_map: Dict[type, Callable] = {
            dict: cls._obfuscate_dict,
            list: cls._obfuscate_list,
            float: cls._obfuscate_value,
            int: cls._obfuscate_value,
            str: cls._obfuscate_value,
        }
        obfuscate_method = obfuscate_methods_map.get(type(input))

        return obfuscate_method

    @classmethod
    def obfuscate(
        cls, input: Union[dict, float, int, list, str]
    ) -> Union[dict, list, str]:
        obfuscate_method = cls._get_method_by_type(input=input)

        if not obfuscate_method:
            return str()

        obfuscated_value = obfuscate_method(input_element=input)

        return obfuscated_value
