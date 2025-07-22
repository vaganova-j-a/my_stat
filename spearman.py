import pandas as pd
import scipy.stats as stats

# Загрузка данных
avocado = pd.read_csv('avocado_sales_2018_2023_rise.csv', encoding='utf-8')
football = pd.read_csv('football_viewers_2018_2023_rise.csv', encoding='utf-8')


# Функция для расчёта корреляции по заданным месяцам
def calculate_spearman(months_list, period_name):
    # Фильтрация данных
    avocado_filtered = avocado[avocado['Месяц'].isin(months_list)]
    football_filtered = football[football['Месяц'].isin(months_list)]

    # Объединение данных
    merged_data = pd.merge(
        avocado_filtered[['Год', 'Месяц', 'Средние_продажи_тонн']],
        football_filtered[['Год', 'Месяц', 'Средние_зрители_млн']],
        on=['Год', 'Месяц']
    )

    # Расчёт корреляции Спирмена
    correlation, p_value = stats.spearmanr(
        merged_data['Средние_продажи_тонн'],
        merged_data['Средние_зрители_млн']
    )

    # Вывод результатов
    print(f"\nАнализ за период: {period_name}")
    print(f"Корреляция Спирмена: {correlation:.3f}")
    print(f"P-значение: {p_value:.3f}")
    print("\nПример данных:")
    print(merged_data.head(6))  # Вывод первых 6 строк для наглядности


# Расчёт для Сентябрь–Ноябрь
calculate_spearman(['Сентябрь', 'Октябрь', 'Ноябрь'], "Сентябрь–Октябрь–Ноябрь")

# Расчёт для Декабрь–Февраль
calculate_spearman(['Декабрь', 'Январь', 'Февраль'], "Декабрь–Январь–Февраль")