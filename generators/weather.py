import numpy as np
rng = np.random.default_rng(12)
with open("../csv/weather.csv","w") as fout:
    fout.write("weather,\n")
    for i in range(100):
        if rng.uniform() <0.1:
            fout.write(f"sunny\n")
        elif rng.uniform()<0.5:
            fout.write(f"cloudy\n")
        elif rng.uniform()<0.8:
            fout.write(f"rainy\n")
        else:
            fout.write(f"windy\n")