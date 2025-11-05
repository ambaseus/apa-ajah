import numpy as np

suhu_c = np.array([22, 19, 17, 20, 22, 23, 21, 19, 22, 24])
suhu_f = (suhu_c * 9/5) + 32

print("suhu celcius: ", suhu_c)
print("suhu fahrenheit: ", suhu_f)
