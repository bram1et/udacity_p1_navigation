"""
Utility functions to help in plotting various agent metrics.
"""

import numpy as np
import matplotlib.pyplot as plt

def sub_plot(coords, data, y_label='', x_label=''):
    """ Plot a single graph (subplot). """

    plt.subplot(coords)
    plt.plot(np.arange(len(data)), data)
    plt.ylabel(y_label)
    plt.xlabel(x_label)


def plot(scores, avg_scores, loss_list, entropy_list):
    """ Plot all data from training run. """

    plt.figure(1)
    # plot score
    sub_plot(231, scores, y_label='Score')
    sub_plot(232, avg_scores, y_label='Avg Score', x_label='Episodes')
    plt.show()