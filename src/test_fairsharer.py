import pytest
from function import fair_sharer

def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
    assert fair_sharer([100, 200, 300], 1, share=0.2) == [180, 160, 260]
