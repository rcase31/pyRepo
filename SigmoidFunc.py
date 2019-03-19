from math import e
import matplotlib.pyplot as plt


def sigmoid(x):
    """
    Sigmoid function. Accepts either single value or lists.
    :param x: single value or list.
    :return: single value or list.
    """
    if isinstance(x, list):
        out = []
        for elem in x:
            out.append(sigmoid(elem))
        return out
    else:
        return 1 / (1 + e ** (-x))


def d_sigmoid(x):
    """
    Derivative of sigmoid function. Accepts either single value or lists.
    :param x: single value or list.
    :return: single value or list.
    """
    if isinstance(x, list):
        out = []
        for elem in x:
            out.append(d_sigmoid(elem))
        return out
    else:
        sig = sigmoid(x)
        return sig * (1 - sig)


if __name__ == '__main__':
    x_interval = [i/6 for i in range(-60, 60)]
    y_interval = sigmoid(x_interval)
    delta_y_interval = d_sigmoid(x_interval)
    plt.plot(x_interval, delta_y_interval)
    plt.plot(x_interval, y_interval)
