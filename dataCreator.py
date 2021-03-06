from scipy.misc import imread
import numpy as np
import pandas as pd
import os
root = './signs'


for directory, subdirectories, files in os.walk(root): # Parse each  directory in the  folder

    for file in files: # Parse each file in that directory
        im = imread(os.path.join(directory,file)) # read the  file and extract its features
        value = im.flatten()
        value = np.hstack((directory[8:],value))  #The directory[8:] indicates after which character the class name should start so change it according to the file name. Hstack places array in stack on each other and directory name is made first coloumn
        df = pd.DataFrame(value).T
        df = df.sample(frac=1)
        with open('data.csv', 'a') as dataset:
            df.to_csv(dataset, header=False, index=False)
