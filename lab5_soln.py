from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0,1,500,endpoint=False)

plt.plot(t, signal.square(2 * np.pi * 5 * t))

plt.show()
