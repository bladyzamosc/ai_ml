from parts.eda.load_order_data import load_order_data

df = load_order_data('../generator/data')
df['part_id'] = df['part_prefix'].astype(str) + '-' + df['part_number'].astype(str)
part_totals = (
    df.groupby('part_id')['quantity']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
top_10_parts = part_totals.head(10)
print(top_10_parts)