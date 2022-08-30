# Third Party
import pytest

# Local
from tests.services.obfuscate.stubs import (
    encoded_valid_list,
    invalid_input_list,
    valid_input_list,
)
from src.services.obfuscate.obfuscate_service import ObfuscateService


def test_obfuscate_list_when_not_passing_any_arguments_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._obfuscate_list()


def test_obfuscate_list_when_passing_more_than_one_argument_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._obfuscate_list(valid_input_list, "unexpected value")


def test_obfuscate_list_when_passing_invalid_input_element_then_return_empty_list():
    encoded_list = ObfuscateService._obfuscate_list(input_element=invalid_input_list)

    assert encoded_list == list()


def test_obfuscate_list_when_passing_valid_input_element_then_run_successfully():
    encoded_list = ObfuscateService._obfuscate_list(input_element=valid_input_list)

    assert encoded_list == encoded_valid_list
