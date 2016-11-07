import nose.tools
from TimeStringApplication import TimeStringApplication

def test_flux_capacitor():
    say = "1.21 Gigawatts!"
    mr_fusion = TimeStringApplication()
    assert mr_fusion.flux_capacitor(say) == say
