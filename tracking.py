__author__ = 'Stella'


''''import numpy as np, h5py
f = h5py.File('Cell0000620.mat','r')
data = f.get('data/variable1')
data = np.array(data)
'''''

import scipy.io as sio

a=sio.loadmat('Cell0000625_v7.mat')
