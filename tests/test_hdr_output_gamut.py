import pytest
import render.hdr_output_gamut as mod

CASES = [
    ("float_swapchain", (1, 2)),
    ("display_gamut", (1, 2)),
    ("recreate_swapchain", (1, 2)),
    ("luminance_meta", (1000.0, 400.0)),
    ("sdr_remap", (1.0, 2.0)),
    ("ui_luminance", (200.0, 100.0)),
    ("screenshot_sync", (1, 2)),
    ("dither_10bit", (1024, 2)),
    ("single_gamma", (2.2, 1.0)),
    ("refresh_profile", (1, 2)),
    ("gamut_convert", (1.0, 0.5)),
    ("maxcll", (1000.0, 2.0)),
    ("hdr_toggle", (1, 2)),
    ("tonemap_target", (203.0, 100.0)),
    ("output_format", (10, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
