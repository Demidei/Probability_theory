import math
import scipy.stats
import statistics


#Задание 1: Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16. Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, если выборочная средняя M = 80, а объем выборки n = 256.

# Так как нам известна характеристика генеральной совокупности, мы можем взять формулу доверительного интервала через Z критерий - мат ожидание + критерий для половины альфы, умноженный на отношение сигмы к квадратному корню числа наблюдений


print("Задача 1 интервал математического ожидания - (" ,80 + scipy.stats.norm.ppf(0.05/2)*(16/math.sqrt(256)),",", 80 - scipy.stats.norm.ppf(0.05/2)*(16/math.sqrt(256)),")")

#Задание 2: В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей, оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95.

# Если я правильно понимаю, задача аналогична предыдущей, только нам не известна дисперсия или отклонение генеральной совокупности

a=[6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]

print("Задача 2 интервал математического ожидания - (" ,(sum(a)/len(a))  + scipy.stats.t.ppf(0.05/2, df=len(a)-1)*(statistics.stdev(a)/math.sqrt(len(a))),",",  (sum(a)/len(a)) - scipy.stats.t.ppf(0.05/2, df=len(a)-1)*(statistics.stdev(a)/math.sqrt(len(a))),")")

#Задание 3: .Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175 Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

# По аналогии с семинаром

a1=[175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
a2=[178, 165, 165, 173, 168, 155, 160, 164, 178, 175]

D=0.5*((statistics.stdev(a1)*statistics.stdev(a1))+(statistics.stdev(a2)*statistics.stdev(a2)))
Sd=math.sqrt((D/len(a1))+(D/len(a2)))


print("Задача 3 интервал разности математического ожидания - (",((sum(a1)/len(a1))-(sum(a2)/len(a2)))+Sd*scipy.stats.t.ppf(0.05/2,(len(a1)-1)+(len(a2)-1)) ,",",((sum(a1)/len(a1))-(sum(a2)/len(a2)))-Sd*scipy.stats.t.ppf(0.05/2,(len(a1)-1)+(len(a2)-1))  ,")")

