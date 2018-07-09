import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


figures_directory='Figures';

class PlotService:
    def __init__(self):
        pass;


    def plot_bar_graph(self,labels,values,figure_name,title,x_label):
        objects = labels
        y_pos = np.arange(len(objects))
        performance = values

        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel(x_label)
        plt.title(title)
        plt.savefig(figures_directory + '/'+figure_name)
        print('plot');
        pass;