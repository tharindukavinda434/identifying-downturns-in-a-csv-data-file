
# importing libraries
from re import L
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#taking the inputs
input_csv_name = input('enter your csv name : ')
start_quater   = input('Start Quater : ')
end_quater     = input('End Quater : ')
x              = input('x :')
x =int(x)

print (input_csv_name)
print (start_quater)
print(end_quater)
print(x)

#csv file reading
df = pd.read_csv(input_csv_name,header=None)
df =df.iloc[8::, ::]

# getting the data in the dataframe
s1 = ( df.iloc[:,0].values )
s2 = ( df.iloc[:,1].values )

#getting the quater data from the data set
for i in range (len(s1)):
    t = s1[i]
    t = list(t)
    if ( len(t) == 4 ):
        start_index = i
    end_index=i


s1 = s1[start_index+1:end_index+1]
s2 = s2[start_index+1:end_index+1]
s3=[]

#converting strings into integers
for i in range (len(s2)):
    t = int (s2[i])
    s3.append(t)


for i in range ( len (s1) ):
    if ( s1[i] == str(start_quater)  ):
        slice_start_index = i
        

    if ( s1[i] == str(end_quater)  ):
        slice_end_index = i


s1 = s1[slice_start_index:slice_end_index+1]
s3 = s3[slice_start_index:slice_end_index+1]       
print (len(s1))
final_s1 = []
final_s3 = []

#algorithm to get the downturns
for i in range ( len(s1) ):
    if ( i+2*x <= len(s1) ):
        s1t_first_half   = s1[i:i+x]
        s1t_second_half  = s1[i+x:i+2*x]

        #the total length of we need to consider is 2*x
        s1t  = s1[i:i+2*x]
        s3t  = s3[i:i+2*x]
        #getting the first half
        s3t_first_half   = s3[i:i+x]
        #initially flag values are false
        #first  flag is for minus identifying minus gradient
        #second flag is for plus  identifying minus gradient
        flag_1 =  False
        flag_2 =  False
        #minus gradient for consecutive x 
        for j in range ( len(s3t_first_half) ):
            if ( j == 0 ):
                t = s3t_first_half[j]

            else:
                if ( t > s3t_first_half[j] ):
                    t  = s3t_first_half[j]
                else:
                    break

        if ( j == len(s3t_first_half) -1 ):
            flag_1 = True
            print('flag_1')
        #getting the first half
        s3t_second_half  = s3[i+x:i+2*x]
        #plus gradient for consecutive x 
        for k in range ( len(s3t_second_half) ):
            if ( k == 0 ):
                t = s3t_second_half[k]

            else:
                if ( t < s3t_second_half[k] ):
                    t  = s3t_second_half[k]
                else:
                    break

        if ( k == len(s3t_second_half) -1 ):
            flag_2 = True
            print('flag_2')
        # if the both flags are True we have the required time period
        if (  (flag_1 == True) and (flag_2 == True) ):
            final_s1.append (s1t)
            final_s3.append(s3t)
        

        print('_________________________')

    
    else:
        break


#print(final_s1)
#print(final_s3)


#plotting the graph for captured downturns
for i in range(len(final_s3)):
    plt.figure()
    temp = final_s1[i]
    start_date = temp[0]
    print ('start date : ',start_date)
    end_date   = temp[-1]
    print ('end date : ',end_date)
    plt.plot(final_s3[i])
    print ( 'lower : ' ,min(final_s3[i]) )
    plt.title (str(start_date)+' : '+str(end_date))

plt.show()

