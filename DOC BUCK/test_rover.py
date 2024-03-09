from main import roverpos


def test_rover():

    assert roverpos(5, 5, (1, 2, "N", "LMLMLMLMM"), (3, 3, "E", "MMRMMRMRRM"),(3, 3, "E", "MMRMMRMRRM")) == [(1, 3, 'N'), (5, 1, 'E'), (5, 1, 'E')]
    assert roverpos(5, 5, (3, 3, "E", "MMRMMRMRRM")) == [(5, 1, "E")]
    assert roverpos(5, 5, (1, 2, "N", "LMLMLMLMM")) == [(1, 3, "N")]
