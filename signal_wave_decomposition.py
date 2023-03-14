import numpy as np
import matplotlib.pyplot as plt
import math

freq_sin = np.asarray([5,6])			#Frequency of Sine Waves
amplitude_sin = np.asarray([5,8])		#Amplitude of Sine Waves

freq_cos = np.asarray([4,11])			#Frequency of Cosine Waves
amplitude_cos = np.asarray([3,20])		#Amplitude of Sine Waves


#number of time-dimention points to plot
sampling_frequency = 1000

#intervals at which time points are sampled
sampling_interval = 1/sampling_frequency

#start and end time
start, end = 0,10



#time points
time = np.arange(start,end,sampling_interval)


#creating sine waves


data_sin =0
data_cos =0

for i in range(len(freq_sin)):
    data_sin = data_sin + amplitude_sin[i]*np.sin(2*np.pi*freq_sin[i]*time)


for i in range(len(freq_cos)):
    data_cos = data_cos + amplitude_cos[i]*np.cos(2*np.pi*freq_cos[i]*time)




#plt.show()

#sum of both waves
data_sum = np.asarray(data_sin) + np.asarray(data_cos)

noise = np.random.normal(0,10,len(time))   #adding noise

data_sum = np.asarray(data_sum) + noise







#Performing fourier transform on the summed waves
ft = np.fft.fft(data_sum)/len(data_sum)

#taking half data points
fourierTransform = ft[range(int(len(data_sum)/2))]


tpCount = len(data_sum)

values = np.arange(int(tpCount/2))


timePeriod  = tpCount/sampling_frequency
#print(timePeriod)

frequency = values/timePeriod
frequency=np.asarray(frequency)

thresh = np.amax(np.abs(fourierTransform))/10

a=0
for i in range(len(fourierTransform)):
    if np.abs(fourierTransform[i]) > thresh:
        print(f"{i} : {frequency[i]} : {np.abs(fourierTransform[i])}")
        a = i







#axis[3].plot(frequency[0:a+50],np.abs(fourierTransform)[0:a+50])
#plt.show()

amplitude_check = 2* np.abs(fourierTransform)

#amplitude_check=amplitude_check[range(int(len(amplitude_sum)/2))]
#plt.plot(frequency[0:a+50],amplitude_check[0:a+50])
#plt.show()

plt.plot(frequency[0:a+50],amplitude_check[0:a+50])
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()


x_2 = fourierTransform #ft


x_2_check=[]


for i in range(len(x_2)):
    if np.abs(x_2[i]) < thresh:
        x_2_check.append(0)
    else:
        x_2_check.append(x_2[i])
        print(x_2[i])

#exit()



sin_count = 0
amplitude_sin_print =[]
frequency_sin_print =[]

cos_count = 0
amplitude_cos_print =[]
frequency_cos_print =[]
for i in range(len(x_2_check)):
    if np.abs(np.imag(x_2_check[i])) > np.abs(np.real(x_2_check[i])):
        sin_count = sin_count + 1
        amplitude_sin_print.append(np.round(amplitude_check[i],decimals=1))
        frequency_sin_print.append((frequency[i]))
        print(f"Sine wave of frequency : {(frequency[i])} and amplitude : {np.round(amplitude_check[i],decimals=1)}")
    elif np.abs(np.imag(x_2_check[i])) < np.abs(np.real(x_2_check[i])):
        cos_count = cos_count + 1
        amplitude_cos_print.append(np.round(amplitude_check[i],decimals=1))
        frequency_cos_print.append((frequency[i]))
        print(f"Cos wave of frequency : {frequency[i]} and amplitude : {np.round(amplitude_check[i],decimals=1)}")
    else:
        continue




fig, axis = plt.subplots(1+sin_count + cos_count,1)
plt.subplots_adjust(hspace=2)

axis[0].plot(time,data_sum)
axis[0].set_title("Original Wave")


for i in range(sin_count):
    axis[i+1].plot(time,amplitude_sin_print[i]*np.sin(2*np.pi*frequency_sin_print[i]*time))
    axis[i+1].set_title(f"Sine Wave \n"
                      f"Amplitude = {amplitude_sin_print[i]} Frequency = {frequency_sin_print[i]}")


for i in range(cos_count):
    axis[1+sin_count + i].plot(time,amplitude_cos_print[i]*np.cos(2*np.pi*frequency_cos_print[i]*time))
    axis[1+sin_count + i].set_title(f"Cos Wave \n"
                      f"Amplitude = {amplitude_sin_print[i]} Frequency = {frequency_sin_print[i]}")

axis[sin_count + cos_count].set_xlabel("Time")

plt.show()
