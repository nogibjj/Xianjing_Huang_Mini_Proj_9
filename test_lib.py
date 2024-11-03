from lib import read_data


def test_read_data():
    df = read_data("MSFT-stock.csv")
    assert df is not None


if __name__ == "__main__":
    test_read_data()
