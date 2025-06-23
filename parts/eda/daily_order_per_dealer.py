from parts.eda.load_order_data import load_order_data

df = load_order_data('../generator/data')

df['order_date'] = df['order_datetime'].dt.date

orders_per_day = (
    df.groupby(['dealer', 'order_date'])['order_id']
    .nunique()
    .reset_index(name='num_orders')
)

print(orders_per_day.head(10))
