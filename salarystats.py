import math

class SalaryStats:
    def __init__(self, data):
        self.data = data
        self.sorted_data = sorted(data)

    #центральные тенденции
    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        n = len(self.data)
        if n % 2 == 1:
            return self.sorted_data [n // 2]
        else:
            return (self.sorted_data[n // 2 - 1] + self.sorted_data[n // 2]) / 2

    def quantile(self, p):
        p_idx = int(p * len(self.data))
        return self.sorted_data[p_idx]

    #вариация
    def data_range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        x_mean = self.mean()
        deviations = sum((x - x_mean) ** 2 for x in self.data)
        return deviations / (len(self.data) - 1) if len(self.data) >= 2 else 0

    def standard_deviation(self):
        return math.sqrt(self.variance())

    def interquartile_range(self):
        return self.quantile(0.75) - self.quantile(0.25)

    def __str__(self):
        sep1 = "-" * 10 + " Центральные тенденции " + "-" * 10 + "\n"
        sep2 = "-" * 16 + " Вариация " + "-" * 17 + "\n"

        central_tend = (f"Средняя зарплата: {self.mean()}\n"
                      f"Медианная зарплата: {self.median()}\n"
                      f"10-й процентиль: {self.quantile(0.10)}\n"
                      f"25-й процентиль: {self.quantile(0.25)}\n"
                      f"50-й процентиль: {self.quantile(0.50)}\n"
                      f"75-й процентиль: {self.quantile(0.75)}\n"
                      f"90-й процентиль: {self.quantile(0.90)}\n")

        variation = (f"Размах: {self.data_range()}\n"
                     f"Дисперсия: {self.variance()}\n"
                     f"Стандартное отклонение: {self.standard_deviation()}\n"
                     f"Интерквартильный размах: {self.interquartile_range()}\n")

        return sep1 + central_tend + "\n" + sep2 + variation



salary_stats_rub = [20000, 40000, 100000, 250000, 120000, 63000, 1500000,
                    36000, 78000, 145000, 1350000, 24000, 87000, 53000]

total_salary_stats = SalaryStats(salary_stats_rub)
print(str(total_salary_stats))
