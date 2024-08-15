import numpy as np
from scipy import stats


wastewater, *deaths = np.genfromtxt(
    f"wastewater_deaths0-8.csv", delimiter=",", skip_header=1, unpack=True
)

for i, d in enumerate(deaths):
    r = stats.pearsonr(wastewater, d)
    print(f"offset {i}:", r.statistic, r.pvalue)
