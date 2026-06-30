import numpy as np
import matplotlib.pyplot as plt

# Yıllar
years = np.arange(2015, 2026)

# Net asgari ücret (TL) - Temmuz verileri
wages_tl = np.array([
    1000.54, 1300.99, 1404.06, 1603.12, 2020.90,
    2324.71, 2825.90, 5500.35, 11402.32, 17002.12, 22104.67
])

# USD/TRY kuru - Temmuz ortalama/tahmini
usd_try = np.array([
    2.70, 2.90, 3.50, 4.80, 5.70,
    7.00, 8.50, 16.00, 27.00, 34.00, 41.00
])

# Gümüş fiyatı (USD/ons) - Temmuz
silver_usd_oz = np.array([
    15.05, 19.99, 16.15, 15.72, 15.79,
    17.97, 25.68, 19.08, 24.04, 29.77, 36.00
])

# Dolar karşılığı net maaş
wages_usd = wages_tl / usd_try

# Alınabilecek ons gümüş miktarı
silver_oz_affordable = wages_usd / silver_usd_oz

# Grafik
plt.figure(figsize=(10, 6))
plt.plot(years, silver_oz_affordable, color='purple', marker='o')
plt.title("Asgari Ücretle Alınabilen Ons Gümüş Miktarı (Temmuz 2015–2025)", fontsize=13)
plt.xlabel("Yıl", fontsize=12)
plt.ylabel("Ons Gümüş", fontsize=12)
plt.grid(True)
plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()

# İsteğe bağlı: Değerleri yazdır
for year, usd, silver in zip(years, wages_usd, silver_oz_affordable):
    print(f"{year}: {usd:.2f} $ → {silver:.2f} ons gümüş")
