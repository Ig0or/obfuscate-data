# Standard
from abc import ABCMeta, abstractmethod
from typing import Union


class IObfuscateService(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def obfuscate(
        cls, input: Union[dict, float, int, list, str]
    ) -> Union[dict, list, str]:
        pass
