import pytest
from employee import Employee


@pytest.fixture
def employee():
    """Fixture to create an employee instance for testing."""
    return Employee("Franklin", "Dolittle", 50000)


def test_give_default_raise(employee):
    """Test that the default raise of 5000 is applied."""
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    """Test that a custom raise amount is applied."""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
