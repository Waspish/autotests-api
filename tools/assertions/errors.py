from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema
from tools.assertions.base import assert_length, assert_equal


def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.location, expected.location, "location")


def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    assert_length(actual=actual.details, expected=expected.details, name="details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual=actual.details[index], expected=detail)
