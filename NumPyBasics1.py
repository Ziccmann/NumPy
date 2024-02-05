import numpy as np


monthly_temperatures = np.array([20.5, 22.1, 25.3, 28.7, 30.2, 32.8, 34.5, 33.6, 31.8, 28.4, 24.7, 21.2])

mean_temperature = np.mean(monthly_temperatures)
median_temperature = np.median(monthly_temperatures)
std_temperature = np.std(monthly_temperatures)

print('Mean Temperature =', mean_temperature)
print('Median Temperature =', median_temperature)
print('Std Temperature =', std_temperature)

mounths_temperatures_above_average = monthly_temperatures > mean_temperature
print('Months With Temperature Above The Annual Average =', mounths_temperatures_above_average)

quarterly_temperatures = monthly_temperatures.reshape(4, 3)


average_temperature_per_quarter = np.mean(quarterly_temperatures, axis=1)

print("Quarterly Temperatures (2D Array):")
print(quarterly_temperatures)
print("Average Temperature for Each Quarter:", average_temperature_per_quarter)