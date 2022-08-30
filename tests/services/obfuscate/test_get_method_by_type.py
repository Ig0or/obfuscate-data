# Third Party
import pytest

# Local
from src.services.obfuscate.obfuscate_service import ObfuscateService


def test_get_method_by_type_when_not_passing_any_arguments_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._get_method_by_type()


def test_get_method_by_type_when_passing_more_than_one_argument_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._get_method_by_type("new input", "unexpected value")


def test_get_method_by_type_when_passing_invalid_input_then_return_none():
    obfuscate_method = ObfuscateService._get_method_by_type(input=callable)

    assert obfuscate_method is None


def test_get_method_by_type_when_passing_valid_input_then_run_successfully():
    obfuscate_method = ObfuscateService._get_method_by_type(input="new input")

    assert callable(obfuscate_method)
    assert obfuscate_method == ObfuscateService._obfuscate_value
