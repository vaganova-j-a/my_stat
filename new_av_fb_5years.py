import pandas as pd

# Загрузка данных
avocado = pd.read_csv('avocado_sales_2018_2023_rise.csv')
nfl = pd.read_csv('football_viewers_2018_2023_rise.csv')

# Фильтрация по сезону NFL
season_months = ['Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'Январь', 'Февраль']
avocado_season = avocado[avocado['Месяц'].isin(season_months)]
nfl_season = nfl[nfl['Месяц'].isin(season_months)]

# Объединение данных
merged = pd.merge(avocado_season, nfl_season, on=['Год', 'Месяц'])
sales = merged['Средние_продажи_тонн']
viewers = merged['Средние_зрители_млн']

from scipy.stats import spearmanr

# Расчёт корреляции Спирмена
r_spearman, p_value = spearmanr(sales, viewers)

print(f"Коэффициент Спирмена (r): {r_spearman:.3f}")
print(f"p-value: {p_value:.5f}")

import matplotlib.pyplot as plt
import numpy as np

# Ранжирование данных
rank_sales = sales.rank()  # Ранги продаж
rank_viewers = viewers.rank()  # Ранги просмотров

# Построение графика
plt.figure(figsize=(8, 6))
plt.scatter(rank_sales, rank_viewers, alpha=0.7, color='blue')
plt.title("График рассеяния с рангами (корреляция Спирмена)")
plt.xlabel("Ранг продаж авокадо")
plt.ylabel("Ранг просмотров NFL")
plt.grid(True)

# Линия тренда (показывает направление связи)
z = np.polyfit(rank_sales, rank_viewers, 1)
p = np.poly1d(z)
plt.plot(rank_sales, p(rank_sales), color='red', linestyle='--')

plt.show()