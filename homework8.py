import math
import scipy.stats
import statistics
import numpy as np

#Задание 1: Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy Полученные значения должны быть равны. Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])

ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Казалось бы -все должно быть просто, но у меня возникли сложности практически сразу
print("Задача 1 автоматически вычисленная ковариация -",np.cov(zp,ks))

# Я попробовал вычислить значение ковариации вручную разными способами, но эти значения разошлись с автоматически вычисленным

print("Задача 1 вычисленние ковариации -",np.mean(zp*ks)-(np.mean(zp)*np.mean(ks)))

cov=0
i=0
while i < len(zp):
        cov=cov+(zp[i]-(sum(zp)/len(zp)))*(ks[i]-(sum(ks)/len(ks)))
        i += 1

print("Задача 1 альтернативное вычисленние ковариации -",cov/len(zp))

# В условии задачи сказано, что ковариации должны сойтись. Видимо я что-то не понимаю

# Тем не менее, при вычислении корреляции от ковариации, полученной "вручную", если в функции std взять ddof=0 результаты совпадают с автоматически вычисленным 

print("Задача 1 автоматически вычисленная корреляция -",np.corrcoef(zp,ks))

print("Задача 1 вычисление корреляция -",(np.mean(zp*ks)-(np.mean(zp)*np.mean(ks)))/(np.std(zp,ddof=0)*np.std(ks,ddof=0)))



#Задание 2: Измерены значения IQ выборки студентов, обучающихся в местных технических вузах: 131, 125, 115, 122, 131, 115, 107, 99, 125, 111. Известно, что в генеральной совокупности IQ распределен нормально. Найдите доверительный интервал для математического ожидания с надежностью 0.95.

# Используем формулу доверительного интервала через t критерий

a=[131, 125, 115, 122, 131, 115, 107, 99, 125, 111]

print("Задача 2 интервал математического ожидания - (" ,np.mean(a)  + scipy.stats.t.ppf(0.05/2, df=len(a)-1)*(statistics.stdev(a)/math.sqrt(len(a))),",",  np.mean(a) - scipy.stats.t.ppf(0.05/2, df=len(a)-1)*(statistics.stdev(a)/math.sqrt(len(a))),")")

#Задание 3: Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2. Найдите доверительный интервал для математического ожидания с надежностью 0.95.

# Используем формулу доверительного интервала через Z критерий

avg=174.2
n=27
std=5

print("Задача 3 интервал математического ожидания - (" ,avg  + scipy.stats.norm.ppf(0.05/2)*(std/math.sqrt(n)),",",  avg - scipy.stats.norm.ppf(0.05/2)*(std/math.sqrt(n)),")")

