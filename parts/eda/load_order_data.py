import pandas as pd
import os
from glob import glob

def load_order_data(path: str) -> pd.DataFrame:
    """
    Wczytuje wszystkie pliki CSV z danego folderu, łączy je w jeden DataFrame.
    Parsuje kolumnę 'order_datetime' jako datę, jeśli istnieje.

    :param path: Ścieżka do folderu zawierającego pliki CSV
    :return: Jeden scalony DataFrame
    """
    # Wyszukiwanie plików .csv
    csv_files = glob(os.path.join(path, '*.csv'))
    if not csv_files:
        raise FileNotFoundError(f"Nie znaleziono plików CSV w folderze: {path}")

    print(f"🔍 Znaleziono {len(csv_files)} plików CSV w folderze: {path}")

    df_list = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if 'order_datetime' in df.columns:
                df['order_datetime'] = pd.to_datetime(df['order_datetime'])
            df_list.append(df)
        except Exception as e:
            print(f"⚠️ Błąd przy wczytywaniu {file}: {e}")

    if not df_list:
        raise ValueError("Nie udało się wczytać żadnych danych.")

    df_combined = pd.concat(df_list, ignore_index=True)
    print(f"✅ Wczytano {len(df_combined)} wierszy ze wszystkich plików.")
    return df_combined
