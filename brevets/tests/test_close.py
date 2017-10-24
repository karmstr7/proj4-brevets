"""
Nose tests for closeclose_time() in acpclose_times.py
"""

from acp_times import close_time

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_empty():
    """
    There might not be anything!
    """
    assert close_time(0, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T09:00:00+00:00"


def test_negative():
    """
    What happens with a negative Control?
    """
    assert close_time(-100, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T09:00:00+00:00"


def test_small():
    """
    What happens with a very small Control?
    """
    assert close_time(1, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T08:04:00+00:00"


def test_large():
    """
    What happens with a large control that's within the allowed total distance
    """
    assert close_time(219, 200, '2017-01-01T08:00:00.000Z') == "2017-01-01T21:30:00+00:00"


def test_too_large():
    """
    What happens with a humongous control?
    """
    assert close_time(1000, 200, '2017-01-01T08:00:00.000Z') is None


def test_long_brevet():
    """
    Set control_km, brevet_dist_km to 1000km
    """
    assert close_time(999, 1000, '2017-01-01T08:00:00+00:00') == "2017-01-04T10:55:00+00:00"
