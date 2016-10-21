import sh


def test_get_soccer_data():
    expected = sh.get_soccer_data(league="premier", year=2015).shape
    # print(expected)
    assert expected == (380, 65)


def test_description():
    expected = open(sh.get_data_file("notes.txt"), "r").readline()
    assert expected == "Notes for Football Data\n"


def test_get_result_data():
    # sh.get_result_data("premier", 2015, "Liverpool")
    pass
