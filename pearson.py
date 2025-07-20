import pandas as pd

# Загрузка данных
avocado = pd.read_csv('avocado_sales_2018_2023_rise.csv')
football = pd.read_csv('football_viewers_2018_2023_rise.csv')

# Объединение данных
merged = pd.merge(avocado, football, on=['Год', 'Месяц'])

# 1. Общая корреляция по всем месяцам
total_corr = merged[['Средние_продажи_тонн', 'Средние_зрители_млн']].corr().iloc[0,1]

# 4. Корреляция для сезона NFL (сентябрь-декабрь)
nfl_season = merged[merged['Месяц'].isin(['Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'])]
nfl_corr = nfl_season[['Средние_продажи_тонн', 'Средние_зрители_млн']].corr().iloc[0,1]

print(f"Общая корреляция: {total_corr:.3f}")
print(f"Сезон NFL: {nfl_corr:.3f}")