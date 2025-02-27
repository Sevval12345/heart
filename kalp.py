# -*- coding: utf-8 -*-
"""kalp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1inPvRcv54NhCLieuffuQEcuPHLZEGwcd
"""

!apt install xvfb
!pip install pyvirtualdisplay
!apt install ghostscript

--------------------------------------------------------------------------------------
#Kalp ama resim

import matplotlib.pyplot as plt
import numpy as np

def corazon(n):
  x = 16 * np.sin(n) ** 3
  y = 13 * np.cos(n) - 5 * np.cos(2 * n) - 2 * np.cos(3 * n) - np.cos(4 * n)
  return x, y

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_facecolor('black')

for i in range(15):
  x_vals = []
  y_vals = []
  for n in range(0, 100, 2):
    x, y = corazon(n/10)
    x_vals.append(x*i)
    y_vals.append(y*i)
  ax.plot(x_vals, y_vals, color='red')

plt.show()


---------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Kalp şekli koordinatlarını tanımlayan fonksiyon
def corazon(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# Animasyon için figür ve eksenler oluşturma
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Kalp çizgileri için birden fazla çizgi objesi tanımlama
lines = [ax.plot([], [], color='red', lw=1)[0] for _ in range(10)]

# Animasyonun başlangıç durumu
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Her kare için güncelleme fonksiyonu
def update(frame):
    t = np.linspace(0, 2 * np.pi, 500)  # Kalp şekli için açı aralığı
    for i, line in enumerate(lines):
        scale = (frame % 50) / 50 + i * 0.2  # Boyut çarpanı, iç içe kalpler için ayarlanır
        x, y = corazon(t)
        x_scaled = x * scale
        y_scaled = y * scale
        line.set_data(x_scaled, y_scaled)
    return lines

# Animasyonu oluşturma
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# Animasyonu gösterme
plt.show()
ani.save("kalp.mp4", writer="ffmpeg")
