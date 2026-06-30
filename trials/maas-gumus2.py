import numpy as np
import matplotlib.pyplot as plt

# Yıllar
years = np.arange(2015, 2026)

# Asgari ücret (TL)
wages_tl = np.array([
    1000.54, 1300.99, 1404.06, 1603.12, 2020.90,
    2324.71, 2825.90, 5500.35, 11402.32, 17002.12, 22104.67
])

# USD/TRY kuru
usd_try = np.array([
    2.70, 2.90, 3.50, 4.80, 5.70,
    7.00, 8.50, 16.00, 27.00, 34.00, 41.00
])

# Gümüş fiyatı (USD/ons)
silver_usd_oz = np.array([
    15.05, 19.99, 16.15, 15.72, 15.79,
    17.97, 25.68, 19.08, 24.04, 29.77, 36.00
])

# Asgari ücretin dolar karşılığı
wages_usd = wages_tl / usd_try

# Alınabilen ons gümüş miktarı
silver_oz_affordable = wages_usd / silver_usd_oz

# Grafik (Çift Y Ekseni)
fig, ax1 = plt.subplots(figsize=(10, 6))

color1 = 'tab:blue'
ax1.set_xlabel("Yıl")
ax1.set_ylabel("Asgari Ücret (USD)", color=color1)
ax1.plot(years, wages_usd, color=color1, marker='o', label="Asgari Ücret (USD)")
ax1.tick_params(axis='y', labelcolor=color1)

# Sağ eksen
ax2 = ax1.twinx()
color2 = 'tab:green'
ax2.set_ylabel("Alınabilen Gümüş (ons)", color=color2)
ax2.plot(years, silver_oz_affordable, color=color2, marker='s', label="Alınabilen Gümüş (ons)")
ax2.tick_params(axis='y', labelcolor=color2)

plt.title("Asgari Ücret ($) ve Alınabilen Gümüş Miktarı (2015–2025)", fontsize=13)
fig.tight_layout()
plt.grid(True)
plt.xticks(years, rotation=45)
plt.show()
