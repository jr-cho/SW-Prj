import numpy as np
import matplotlib.pyplot as plt

def plot():
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('Angle (radians)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot()
