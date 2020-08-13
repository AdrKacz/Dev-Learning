import numpy as np

ttmbond = 10
daywalk = np.arange(0,30)
dtm = ttmbond - daywalk/252 

curve_list = [0.083,0.25,0.5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pos1= np.ones((len(daywalk+1),len(column_list)))
pos2 = pos*curve_list

pos3 = pos2 <= dtm