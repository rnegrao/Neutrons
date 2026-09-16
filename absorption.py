import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

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
    data_set1 = np.loadtxt('data/neutronabsorption_NIST.txt',skiprows=1)
    lambda_ang = data_set1[:,0]
    Helium3_NIST = data_set1[:,1] #3He(20atm)5mm0.00251g/cm3
    LiF_NIST = data_set1[:,2]   #Li6F:ZnS(Ag)450um(1:2)(0.44g/cm3)
    LiF_NIST_2 = data_set1[:,3] #Li6F:ZnS(Ag)450um(1:3)(0.36g/cm3)
    LiF_NIST_3 = data_set1[:,4] #Li6F:ZnS(Ag)250um(1:2)(0.44g/cm3)

    data_set2 = np.loadtxt('data/neutronabsorption_LDN.txt',skiprows=1)
    lambda_ang_1 = data_set2[:,0]
    Helium3_1 = data_set2[:,1]

    data_set3 = np.loadtxt('data/neutronabsorption_ref1.txt',skiprows=2) #timepix detector
    lambda_ang_2 = data_set3[0]
    LiF_2 = data_set3[1]
    LiI_2 = data_set3[2]

    data_set4 = np.loadtxt('data/neutron_detection_efficiency_SDX_detector_ref2.txt',skiprows=2) #isi SDX
    lambda_ang_3 = data_set4[:,0]
    LiF_3 = data_set4[:,1]

    data_set5 = np.loadtxt('data/neutron_detection_efficiency_ref3.txt',skiprows=2) #chiness article 
    lambda_ang_4 = data_set5[:,0]
    LiF_4 = data_set5[:,1]

    data_set6 = np.loadtxt('data/neutronabsorption_ref4.txt',skiprows=2) # NIST article
    lambda_ang_5 = data_set6[0]
    LiF_5 = data_set6[1]
        
    # Set font to sans-serif for a scientific look
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'legend.fontsize': 8,
        'lines.linewidth': 1.5,
        'lines.markersize': 6,
        'mathtext.fontset': 'cm',
    })  
    
    # plot data
    fig1, ax = plt.subplots(figsize=(8, 8))

    # plot region of interest
    plt.axvline(x=1, color=hex_colors_bw[5], linestyle='--')
    plt.axvline(x=2, color=hex_colors_bw[5], linestyle='--')
    plt.axhline(y=50, color=hex_colors_bw[0], linestyle='--')

    #3He
    ax.plot(lambda_ang,Helium3_NIST, label='3He 20atm and 5mm thickness. Data points from NIST', marker=maker_style[0],linestyle='None',color=hex_colors_bw[1])
    ax.plot(lambda_ang_1,Helium3_1, label='3He LDN-SK03610 20atm. Data points from ASI Quotation',marker=maker_style[1],linestyle='None',color=hex_colors_bw[3])

    #LiF
    ax.plot(lambda_ang,LiF_NIST, label='6LiF:ZnS(Ag)(1:2) 0.45mm thickness. Data points from NIST',marker=maker_style[2],linestyle='None',color=hex_colors[2])
    ax.plot(lambda_ang,LiF_NIST_2, label='6LiF:ZnS(Ag)(1:3) 0.45mm thickness. Data points from NIST',marker=maker_style[3],linestyle='None',color=hex_colors[3])
    ax.plot(lambda_ang,LiF_NIST_3, label='6LiF:ZnS(Ag)(1:2) 0.25mm thickness. Data points from NIST',marker=maker_style[8],linestyle='None',color=hex_colors[5])
    
    ax.plot(lambda_ang_3,LiF_3*100, label='6LiF:ZnS(Ag)(1:2) 0.45mm thickness. Data points from https://doi.org/10.1107/S1600576724002462',marker=maker_style[4],linestyle='None',color=hex_colors[4])
        
    ax.plot(lambda_ang_2,LiF_2, label='6LiF:ZnS(Ag) 0.25mm thickness. Data points from https://doi.org/10.1063/5.0189920',marker=maker_style[5],linestyle='None',color=hex_colors_blue[1])
    ax.plot(lambda_ang_2,LiI_2, label='6LiI:Eu 0.25mm thickness. Data points from https://doi.org/10.1063/5.0189920',marker=maker_style[6],linestyle='None',color=hex_colors_blue[1])
    ax.plot(lambda_ang_5,LiF_5, label='6LiF:ZnS(Ag)(1:2) 0.40mm thickness. Data points from 10.1109/TNS.2018.2809567',marker=maker_style[7],linestyle='None',color=hex_colors_blue[2])
    
    # Add labels and title
    plt.xlabel('$\lambda$ (Ang)')
    plt.ylabel('Neutron Absorption (%)')
    plt.title('')
    plt.xlim(0,5.250) # X-axis from  to 
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
