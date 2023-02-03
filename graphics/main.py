from utils import Stat
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


stats = Stat.read_csv('stats_code.csv')
stats_2 = Stat.read_csv('stats_firefox.csv')
stats_3 = Stat.read_csv('stats_f2.csv')


cpu_stats = Stat.get_for_matplotlib(stats, 'cpu')
cpu_stats_2 = Stat.get_for_matplotlib(stats_2, 'cpu')
cpu_stats_3 = Stat.get_for_matplotlib(stats_3, 'cpu')


def lines(lines, labels, attr):
    # fig = plt.figure()  # an empty figure with no Axes
    fig, ax = plt.subplots()  # a figure with a single Axes
    handles = []
    # fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

    for i in range(len(lines)):
        ll, = ax.plot(lines[i]['x'], lines[i]['y'], label = labels[i])
        handles.append(ll)

    ax.legend(handles = handles)
    ax.set_xlabel("Seconds")
    ax.set_ylabel(attr)
    # plt.ylim([0, 400])
    plt.show()


def get_colors(length):
    colors = ['tab:blue', 'tab:red', 'tab:green', 'tab:orange', 'k', 'w']
    return colors[:length]

def bars(vals, labels, attr):
    fig, ax = plt.subplots()  # a figure with a single Axes
    ax.bar(labels, vals, color = get_colors(len(vals)))
    ax.set_ylabel(attr)
    plt.show()


# lines([cpu_stats, cpu_stats_2], ['code', 'firefox'], '%CPU usage')

avg_cpu = Stat.get_average(stats, 'cpu')
avg_cpu_2 = Stat.get_average(stats_2, 'cpu')
avg_cpu_3 = Stat.get_average(stats_3, 'cpu')

bars([avg_cpu, avg_cpu_2, avg_cpu_3], ['code', 'firefox', 'firefox2'], 'Average CPU usage')


