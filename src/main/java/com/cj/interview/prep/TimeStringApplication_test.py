import nose.tools
from TimeStringApplication import TimeStringApplication

def test_flux_capacitor():
    say = "12:32 34:01 15:23 9:27 55:22 25:56" 
    mr_fusion = TimeStringApplication()
    assert mr_fusion.flux_capacitor(say) == say
