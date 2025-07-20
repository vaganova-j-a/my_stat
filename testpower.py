import numpy as np
from scipy.stats import norm
from statsmodels.stats.power import TTestPower

# Исходные параметры исследования
observed_corr = 0.825  # Наблюдаемая корреляция в сезоне NFL
n_observations = 24     # 6 лет × 4 месяца (сентябрь-декабрь)
alpha = 0.05            # Уровень значимости

# 1. Расчет через Z-преобразование Фишера (точный метод)
z_effect = 0.5 * np.log((1 + observed_corr) / (1 - observed_corr))
se = 1 / np.sqrt(n_observations - 3)
z_critical = norm.ppf(1 - alpha)  # Односторонний тест

# Вероятность ошибки второго рода (β)
beta = norm.cdf((z_critical - z_effect/se))
power = 1 - beta

# 2. Расчет через statsmodels (альтернативный метод)
effect_size = observed_corr  # Для корреляции Cohen's d ≈ r
analysis = TTestPower()
sm_power = analysis.solve_power(effect_size=effect_size,
                               nobs=n_observations,
                               alpha=alpha,
                               alternative='larger')

# Вывод результатов
print(f"   - Вероятность ошибки II рода (β): {beta:.6f} ({beta*100:.4f}%)")
print(f"   - Мощность теста (1-β): {power:.6f} ({power*100:.2f}%)")
