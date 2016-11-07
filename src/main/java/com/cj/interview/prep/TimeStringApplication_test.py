import nose.tools
from TimeStringApplication import TimeStringApplication

def test_something():
    flux_capacitor = TimeStringApplication()
    assert flux_capacitor.mr_fusion() == "1.21 gigawatts!"
