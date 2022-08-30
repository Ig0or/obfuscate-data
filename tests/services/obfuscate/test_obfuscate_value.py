# Third Party
import pytest

# Local
from src.services.obfuscate.obfuscate_service import ObfuscateService


def test_obfuscate_value_when_not_passing_any_arguments_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._obfuscate_value()


def test_obfuscate_value_when_passing_more_than_one_argument_then_raise_type_error():
    with pytest.raises(TypeError):
        ObfuscateService._obfuscate_value("new input", "unexpected value")


def test_obfuscate_value_when_passing_invalid_input_element_then_run_successfully():
    encoded_value = ObfuscateService._obfuscate_value(
        input_element={"invalid data type": "invalid data type"}
    )

    assert encoded_value == "fc00139df3"


def test_obfuscate_value_when_passing_valid_input_element_then_run_successfully():
    encoded_value = ObfuscateService._obfuscate_value(input_element=1234567)

    assert encoded_value == "a5002d93b4"
