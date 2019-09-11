from projection_area_of_3d_shapes import xy_area, xz_area, yz_area


def test_xy_area():
    assert 1 == xy_area([[2]])
    assert 4 == xy_area([[1, 2], [3, 4]])
    assert 2 == xy_area([[1, 0], [0, 4]])


def test_xz_area():
    assert 2 == xz_area([[2]])
    assert 6 == xz_area([[1, 2], [3, 4]])


def test_yz_area():
    assert 2 == yz_area([[2]])
    assert 7 == yz_area([[1, 2], [3, 4]])
