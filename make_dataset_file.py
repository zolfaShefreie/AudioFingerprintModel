import numpy as np
import os

DIR_TO_DATASET = './dataset'

if __name__ == '__main__':
    features = np.array([])

    # get all file paths
    file_paths = [DIR_TO_DATASET+'/'+path for path in os.listdir(DIR_TO_DATASET)]

    # concat array of per file to one array
    for path in file_paths:
        with open(path, 'rb') as f:
            features = np.concatenate((features, np.load(f, allow_pickle=True)), axis=0)

    print(features.shape)

    # save to one file
    with open('./all.npy', 'wb') as f:
        np.save(f, features)
