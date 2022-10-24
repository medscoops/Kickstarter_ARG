# use with:
#    import graph_snippets or from graph_snippets import line_plot, bar_plot

import matplotlib.pyplot as plt
import seaborn as sns
import sys



def line_plot(df, x, y, figsize=(16,10), xlabel=None, ylabel=None, fontsize=12, legend_label=None, title=None, library="plt"):
    
    if library == "plt":
        plt.figure(figsize=figsize)
        plt.plot(x, y, label=legend_label)
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)
        plt.xticks(rotation=45, horizontalalignment='right', fontsize=11)
        plt.yticks(fontsize=11)
        plt.title(title, fontsize=fontsize)
        plt.legend(loc='upper left', fontsize=fontsize)
        plt.show();
    
    elif library == "sns":
        plt.figure(figsize=figsize)
        sns.lineplot(x=x, y=y, data=df, label=legend_label)
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)
        plt.xticks(rotation=45, horizontalalignment='right', fontsize=11)
        plt.yticks(fontsize=11)
        plt.title(title, fontsize=fontsize)
        plt.legend(loc='upper left', fontsize=fontsize)
        plt.show();



def bar_plot(df, x, y, figsize=(16,10), xlabel=None, ylabel=None, fontsize=12, legend_label=None, title=None, library="plt", hue=None):
    """_summary_

    Args:
        df (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
        figsize (tuple, optional): _description_. Defaults to (16,10).
        xlabel (_type_, optional): _description_. Defaults to None.
        ylabel (_type_, optional): _description_. Defaults to None.
        fontsize (int, optional): _description_. Defaults to 12.
        legend_label (_type_, optional): _description_. Defaults to None.
        title (_type_, optional): _description_. Defaults to None.
        library (str, optional): _description_. Defaults to "plt".
        hue (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    Or shows graph.
    """
    if library == "plt" and hue==None:
        plt.figure(figsize=figsize)
        plt.bar(x = x, height = y, label=legend_label)
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)
        plt.title(title, fontsize=20)
        plt.show();
    elif library == "plt" and hue != None:
        sys.stderr.write("No argument 'hue' in Matplotlib bar plot.")
    elif library == "sns":
        plt.figure(figsize=figsize)
        sns.barplot(x=x, y=y, data=df, hue=hue)
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.ylabel(ylabel, fontsize=fontsize)
        plt.title(title, fontsize=20)
        plt.legend(loc='upper left', fontsize=13)
        plt.show(); # or return plot

