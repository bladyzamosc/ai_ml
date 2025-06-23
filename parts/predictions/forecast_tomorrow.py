from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from parts.eda.load_order_data import load_order_data

df = load_order_data('../generator/data')

# Krok 1: agregacja liczby części po dealerze i dacie (bez godziny)
df['order_date'] = df['order_datetime'].dt.date

daily_quantity = (
    df.groupby(['dealer', 'order_date'])['quantity']
    .sum()
    .reset_index()
)

# Wybierz dealera do prognozy
dealer_name = 'Dealer_1'
dealer_data = daily_quantity[daily_quantity['dealer'] == dealer_name].copy()

# Konwersja dat na liczby dni od startu
dealer_data['order_date'] = pd.to_datetime(dealer_data['order_date'])
dealer_data = dealer_data.sort_values('order_date')
dealer_data['day_num'] = (dealer_data['order_date'] - dealer_data['order_date'].min()).dt.days

# Dane treningowe
X = dealer_data[['day_num']].values
y = dealer_data['quantity'].values

# Model regresji liniowej
model = LinearRegression()
model.fit(X, y)

# Prognoza na jutro
next_day_num = dealer_data['day_num'].max() + 1
predicted_qty = model.predict([[next_day_num]])

print(f"Prognozowana liczba części na jutro dla {dealer_name}: {predicted_qty[0]:.0f}")
