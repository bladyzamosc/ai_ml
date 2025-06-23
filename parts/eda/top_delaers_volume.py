from parts.eda.load_order_data import load_order_data

df = load_order_data('../generator/data')

dealer_bu_volume = (
    df.groupby(['dealer', 'gci_number_business_unit'])['quantity']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

top_10_bu = dealer_bu_volume.head(10)
print(top_10_bu)