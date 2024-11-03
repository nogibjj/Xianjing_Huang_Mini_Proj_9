from lib import read_data
from script import generate_summary_statistics, compute_summary_statistics
from script import draw_line_chart, generate_PDF


def test_generate_summary_statistics():
    df = read_data("MSFT-stock.csv")
    res = generate_summary_statistics(df)
    assert res is not None


def test_compute_summary_statistics():
    df = read_data("MSFT-stock.csv")
    res = compute_summary_statistics(df)
    assert res is None


def test_draw_line_chart():
    df = read_data("MSFT-stock.csv")
    res = draw_line_chart(df)
    assert res is None


def test_generate_PDF():
    df = read_data("MSFT-stock.csv")
    res = generate_PDF(df)
    assert res is None


if __name__ == "__main__":
    test_generate_summary_statistics()
    test_compute_summary_statistics()
    test_draw_line_chart()
    test_generate_PDF()
