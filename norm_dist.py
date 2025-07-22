import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import os

# Создаем папку для сохранения графиков, если её нет
if not os.path.exists('graphs'):
    os.makedirs('graphs')

# Загрузка данных
avocado = pd.read_csv('avocado_sales_2018_2023_rise.csv')
nfl = pd.read_csv('football_viewers_2018_2023_rise.csv')

# Объединение данных
merged = pd.merge(avocado, nfl, on=['Год', 'Месяц'])
sales = merged['Средние_продажи_тонн']
viewers = merged['Средние_зрители_млн']


# Функция для построения и сохранения гистограммы
def plot_and_save_hist(data, title, xlabel, filename, color='skyblue'):
    plt.figure(figsize=(10, 6))

    # Гистограмма
    plt.hist(data, bins=20, density=True, alpha=0.6, color=color,
             edgecolor='black', label='Реальные данные')

    # Кривая нормального распределения
    mu, sigma = np.mean(data), np.std(data)
    x = np.linspace(min(data), max(data), 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r--', linewidth=2,
             label='Нормальное распределение')

    plt.title(f'Распределение {title}\nμ={mu:.1f}, σ={sigma:.1f}', fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel('Плотность вероятности', fontsize=12)
    plt.legend(fontsize=12, framealpha=0.9)
    plt.grid(True, linestyle='--', alpha=0.5)

    # Сохранение графика
    plt.savefig(f'graphs/{filename}.png', dpi=300, bbox_inches='tight')
    plt.show()
    print(f'График сохранён как: graphs/{filename}.png')


# Построение и сохранение графиков
plot_and_save_hist(sales, 'продаж авокадо', 'Продажи (тонн)',
                   'avocado_sales_distribution', 'lightgreen')

plot_and_save_hist(viewers, 'просмотров NFL', 'Просмотры (млн)',
                   'nfl_viewers_distribution', 'lightcoral')