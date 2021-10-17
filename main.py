import pandas as pd
import matplotlib.pyplot as plt


# gets the percent difference between the qbr of the best quarterback and
# the qbr for the average quarterback between the indicated years
def percent_difference(averages: pd.DataFrame, leaders: pd.DataFrame, start: int, end: int) -> pd.DataFrame:
    res = []
    stat_av = averages["Rate"]
    stat_lead = leaders["Rate"]

    for i in range(start, end+1):
        res.append([i, (stat_lead[i] - stat_av[i]) / stat_av[i] * 100])

    return pd.DataFrame(data=res, columns=["year", "difference average/top qbr"])


def main():
    averages = pd.read_csv("passing_averages.csv")
    averages = averages.set_index("Year")
    leaders = pd.read_csv("qbr_leaders_by_year.csv")
    leaders = leaders.set_index("Year")
    percent_differences = percent_difference(averages, leaders, 1970, 2020)
    plt.scatter(percent_differences["year"], percent_differences["difference average/top qbr"])
    plt.show()


main()
