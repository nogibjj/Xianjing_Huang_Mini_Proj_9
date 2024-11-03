import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


def generate_summary_statistics(df):
    """Return Summary Stats"""
    #     cols = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    return df.describe()


def compute_summary_statistics(df):
    """compute mean, median, standard deviation"""
    col_len = df.shape[1]

    for i in range(1, col_len):
        name = df.columns[i]
        mean = df[name].mean()
        print(f"Mean of {name}: {mean:.2f}")
    print("-------------")
    for i in range(1, col_len):
        name = df.columns[i]
        median = df[name].median()
        print(f"Median of {name}: {median:.2f}")
    print("-------------")
    for i in range(1, col_len):
        name = df.columns[i]
        std = df[name].std()
        print(f"Standard Deviation of {name}: {std:.2f}")
    print("-------------")
    return


def draw_line_chart(df):
    """Show the Open and Close prices over time"""
    df["Date"] = pd.to_datetime(df["Date"])
    plt.figure(figsize=(10, 6))
    plt.plot(df["Date"], df["Open"], label="Open", marker="o")
    plt.plot(df["Date"], df["Close"], label="Close", marker="o")
    plt.title("Open and Close Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=10)
    plt.savefig("stock_line_chart.png")
    return


#     plt.show()


def generate_PDF(df):
    """create PDF and save"""
    pdf = FPDF()
    pdf.add_page()
    # add title
    pdf.set_font("Arial", "B", 16)
    title = "Report " "for Microsoft-Stock"
    pdf.cell(200, 10, txt=title, ln=True, align="C")

    pdf.ln(10)

    # part1: dataset introduction
    pdf.set_font("Arial", "B", 14)
    title_part1 = "1. Dataset Introduction"
    pdf.cell(200, 10, txt=title_part1, ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    content_part1 = (
        "This is a reduced version of Microsoft's Stock from Yahoo Finance! \n"
        "Date: Date of stock information. \n"
        "Open: Opening price. \n"
        "High: Highest price. \n"
        "Low: Lowest price. \n"
        "Close: Closing price. \n"
        "Adj Close: Closing price after adjustments for all applicable "
        "splits and dividend distributions. \n"
        "Volume: Amount of stock. \n"
        "Data source: "
    )
    pdf.multi_cell(0, 10, txt=content_part1)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.set_y(y - 10)
    pdf.set_x(x + 22)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font("Arial", "I", 10)
    link_txt = "https://www.kaggle.com/datasets/pauldavidjarvis/microsoft-stock"
    pdf.cell(
        200,
        10,
        txt=link_txt,
        ln=True,
        align="L",
        link="https://www.kaggle.com/datasets/pauldavidjarvis/microsoft-stock",
    )

    pdf.ln(10)
    # part2: descriptive statistics
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "B", 14)
    title_part2 = "2. Descriptive Statistics"
    pdf.cell(200, 10, txt=title_part2, ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    content_part2 = f"{generate_summary_statistics(df)}"
    pdf.multi_cell(200, 10, txt=content_part2)

    pdf.ln(10)

    # part3: data visualization
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    title_part3 = "3. Data Visualization"
    pdf.cell(200, 10, txt=title_part3, ln=1, align="L")
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.image("stock_line_chart.png", x=x, y=y, w=190)

    # save PDF
    pdf.output("report.pdf")


# if __name__ == "__main__":
#     df = read_data("MSFT-stock.csv")
#     print(generate_summary_statistics(df))
#     compute_summary_statistics(df)
#     draw_line_chart(df)
#     generate_PDF(df)
