import numpy as np
rng = np.random.default_rng(12)
with open("../csv/weather.txt","w") as fout:
    fout.write("iteration,weather,\n")
    for i in range(100):
        if rng.uniform() <0.1:
            fout.write(f"{i},sunny,\n")
        elif rng.uniform()<0.5:
            fout.write(f"{i},cloudy,\n")
        elif rng.uniform()<0.8:
            fout.write(f"{i},rainy,\n")
        else:
            fout.write(f"{i},windy,\n")