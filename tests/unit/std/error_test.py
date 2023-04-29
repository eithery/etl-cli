#
# (C) Eithery Lab, 2023
# Contains unit tests for error module
#
import pytest
from expects import expect, have_property, be, equal
from etl.std.error import Error, error


def describe_error():
    ERROR_MESSAGE = 'Something wrong happens'
    ERROR_CODE = 'FILE_NOT_FOUND'
    ERROR_DESCRIPTION = 'Some long error description'


    @pytest.fixture
    def simple_error() -> Error:
        return Error(ERROR_MESSAGE)


    @pytest.fixture
    def complex_error() -> Error:
        return Error(ERROR_MESSAGE, code = ERROR_CODE, description = ERROR_DESCRIPTION)


    def it_contains_error_message(simple_error: Error):
        expect(simple_error).to(have_property('message'))
        expect(simple_error.message).to(be(ERROR_MESSAGE))


    def it_provides_convenience_function_error():
        expect(error(ERROR_MESSAGE).message).to(be(ERROR_MESSAGE))


    def it_may_contain_error_code(complex_error: Error):
        expect(complex_error.code).to(be(ERROR_CODE))


    def it_may_contain_a_long_description(complex_error: Error):
        expect(complex_error.description).to(be(ERROR_DESCRIPTION))


    def it_supports_a_custom_string_representation(simple_error):
        expect(str(simple_error)).to(equal(ERROR_MESSAGE))
