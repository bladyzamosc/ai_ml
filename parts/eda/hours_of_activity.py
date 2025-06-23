import matplotlib
matplotlib.use('Agg')  # renderowanie bez GUI

from parts.eda.load_order_data import load_order_data
import matplotlib.pyplot as plt
import seaborn as sns

df = load_order_data('../generator/data')
df['order_hour'] = df['order_datetime'].dt.hour
df['day_of_week'] = df['order_datetime'].dt.dayofweek
df['day_name'] = df['order_datetime'].dt.day_name()

heatmap_data = (
    df.groupby(['day_of_week', 'order_hour'])['order_id']
    .nunique()
    .unstack(fill_value=0)
)

plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=0.3, linecolor='white', annot=True, fmt='d')

plt.title('Heatmapa: Aktywność zakupowa (dzień tygodnia × godzina)')
plt.xlabel('Godzina (0–23)')
plt.ylabel('Dzień tygodnia (0 = pon, 6 = niedz)')
plt.yticks(ticks=range(7), labels=['Pon', 'Wt', 'Śr', 'Czw', 'Pt', 'Sob', 'Niedz'], rotation=0)
plt.tight_layout()

# ZAPIS do pliku
plt.savefig('trash\heatmap_hours_vs_days.png', dpi=150)
