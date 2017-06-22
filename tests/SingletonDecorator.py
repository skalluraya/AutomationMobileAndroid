'''
Created on Jun 21, 2017

@author: Shrikanth
'''


#This function is used as decorator to create Singleton classes
def singleton(cls):
    instances = {}
    def getinstance(*arg):
        if cls not in instances:
            instances[cls] = cls(*arg)
        return instances[cls]
    return getinstance        