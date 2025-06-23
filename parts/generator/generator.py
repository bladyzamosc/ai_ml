import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Parametry
NUM_DEALERS = 20
MIN_BU_PER_DEALER = 1
MAX_BU_PER_DEALER = 4

MIN_ORDERS_PER_DAY = 10
MAX_ORDERS_PER_DAY = 40

MIN_PARTS_PER_ORDER = 1
MAX_PARTS_PER_ORDER = 1000

NUM_PART_PREFIXES = 5  # np. 50 różnych prefixów części
MAX_PART_NUMBER = 3000  # numer części w prefixie, tak aby razem było 15k części

MIN_QTY_PER_PART = 1
MAX_QTY_PER_PART = 1000

DAYS_TO_GENERATE = 7
START_DATE = datetime(2025, 6, 15)

# Generujemy dealerów
dealers = [f'Dealer_{i+1}' for i in range(NUM_DEALERS)]

# Generujemy business units (BU) i przypisujemy im gci_number
dealer_to_bu = {}
gci_counter = 100000  # zaczynamy numerację gci_number od 100000 (dla business units)

for dealer in dealers:
    num_bu = np.random.randint(MIN_BU_PER_DEALER, MAX_BU_PER_DEALER+1)
    bu_list = []
    for _ in range(num_bu):
        bu_list.append(str(gci_counter))
        gci_counter += 1
    dealer_to_bu[dealer] = bu_list

# Generujemy prefixy części, np. litery lub "P1", "P2", ...
part_prefixes = [f'P{num}' for num in range(1, NUM_PART_PREFIXES+1)]

# Funkcja do losowania liczby części w zamówieniu (głównie 2-10)
def sample_num_parts():
    if np.random.rand() < 0.7:
        return np.random.randint(2, 11)
    else:
        return np.random.randint(11, MAX_PARTS_PER_ORDER+1)

rows = []
order_id_counter = 1

for day_offset in range(DAYS_TO_GENERATE):
    current_date = START_DATE + timedelta(days=day_offset)
    for dealer in dealers:
        bus_units = dealer_to_bu[dealer]
        orders_today = np.random.randint(MIN_ORDERS_PER_DAY, MAX_ORDERS_PER_DAY+1)
        for _ in range(orders_today):
            # wybieramy BU i jego gci_number
            bu = np.random.choice(bus_units)
            num_parts = sample_num_parts()

            # losujemy prefixy i numery części
            prefixes = np.random.choice(part_prefixes, size=num_parts)
            numbers = np.random.randint(1, MAX_PART_NUMBER+1, size=num_parts)

            qtys = np.random.randint(MIN_QTY_PER_PART, MAX_QTY_PER_PART+1, size=num_parts)

            order_time = current_date + timedelta(seconds=np.random.randint(0, 86400))
            order_id = f'ORD_{order_id_counter}'
            order_id_counter += 1

            for prefix, number, qty in zip(prefixes, numbers, qtys):
                rows.append({
                    'order_id': order_id,
                    'dealer': dealer,
                    'gci_number_business_unit': bu,
                    'order_datetime': order_time,
                    'part_prefix': prefix,
                    'part_number': number,
                    'quantity': qty
                })

df = pd.DataFrame(rows)

print(f'Wygenerowano {len(df)} pozycji zamówień.')
print(df.head())

# Możesz zapisać plik do CSV, jeśli chcesz:
df.to_csv('data\synthetic_orders_v2.csv', index=False)
