# Third Party
import pytest

# Local
from src.services.obfuscate.obfuscate_service import ObfuscateService


def test_hash_value_when_not_passing_any_arguments_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._hash_value()


def test_hash_value_when_passing_more_than_one_argument_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._hash_value("new input", "unexpected value")


def test_hash_value_when_passing_invalid_value_then_run_successfully():
    encoded_value = ObfuscateService._hash_value(value=["invalid data type"])

    assert encoded_value == "26fbc347b9"


def test_hash_value_when_passing_valid_value_then_run_successfully():
    encoded_value = ObfuscateService._hash_value(value="value to encode")

    assert encoded_value == "734037c262"
