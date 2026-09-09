import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

maker_style = [
                'o',
                's',
                'D',
                'P',
                'X',
                'p',
                '^'
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
    data_set1 = np.loadtxt('neutronabsorption_NIST.txt',skiprows=1)
    lambda_ang = data_set1[:,0]
    Helium3 = data_set1[:,1]
    LiF = data_set1[:,2]

    data_set2 = np.loadtxt('neutronabsorption_LDN.txt',skiprows=1)
    lambda_ang_1 = data_set2[:,0]
    Helium3_1 = data_set2[:,1]

    data_set3 = np.loadtxt('neutronabsorption_ref1.txt',skiprows=1)
    lambda_ang_2 = data_set3[0]
    LiF_2 = data_set3[1]
    LiI_2 = data_set3[2]
    
    # Set font to sans-serif for a scientific look
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'legend.fontsize': 14,
        'lines.linewidth': 1.5,
        'lines.markersize': 6,
        'mathtext.fontset': 'cm',
    })

    
    
    # plot data
    fig1, ax = plt.subplots(figsize=(8, 8))

    # plot region of interest
    plt.axvline(x=1, color=hex_colors_blue[5], linestyle='--')
    plt.axvline(x=2, color=hex_colors_blue[5], linestyle='--')
    
    ax.plot(lambda_ang,Helium3, label='3He 20atm and 0.5cm thickness. Data points from NIST', marker=maker_style[1],linestyle='None',color=hex_colors_bw[1])
    ax.plot(lambda_ang,LiF, label='6LiF:ZnS(Ag) 250$\mu$m thickness. Data points from NIST',marker=maker_style[2],linestyle='None',color=hex_colors_bw[2])
    ax.plot(lambda_ang_1,Helium3_1, label='3He 20atm. Data points from ASI Quotation',marker=maker_style[3],linestyle='None',color=hex_colors_bw[3])
    ax.plot(lambda_ang_2,LiF_2, label='6LiF:ZnS(Ag) 250$\mu$m thickness. Data points from DOI',marker=maker_style[4],linestyle='None',color=hex_colors[2])
    ax.plot(lambda_ang_2,LiI_2, label='6LiI:Eu 250$\mu$m thickness. Data points from DOI',marker=maker_style[5],linestyle='None',color=hex_colors[3])

    

    # Add labels and title
    plt.xlabel('$\lambda$ (Ang)')
    plt.ylabel('Neutron Absorption (%)')
    plt.title('')
    plt.xlim(0,4.50) # X-axis from  to 
    plt.ylim(0,130)  # Y-axis from  to 

    # Scientific notation on both axes
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)

    # Add grid, minor ticks, and legend
    ax.grid(True, which='major', linestyle='-', alpha=0.3)
    ax.minorticks_on()
    ax.grid(True, which='minor', linestyle=':', alpha=0.2)
    ax.legend(loc='upper left',frameon=False)

    # Show the plot
    plt.tight_layout()
    plt.show()
    
