# covid_tracker.py

import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_global_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    return response.json()

def get_country_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    return response.json()
def display_global_stats():
    data = get_global_data()
    print("\n🌐 Global COVID-19 Stats:")
    print(f"Total Cases: {data['cases']}")
    print(f"Total Deaths: {data['deaths']}")
    print(f"Total Recovered: {data['recovered']}")
    print(f"Active Cases: {data['active']}")
    print(f"Today's Cases: {data['todayCases']}")

def display_country_stats(country):
    data = get_country_data(country)
    print(f"\n📍 COVID-19 Stats for {data['country']}:")
    print(f"Total Cases: {data['cases']}")
    print(f"Total Deaths: {data['deaths']}")
    print(f"Total Recovered: {data['recovered']}")
    print(f"Active Cases: {data['active']}")
    print(f"Today's Cases: {data['todayCases']}")
def plot_top_countries_cases(top_n=10):
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)
    top_countries = df.sort_values(by="cases", ascending=False).head(top_n)

    plt.figure(figsize=(12, 6))
    plt.bar(top_countries["country"], top_countries["cases"], color='skyblue')
    plt.title(f"Top {top_n} Countries by Total COVID-19 Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def main():
    print("🦠 Welcome to the COVID-19 Global Data Tracker")
    display_global_stats()

    while True:
        country = input("\nEnter a country name (or type 'exit' to quit): ").strip()
        if country.lower() == "exit":
            break
        try:
            display_country_stats(country)
        except:
            print("❌ Country not found. Try again.")

    plot_top_countries_cases()

if __name__ == "__main__":
    main()
