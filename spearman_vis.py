import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import os

# Создаем папку для графиков
os.makedirs('graphs', exist_ok=True)

# Загрузка данных
avocado = pd.read_csv('avocado_sales_2018_2023_rise.csv')
nfl = pd.read_csv('football_viewers_2018_2023_rise.csv')

# Фильтрация по сезону NFL (сентябрь-февраль)
season_months = ['Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'Январь', 'Февраль']
avocado_season = avocado[avocado['Месяц'].isin(season_months)]
nfl_season = nfl[nfl['Месяц'].isin(season_months)]

# Объединение данных
merged = pd.merge(avocado_season, nfl_season, on=['Год', 'Месяц'])
sales = merged['Средние_продажи_тонн']
viewers = merged['Средние_зрители_млн']

# Расчет корреляции Спирмена
r, p = spearmanr(sales, viewers)

# Настройка стиля (используем актуальный стиль Seaborn)
plt.style.use('seaborn-v0_8')  # Совместимый стиль для новых версий
sns.set_style("whitegrid")  # Дополнительная настройка через Seaborn

# Создание фигуры
plt.figure(figsize=(10, 6))

# График рассеяния с линией тренда
scatter = sns.regplot(x=sales, y=viewers,
                     scatter_kws={'alpha':0.6, 'color':'royalblue', 's':80},
                     line_kws={'color':'red', 'linestyle':'--', 'linewidth':2})

# Добавление заголовка и подписей
plt.title(f'Корреляция Спирмена: Продажи авокадо vs Просмотры NFL (сезон: сент-фев)\n'
          f'r = {r:.3f}, p-value = {p:.4f}', fontsize=14, pad=20)
plt.xlabel('Продажи авокадо (тонн)', fontsize=12)
plt.ylabel('Просмотры NFL (млн)', fontsize=12)

# Улучшение отображения сетки
plt.grid(True, linestyle='--', alpha=0.5)

# Добавление аннотации с коэффициентом
plt.annotate(f'Spearman r = {r:.3f}\np-value = {p:.4f}',
             xy=(0.7, 0.1), xycoords='axes fraction',
             bbox=dict(boxstyle='round', fc='white', ec='gray', alpha=0.8))

# Сохранение графика
plt.savefig('graphs/spearman_nfl_season.png', dpi=300, bbox_inches='tight')
print("График сохранен: graphs/spearman_nfl_season.png")

# Показать график
plt.tight_layout()
plt.show()