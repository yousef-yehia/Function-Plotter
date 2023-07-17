import pytest
from PySide2.QtCore import Qt

import Validation
from Function_plotter import FunctionPlotter


@pytest.fixture
def app(qapp, qtbot):
    window = FunctionPlotter()
    qtbot.addWidget(window)
    return window


def test_plot_button_click(app, qtbot):
    app.edit_func.setText("5*x^3 + 2*x")
    app.edit_min.setText("0")
    app.edit_max.setText("10")
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)
    assert app.figure.axes[0].lines[0].get_xdata() is not None
    assert app.figure.axes[0].lines[0].get_ydata() is not None


def test_valid_function_input(app) -> None:
    app.edit_func.setText("5*x^3 + 2*x")
    app.edit_min.setText("0")
    app.edit_max.setText("10")
    assert not Validation.validate_function_characters("5*x^3 + 2*x")


def test_invalid_function_input(app) -> None:
    with pytest.raises(ValueError):
        app.edit_func.setText("5*x^3 + 2*")
        app.edit_min.setText("0")
        app.edit_max.setText("10")


def test_invalid_value_of_x(app) -> None:
    app.edit_func.setText("5*x^3 + 2*y")
    app.edit_min.setText("10")
    app.edit_max.setText("0")
    assert Validation.validate_min_max(10, 0)


def test_invalid_character(app) -> None:
    app.edit_func.setText("5*x^3 + 2*y")
    app.edit_min.setText("0")
    app.edit_max.setText("10")
    assert Validation.validate_function_characters("5*x^3 + 2*y")
    assert "Error" in app.windowTitle()


if __name__ == "__main__":
    pytest.main()
