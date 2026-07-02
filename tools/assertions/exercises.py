from typing import List

import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, ExerciseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_is_true, assert_length
from tools.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise")

    assert_equal(actual.title, expected.title, name="title")
    assert_equal(actual.course_id, expected.course_id, name="course_id")
    assert_equal(actual.max_score, expected.max_score, name="max_score")
    assert_equal(actual.min_score, expected.min_score, name="min_score")
    assert_equal(actual.order_index, expected.order_index, name="order_index")
    assert_equal(actual.description, expected.description, name="description")
    assert_equal(actual.estimated_time, expected.estimated_time, name="estimated_time")
    assert_equal(actual.id, expected.id, name="id")


@allure.step("Check create exercise response")
def assert_create_exercise_response(response: CreateExerciseResponseSchema, request: CreateExerciseRequestSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует запросу.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create exercise response")

    assert_equal(response.exercise.title, request.title, name="title")
    assert_equal(response.exercise.course_id, request.course_id, name="course_id")
    assert_equal(response.exercise.max_score, request.max_score, name="max_score")
    assert_equal(response.exercise.min_score, request.min_score, name="min_score")
    assert_equal(response.exercise.order_index, request.order_index, name="order_index")
    assert_equal(response.exercise.description, request.description, name="description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, name="estimated_time")

    assert_is_true(response.exercise.id, name="exercise_id")


@allure.step("Check get exercise response")
def assert_get_exercise_response(create_exercise_response: CreateExerciseResponseSchema,
                                 get_exercise_response: GetExerciseResponseSchema):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные файла не совпадают.
    """
    logger.info("Check get exercise response")

    assert_exercise(actual=get_exercise_response.exercise, expected=create_exercise_response.exercise)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        create_exercise_responses: List[CreateExerciseResponseSchema],
        get_exercises_response: GetExercisesResponseSchema
):
    """
    Проверяет, что ответ на получение упражнений соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе данных упражнений.
    :param create_exercise_responses: Ответ API при создании упражнений.
    :raises AssertionError: Если данные файла не совпадают.
    """
    logger.info("Check get exercises response")

    assert_length(actual=get_exercises_response.exercises, expected=create_exercise_responses, name="exercises")

    for index, exercise in enumerate(create_exercise_responses):
        assert_exercise(actual=get_exercises_response.exercises[index], expected=exercise.exercise)


@allure.step("Check update exercise response")
def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema,
        exercise_id: str
):
    """
    Проверяет, что ответ на обновление курса соответствует запросу.

    :param request: Исходный запрос на обновление упражнения.
    :param response: Ответ API с данными упражнения.
    :param exercise_id: Id упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update exercise response")

    assert_equal(response.exercise.title, request.title, name="title")
    assert_equal(response.exercise.max_score, request.max_score, name="max_score")
    assert_equal(response.exercise.min_score, request.min_score, name="min_score")
    assert_equal(response.exercise.order_index, request.order_index, name="order_index")
    assert_equal(response.exercise.description, request.description, name="description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, name="estimated_time")

    assert_equal(response.exercise.id, exercise_id, name="exercise_id")

    assert_is_true(response.exercise.course_id, name="course_id")


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если упражнение не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    logger.info("Check exercise not found response")

    # Ожидаемое сообщение об ошибке, если упражнение не найдено
    expected = InternalErrorResponseSchema(details="Exercise not found")

    # Используем ранее созданную функцию для проверки внутренней ошибки
    assert_internal_error_response(actual=actual, expected=expected)
