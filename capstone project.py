import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

DATA_DIR = "data"

def load_all_csv():
    all_files = Path(DATA_DIR).glob("*.csv")
    df_list = []

    for file in all_files:
        df = pd.read_csv(file)
        df["building"] = file.stem
        df_list.append(df)

    df_combined = pd.concat(df_list)
    df_combined["timestamp"] = pd.to_datetime(df_combined["timestamp"])
    return df_combined

def building_wise_summary(df):
    return df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, reading):
        self.readings.append(reading)

    def total_consumption(self):
        return sum(r.kwh for r in self.readings)

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def load_from_df(self, df):
        for _, row in df.iterrows():
            name = row["building"]
            if name not in self.buildings:
                self.buildings[name] = Building(name)
            self.buildings[name].add_reading(
                MeterReading(row["timestamp"], row["kwh"])
            )

def create_dashboard(df):
    df.set_index("timestamp", inplace=True)

    daily = df.groupby("building")["kwh"].resample("D").sum()
    weekly = df.groupby("building")["kwh"].resample("W").sum()

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    daily.unstack().plot(ax=plt.gca())
    plt.title("Daily Consumption")

    plt.subplot(3, 1, 2)
    weekly.unstack().plot(kind="bar", ax=plt.gca())
    plt.title("Weekly Consumption")

    plt.subplot(3, 1, 3)
    summary = building_wise_summary(df.reset_index())
    plt.scatter(summary.index, summary["max"])
    plt.title("Peak Consumption")

    plt.tight_layout()
    plt.savefig("dashboard.png")
    plt.show()

    return daily, weekly, summary

def export_files(df, summary):
    df.to_csv("cleaned_energy_data.csv", index=False)
    summary.to_csv("building_summary.csv")

    total = df["kwh"].sum()
    highest = summary["sum"].idxmax()

    report = f"""Total Campus Consumption: {total}
Highest Consuming Building: {highest}
"""
    with open("summary.txt", "w") as f:
        f.write(report)

def main():
    df = load_all_csv()
    daily, weekly, summary = create_dashboard(df.copy())

    manager = BuildingManager()
    manager.load_from_df(df)

    export_files(df, summary)

if __name__ == "__main__":
    main()
