#
# (C) Eithery Lab, 2023
# Contains unit tests for result module
#
import pytest
from expects import expect, be, equal, be_true, be_false, be_none, raise_error
from etl.std.error import error
from etl.std.exceptions import InvalidResultException
from etl.std.result import Result, Ok, Err


def describe_result():
    SOME_VALUE = 'Success!'
    ERROR_MESSAGE = 'Something wrong happens'
    SOME_ERROR = error(ERROR_MESSAGE)


    @pytest.fixture
    def error_result():
        return Result(error = SOME_ERROR)


    def it_accepts_a_value_meaning_success_result():
        expect(Result(value = SOME_VALUE).is_ok).to(be_true)


    def it_accepts_an_error_argument_for_error_result():
        expect(Result(error = SOME_ERROR).is_error).to(be_true)


    def it_accepts_an_error_instance_as_error_result():
        expect(Result(SOME_ERROR).is_error).to(be_true)


    def it_may_accept_any_error_type():
        expect(Result(error = ERROR_MESSAGE).is_error).to(be_true)


    def it_returns_unwrapped_value_for_success_result():
        expect(Result(SOME_VALUE).unwrap()).to(be(SOME_VALUE))


    def it_raises_exception_trying_to_unwrap_an_error(error_result):
        expect(error_result.unwrap).to(raise_error(InvalidResultException))


    def it_returns_a_value_for_success_result():
        expect(Result(SOME_VALUE).ok()).to(be(SOME_VALUE))


    def it_returns_none_as_a_value_for_error_result(error_result):
        expect(error_result.ok()).to(be_none)


    def it_returns_an_error_for_error_result(error_result):
        expect(error_result.err()).to(be(SOME_ERROR))


    def it_returns_none_as_an_error_for_success_result():
        expect(Result(SOME_VALUE).err()).to(be_none)


    def it_supports_a_custom_string_representation():
        expect(str(Ok(SOME_VALUE))).to(equal(f'Ok({SOME_VALUE})'))
        expect(str(Err(SOME_ERROR))).to(equal(f'Err({ERROR_MESSAGE})'))
        expect(str(Ok())).to(equal('Ok(None)'))


    def describe_ok():
        def it_creates_a_result_value():
            expect(isinstance(Ok(SOME_VALUE), Result)).to(be_true)


        def it_is_ok_result():
            expect(Ok(SOME_VALUE).is_ok).to(be_true)


        def it_is_not_an_error():
            expect(Ok(SOME_VALUE).is_error).to(be_false)


        def it_does_not_require_value_argument_for_success_result():
            expect(Ok().is_ok).to(be_true)
            expect(Ok().unwrap()).to(be_none)


    def describe_err():
        def it_creates_a_result_value():
            expect(isinstance(Err(SOME_ERROR), Result)).to(be_true)


        def it_is_an_error():
            expect(Err(SOME_ERROR).is_error).to(be_true)


        def it_is_not_ok():
            expect(Err(SOME_ERROR).is_ok).to(be_false)
