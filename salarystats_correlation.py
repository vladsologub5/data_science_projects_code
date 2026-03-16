import math

class SalaryStatsCorrelation:
    def __init__(self, data_1, data_2):
        self.data_1 = data_1
        self.data_2 = data_2
        self.sorted_data_1 = sorted(self.data_1)
        self.sorted_data_2 = sorted(self.data_2)

    def mean(self):
        return (sum(self.data_1) / len(self.data_1),
                sum(self.data_2) / len(self.data_2))

    def median(self):
        n_1 = len(self.data_1)
        n_2 = len(self.data_2)
        if n_1 % 2 == 1 or n_2 % 2 == 1:
            return (self.sorted_data_1[n_1 // 2],
                    self.sorted_data_2[n_2 // 2])
        else:
            return ((self.sorted_data_1[n_1 // 2 - 1] + self.sorted_data_1[n_1 //2]) / 2,
                    (self.sorted_data_2[n_2 // 2 - 1] + self.sorted_data_2[n_2 // 2]) / 2)

    def quantile(self, p):
        p_idx_1 = int(p * len(self.data_1))
        p_idx_2 = int(p * len(self.data_2))
        return (self.sorted_data_1[p_idx_1],
                self.sorted_data_2[p_idx_2])

    def covariance(self):
        assert len(self.data_1) == len(self.data_2)

        x_mean = sum(self.data_1) / len(self.data_1)
        y_mean = sum(self.data_2) / len(self.data_2)
        return sum((x_1 - x_mean) * (x_2 - y_mean)
                   for x_1, x_2 in zip(self.data_1, self.data_2)) / (len(self.data_1) - 1)

    def correlation(self):
        assert len(self.data_1) == len(self.data_2)

        x_mean = sum(self.data_1) / len(self.data_1)
        y_mean = sum(self.data_2) / len(self.data_2)

        variance_1 = sum((x_1 - x_mean) ** 2 for x_1 in self.data_1) / (len(self.data_1) - 1)
        variance_2 = sum((x_2 - y_mean) ** 2 for x_2 in self.data_2) / (len(self.data_2) - 1)

        std_x = math.sqrt(variance_1)
        std_y = math.sqrt(variance_2)
        if std_x > 0 and std_y > 0:
            return self.covariance() / std_x / std_y
        else:
            return 0

    def __str__(self):
        str_1 =  "-" * 10 + " Центральные тенденции " + "-" * 10 + "\n"
        str_2 = "-" * 15 + " Корреляция " + "-" * 16 + "\n"

        central_tend = (f"Среднее арифметическое: {self.mean()}\n"
                        f"Медиана: {self.median()}\n"
                        f"10-й процентиль: {self.quantile(0.10)}\n"
                        f"25-й процентиль: {self.quantile(0.25)}\n"
                        f"50-й процентиль: {self.quantile(0.50)}\n"
                        f"75-й процентиль: {self.quantile(0.75)}\n"
                        f"90-й процентиль: {self.quantile(0.90)}\n")

        correlation = (f"Ковариация: {self.covariance()}\n"
                       f"Корреляция: {self.correlation()}\n")

        return str_1 + central_tend + "\n" + str_2 + correlation

salary_stats_rub = [20000, 40000, 100000, 250000, 120000, 63000, 1500000,
                    36000, 78000, 145000, 1350000, 24000, 87000, 53000]

experience_year = [0.5, 1, 3, 6, 4, 2, 7,
                   3, 5.5, 6.5, 9, 1, 4, 2.5]

total_correlation = SalaryStatsCorrelation(salary_stats_rub, experience_year)
print(str(total_correlation))