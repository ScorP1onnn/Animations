#funcion to create interactive plot
def area(NumBars=10):
    plt.figure()
    curve = np.linspace(0,9, 101)
    plt.plot(curve,10*curve*(5-curve),color='red',label=r'$Velocity$')
    bars_x1 = 0
    bars_x2 = 5
    bars_x = np.linspace(bars_x1,bars_x2,NumBars)
    #bars_cont = np.linspace(bars_x1,bars_x2,101)
    w = bars_x[2] - bars_x[1]
    #plt.bar(bars_cont,np.exp(bars_cont),color='green',label=r'Real Area',width=0.1)
    plt.bar(bars_x,10*bars_x*(5-bars_x),color='blue',edgecolor='black',label=r'Approximated Distance travelled',width=w)
    plt.xlim(-1,6)
    plt.ylim(0,100)
    plt.legend(loc='upper left')
    plt.show()

#make interactive slider
interactive_plot = interactive(area,NumBars=(10,100))
output = interactive_plot.children[-1]
interactive_plot
