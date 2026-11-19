import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import math
import pandas as pd
import pulp
from datetime import datetime, timedelta
maker_style = [
                'o',
                's',
                'd',
                '*',
                '^',
                'p',
                'X',
                'P',
                'v'
                
                ]
hex_colors_bw = [
    "#565656",
    "#6B6B6B",
    "#808080",
    "#969696",
    "#ACACAC",
    "#C2C2C2",
    "#D8D8D8"
            ]
hex_colors = [
    "#67000D",
    "#A50F15",
    "#CB181D",
    "#EF3B2C",
    "#FB6A4A",
    "#FC9272",
    "#FCBBA1",
    "#FEE0D2"
    ]
hex_colors_blue = [
    "#08306b",
    "#08519c",
    "#2171b5",
    "#4292c6",
    "#6baed6",
    "#9ecae1",
    "#c6dbef",
    "#deebf7"
    ]

if __name__ == '__main__':

    # load data
    data_frame_1 = pd.read_csv('20261117/NewFile3.csv', dtype={"Second":float, "Volt":float, "c":str}, delimiter=',', skiprows=1)
    x = data_frame_1['Second']
    y = data_frame_1['Volt']

    # Set font to sans-serif for a scientific look
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'xtick.labelsize': 14,
        'ytick.labelsize': 16,
        'legend.fontsize': 14,
        'lines.linewidth': 1.5,
        'lines.markersize': 6,
        'mathtext.fontset': 'cm',
    })  
    
    # plot data
    fig1, ax = plt.subplots(figsize=(10, 8))

    #3He
    ax.plot((x+5e-6),(y-0.00015), label='Signal 3He tube', marker=maker_style[0],linestyle='-',color=hex_colors_bw[0])
    
    # Add labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (V)')
    plt.title('')
    #plt.xlim(0,5.250) # X-axis from  to 
    #plt.ylim(0,130)  # Y-axis from  to 
    
    # Scientific notation on both axes
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    ax.ticklabel_format(style='sci', axis='both', scilimits=(-9,0))
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    

    # Add grid, minor ticks, and legend
    ax.grid(True, which='major', linestyle='-', alpha=0.3)
    ax.minorticks_on()
    ax.grid(True, which='minor', linestyle=':', alpha=0.2)
    ax.legend(loc='upper right',frameon=False)

    # Show the plot
    plt.tight_layout()
    plt.show()
