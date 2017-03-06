import numpy as np
np.random.seed(4)
import csv

data=np.genfromtxt('recordy.csv',delimiter=',',dtype=float)
action=data[:,0]
result=data[:,1]
playerY=data[:,2]
nextTopY=data[:,3]
nextBottomY=data[:,4]
nextDistance=data[:,5]
nnextTopY=data[:,6]
nnextBottomY=data[:,7]
nnextDistance=data[:,8]

weight1 =np.random.rand(1)
weight2 =0
weight3 =np.random.rand(1)
weight4 =np.random.rand(1)
weight5 =np.random.rand(1)
weight6 =np.random.rand(1)
weight7 =np.random.rand(1)
weight8 =np.random.rand(1)
weight9 =np.random.rand(1)
bias = np.random.rand(1)



def linearRegression ():
    learning_rate = 0.01
    global weight1,weight2, weight3,weight4, weight5,weight6,weight7,weight8,weight9,bias
    trans_data=data.transpose()
    weights=np.matrix([weight1,weight2,weight3,weight4,weight5,weight6,weight7,weight8,weight9])
    start_error=np.sum(np.dot(weights,trans_data))+bias*15000-np.sum(result)
    init_cost = np.power(start_error, 2)
    print ' initial cost %s'% init_cost
    print ' initial error is %s'%start_error
    
    for e in range(0,5):
        global sum_error
        sum_error=0
        for i in range(0,15000):
            curr_error=np.sum(np.dot(weights,data[i]))+bias-result[i]
            
            sum_error +=curr_error
            weight1 = weight1 - (learning_rate * curr_error * action[i] )
            weight3 = weight3 - (learning_rate * curr_error * playerY[i])
            weight4 = weight4 - (learning_rate * curr_error * nextTopY[i])
            weight5 = weight5 - (learning_rate * curr_error * nextBottomY[i] )
            weight6 = weight6 - (learning_rate * curr_error * nextDistance[i])
            weight7 = weight7 - (learning_rate * curr_error * nnextTopY[i])
            weight8 = weight8 - (learning_rate * curr_error * nnextBottomY[i])
            weight9 = weight9 - (learning_rate * curr_error * nnextDistance[i])
            bias = bias - (learning_rate * curr_error * 1.0 )
            end_cost=np.power(sum_error,2)
        print  'end cost %s'%end_cost
    weightsNbias=np.matrix([weight1,weight2,weight3,weight4,weight5,weight6,weight7,weight8,weight9,bias])
    np.savetxt('weights.csv',weightsNbias,delimiter=',')
linearRegression()




