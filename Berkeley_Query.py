import pandas as pd 
import numpy as np
%tensorflow_version 1.x
import tensorflow
print(tensorflow.__version__)
import wget
import pandas as pd
import requests
import csv




class Berkeley_Query(object):
    def __init__(self):
        super().__init__()
        self.short_list = []
    def get_short(self, directory):
        data = pd.read_csv (directory)
        data.columns = ['id', 'project', 'time', 'target_name', 'ra', 'decl', 'center_freq', 'file_type', 'size', 'md5sum', 'url']

        data = data.loc[data['project'] == 'GBT']
        data = data.loc[data['file_type'] == 'HDF5']
        data.to_csv('database_gbt_h5.CSV', sep=',')

        data_numpy = data.values[:,1:]

        links_list =[]
        for i in range(0,data_numpy.shape[0]): 
            string = data_numpy[i,9]
            string = string.replace('fine.h5','mid.h5')
            string = string.replace('time.h5','mid.h5')
            links_list.append(string)
        self.short_list = [] 
        for k in range(0,int(len(links_list)/3)):
            self.short_list.append(links_list[k*3])   
    def get_cadence(self):

