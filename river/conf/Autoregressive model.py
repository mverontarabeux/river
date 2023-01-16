
import matplotlib.pyplot as plt

class AutoregressiveModels():

    """Auto regressive (1) model.

    The autoregressive model specifies that the output variable depends linearly on its own previous values and on a stochastic term.

    Parameters
    ----------
    window_size
        The size of the window used to compute the process.
    """

    def __init__(self, window_size) -> None:
         #self.parameters = p
         self.window_size = window_size

    
    def process(self, start):

        x = [0]

        for t in range(start+1,self.window_size):
            x.append(0.5*x[t-1] + np.random.rand())

        return x

    
    def plot_process(self, x):

        plt.plot(x,label="AR(1) process")
        plt.title("Autoregressive (AR) Model")
        plt.legend()
        plt.show()