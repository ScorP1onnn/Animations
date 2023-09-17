#Possbile demo for the rotation of coordinates and showing resulting components of the vector
# Will work on it today - Sai

x = convert_to_radians = (np.pi/180)


def rotation(theta,vec): #To multiply with rotation matrix
    r = np.asarray([[np.cos(theta * x),-np.sin(theta * x)],
                  [np.sin(theta * x),np.cos(theta * x)]])
    return np.matmul(r,vec)


def rotate(theta = 0):
    
    dxy = np.asarray([[5],[5]])
    
    #Plotting Red Arrow
    plt.quiver(0, 0, dxy[0][0], dxy[1][0], angles='xy', scale_units='xy', scale=1, color='red')
    plt.plot([dxy[0][0],0],[dxy[1][0],0],color='red') #marker='.',markevery=[0]

    #PLotting Axis
    x_1 = np.asarray([[10],[0]])
    x_2 = np.asarray([[-10],[0]])
    y_1 = np.asarray([[0],[10]])
    y_2 = np.asarray([[0],[-10]])

    #Input angle
    t = theta
    
    #Rotation of axis
    x_1_rot = rotation(t,x_1)
    x_2_rot = rotation(t,x_2)
    y_1_rot = rotation(t,y_1)
    y_2_rot = rotation(t,y_2)

    



    r = dxy[0][0]/np.cos(45 * x)
    Ax = np.asarray([[r * np.cos((45-t) * x)],[0]])
    Ay = np.asarray([[0],[r * np.sin((45-t) * x)]])

    #Rotation of basis vectors
    Ax = rotation(t,Ax)
    Ay = rotation(t,Ay)
    #plt.scatter(Ax[0][0],Ax[1][0],color='red')
    #plt.scatter(Ay[0][0],Ay[1][0],color='red')
    
    V = np.array([Ax[0][0],Ax[1][0]])
    W = np.array([Ay[0][0],Ay[1][0]])
    
    
    #Plotting rotated axes
    plt.plot([x_1_rot[0][0],x_2_rot[0][0]],[x_1_rot[1][0],x_2_rot[1][0]],color='black',ls='-',alpha=0.3)
    plt.plot([y_1_rot[0][0],y_2_rot[0][0]],[y_1_rot[1][0],y_2_rot[1][0]],color='black',ls='-',alpha=0.3)

    
    #To change color of vector base and change number in the text
    if np.round(Ax[0][0],1) == 0:
        i = 0 
        cl_x = 'white'
    elif np.round(Ay[1][0],1) !=0 and 135 < theta < 315:
        i = (-1*(np.round(np.sqrt(Ax[0][0] ** 2 + Ax[1][0] ** 2),1)))
        cl_x = 'black'
    else:
        i = (1*(np.round(np.sqrt(Ax[0][0] ** 2 + Ax[1][0] ** 2),1)))
        cl_x = 'orange'


    if np.round(Ay[1][0],1) ==0:
        j = 0
        cl_y = 'white'
    elif np.round(Ay[1][0],1) !=0 and 45 < theta < 225:
        j = (-1 * (np.round(np.sqrt(Ay[1][0] ** 2 + Ay[0][0] ** 2), 1)))
        cl_y = 'black'
    else:
        j = (1* (np.round(np.sqrt(Ay[1][0] ** 2 + Ay[0][0] ** 2),1)))
        cl_y = 'orange'

    
    #Plotting rotated vector basis with text
    plt.text(4,8.5,f"V = {i}i +  {j}j")
    plt.text(-10,8,f"Orange arrow - Positive Axis \nBlack arrow - Negative Axis")
    plt.quiver(0, 0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color=cl_x)
    plt.quiver(0, 0, W[0], W[1], angles='xy', scale_units='xy', scale=1, color=cl_y)
    
    x_axis = np.array([[7.5],[-1]])
    y_axis = np.array([[0.2],[7.5]])
    
    x_axis = rotation(theta,x_axis)
    y_axis = rotation(theta,y_axis)
    
    plt.text(x_axis[0][0],x_axis[1][0],"X-Axis",color="black")
    plt.text(y_axis[0][0],y_axis[1][0],"Y-Axis",color="black")
    #plt.grid()
    plt.xlim(-11,10.5)
    plt.ylim(-11,10.5)
    plt.show()


interactive_plot = interactive(rotate,theta = (0,360,1))
output = interactive_plot.children[-1]
interactive_plot
