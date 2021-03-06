# coding: utf-8

from matplotlib import pyplot

decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='->')


def plot_node(node_text, center_pt, parent_pt, node_type):
    create_plot.ax1.annotate(node_text, xy=parent_pt, xycoords='axes fraction', xytext=center_pt,
                             textcoords='axes fraction', va='center', ha='center', bbox=node_type,
                             arrowprops=arrow_args)


def create_plot():
    fig = pyplot.figure(1, facecolor='white')
    fig.clf()
    create_plot.ax1 = pyplot.subplot(111, frameon=False)
    plot_node('Decision Node', (0.5, 0.1), (0.1, 0.5), decision_node)
    plot_node('Leaf Node', (0.8, 0.1), (0.3, 0.8), leaf_node)
    pyplot.show()


create_plot()
