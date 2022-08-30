# Third Party
import pytest

# Local
from tests.services.obfuscate.stubs import (
    encoded_valid_great_dict,
    valid_great_dict,
)
from src.services.obfuscate.obfuscate_service import ObfuscateService


def test_obfuscate_when_not_passing_any_arguments_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService.obfuscate()


def test_obfuscate_when_passing_more_than_one_argument_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService.obfuscate("new input", "unexpected value")


def test_obfuscate_when_passing_invalid_input_then_run_return_empty_string():
    encoded_value = ObfuscateService.obfuscate(input=callable)

    assert type(encoded_value) == str
    assert encoded_value == str()


def test_obfuscate_when_passing_valid_input_then_run_successfully():
    encoded_value = ObfuscateService.obfuscate(input=valid_great_dict)

    assert encoded_value == encoded_valid_great_dict
