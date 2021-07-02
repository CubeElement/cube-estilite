import pytest
from PyQt5 import QtCore

from pytestqt import qt_compat
from pytestqt.qt_compat import qt_api

from model import Model
from mainframe import MainWindow
import re


@pytest.fixture
def app(qtbot):
    model = Model()
    widget = MainWindow(model)
    qtbot.addWidget(widget)

    return widget

@pytest.fixture
def qline_list(app):
    qlineedit_objects = [app.ui_dia,
                         app.ui_speed,
                         app.ui_rev,
                         app.ui_z,
                         app.ui_feedrate,
                         app.ui_feedpertooth]
    return qlineedit_objects

def clear_all(ui_lines: list):
    for lineedit in ui_lines:
        lineedit.clear()

def test_start_values(app, qline_list):
    for qlineedit in qline_list:
        assert qlineedit.text() == ""

class TestUI:
    @pytest.mark.parametrize(
        'dia, speed, rev, z, f, fz',
        [
           (10, 52, 1655.21, 3, 2000, 0.40276),
           (20, 90, 1432.39, 4, 5000, 0.87266)
        ]
    )
    def test_ui_rev_fz(self, qtbot, app, dia, speed, rev, z, f, fz, qline_list):
        clear_all(qline_list)
        qtbot.keyClicks(app.ui_dia, str(dia))
        app.ui_dia.editingFinished.emit()
        qtbot.keyClicks(app.ui_speed, str(speed))
        app.ui_speed.editingFinished.emit()
        qtbot.keyClicks(app.ui_z, str(z))
        app.ui_z.editingFinished.emit()
        qtbot.keyClicks(app.ui_feedrate, str(f))
        app.ui_feedrate.editingFinished.emit()
        assert app.ui_rev.text() == str(rev)
        assert app.ui_feedpertooth.text() == str(fz)

    @pytest.mark.parametrize(
        'dia, speed, rev, z, f, fz',
        [
           (10, 314.159, 10000,  5, 5526.0, 0.11052),
           (50, 1507.96,  9600, 50,  480.0, 0.001)
        ]
    )
    def test_ui_speed_f(self, qtbot, app, dia, speed, rev, z, f, fz, qline_list):
        clear_all(qline_list)
        qtbot.keyClicks(app.ui_dia, str(dia))
        app.ui_dia.editingFinished.emit()
        qtbot.keyClicks(app.ui_rev, str(rev))
        app.ui_rev.editingFinished.emit()
        qtbot.keyClicks(app.ui_z, str(z))
        app.ui_z.editingFinished.emit()
        qtbot.keyClicks(app.ui_feedpertooth, str(fz))
        app.ui_feedpertooth.editingFinished.emit()
        assert app.ui_speed.text() == str(speed)
        assert app.ui_feedrate.text() == str(f)

    @pytest.mark.parametrize(
        'invalid_input',
        ['a', 'abcdefg', '0.1.1', '0,1', " ", ""])
    def test_ui_invalid_input(self, qtbot, app, qline_list, invalid_input):
        for element in qline_list:
            qtbot.keyClicks(element, str(invalid_input))
            element.editingFinished.emit()
            assert element.text() == ""
            element.clear()

class TestModel:
    app.model = Model()
    app.actvalues = dict()
    @pytest.mark.parametrize(
        'invalid_input',
        ['a', 'abcdefg', '0.1.1', '0,1', " ", "", "-15", -15.0])
    def test_is_valid_float_fail(self, app, invalid_input):
        assert app.is_valid_float(invalid_input) == False

    @pytest.mark.parametrize(
        'valid_input',
        ['0.12', 998, 0.15779, 0, 000.1, 15.0, +15])
    def test_is_valid_float_pass(self, app, valid_input):
        assert app.is_valid_float(valid_input) == True

    def test_assign_pass(self, app, qline_list):
        for element in qline_list:
            app.assign_value(element, 1.0)
        assert app.actvalues == {
            'ui_dia': 1.0,
            'ui_speed': 1.0,
            'ui_rev': 1.0,
            'ui_z': 1.0,
            'ui_feedrate': 1.0,
            'ui_feedpertooth': 1.0
        }

    def test_act_deact(self, app):
        app.activate('ui_dia', 20)
        assert app.actvalues == {'ui_dia': 20}
        app.deactivate('ui_dia')
        assert app.actvalues == {}

    def test_formula_speed(self):
        res = app.model.speed_formula(revolutions=485, diameter=25)
        assert res == 38.09181092477624

    def test_formula_rev(self):
        res = app.model.revolutions_formula(cutting_speed=70, diameter=32)
        assert res == 696.3028760270421

    def test_formula_feedrate(self):
        res = app.model.feedrate_formula(speed=90, znum=5, feedpertooth=0.4)
        assert res == 180.0

    def test_formula_feedrate(self):
        res = app.model.feedpertooth_formula(speed=120, znum=10, feedrate=120)
        assert res == 0.1

    def test_material_buttons(self, qtbot, app, mat_list):
        for ui_item, letter in mat_list.items():
            qtbot.mouseClick(ui_item, QtCore.Qt.LeftButton)
            print(ui_item)
            assert ui_item.text() == mat_list[ui_item]
