import nose.tools
from TimeStringApplication import TimeStringApplication

def test_flux_capacitor():
    question = "12:32 34:01 15:23 9:27 55:22 25:56"
    answer = "2:32:41"
    mr_fusion = TimeStringApplication()
    assert mr_fusion.flux_capacitor(question) == answer
