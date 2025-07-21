import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import locale

# Устанавливаем русскую локаль для дат (хотя теперь она не нужна)
try:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
except:
    locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')

# Загрузка данных
avocado = pd.read_csv('avocado_sales_2018_2023_rise.csv')
football = pd.read_csv('football_viewers_2018_2023_rise.csv')

# Функция для преобразования русских месяцев в даты
def create_date(row):
    months_ru = {
        'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6,
        'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
    }
    return datetime(row['Год'], months_ru[row['Месяц']], 15)

# Создаем столбец с датами
avocado['Дата'] = avocado.apply(create_date, axis=1)
football['Дата'] = football.apply(create_date, axis=1)

# Объединение данных
merged = pd.merge(avocado, football, on=['Год', 'Месяц', 'Дата'], how='left')

# Создание графика
plt.figure(figsize=(16, 8))

# График продаж авокадо
ax1 = plt.gca()
line1 = ax1.plot(merged['Дата'], merged['Средние_продажи_тонн'],
                color='#2ecc71', label='Продажи авокадо (тонн)',
                marker='o', markersize=6, linewidth=2.5)

ax1.set_xlabel('Дата', fontsize=12, fontweight='bold')
ax1.set_ylabel('Продажи авокадо (тонн)', color='#2ecc71',
              fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#2ecc71')
ax1.set_ylim(0, max(merged['Средние_продажи_тонн']) * 1.1)

# График зрителей футбола
ax2 = ax1.twinx()
line2 = ax2.plot(merged['Дата'], merged['Средние_зрители_млн'],
                color='#3498db', label='Зрители футбола (млн)',
                marker='s', markersize=6, linewidth=2.5)

ax2.set_ylabel('Зрители футбола (млн)', color='#3498db',
              fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#3498db')
ax2.set_ylim(0, max(merged['Средние_зрители_млн']) * 1.1)

# Настройка оси X - форматируем только как номер месяца без ведущего нуля
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%-m'))  # %-m убирает ведущий ноль
plt.xticks(rotation=0, fontsize=10)

# Заголовок и легенда
plt.title('Динамика продаж авокадо и просмотров футбола (2018-2023)',
         fontsize=14, pad=20, fontweight='bold')

# Объединение легенд
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10, framealpha=1)

# Сетка
ax1.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
#изменение файла