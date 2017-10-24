"""
Nose tests for open_time() in acp_times.py
"""

from acp_times import open_time

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_empty():
    """
    There might not be anything!
    """
    assert open_time(0, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T08:00:00+00:00"


def test_negative():
    """
    What happens with a negative Control?
    """
    assert open_time(-100, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T08:00:00+00:00"


def test_small():
    """
    What happens with a very small Control?
    """
    assert open_time(1, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T08:02:00+00:00"


def test_large():
    """
    What happens with a large control that's within the allowed total distance
    """
    assert open_time(219, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T13:53:00+00:00"


def test_too_large():
    """
    What happens with a humongous control?
    """
    assert open_time(1000, 200, '2017-01-01T08:00:00.000Z') is None


def test_long_brevet():
    """
    Set control_km, brevet_dist_km to 1000km
    """
    assert open_time(999, 1000, '2017-01-01T08:00:00+00:00') == "2017-01-02T17:03:00+00:00"
