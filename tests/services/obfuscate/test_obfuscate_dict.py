# Third Party
import pytest

# Local
from tests.services.obfuscate.stubs import (
    encoded_valid_dict,
    invalid_input_dict,
    valid_input_dict,
)
from src.services.obfuscate.obfuscate_service import ObfuscateService


def test_obfuscate_dict_when_not_passing_any_arguments_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._obfuscate_dict()


def test_obfuscate_dict_when_passing_more_than_one_argument_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._obfuscate_dict(valid_input_dict, "unexpected value")


def test_obfuscate_dict_when_passing_invalid_input_element_then_return_empty_dict():
    encoded_dict = ObfuscateService._obfuscate_dict(input_element=invalid_input_dict)

    assert encoded_dict == dict()


def test_obfuscate_dict_when_passing_valid_input_element_then_run_successfully():
    encoded_dict = ObfuscateService._obfuscate_dict(input_element=valid_input_dict)

    assert encoded_dict == encoded_valid_dict
