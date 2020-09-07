import numpy as np


def make_array_from_list(some_list):
    return np.array(some_list)
    pass


def make_array_from_number(num):
    num_array=np.array([num])
    return num_array
    pass


class NumpyBasics:
    def add_arrays(self, a, b):
        res=np.add(a,b)
        return res
        pass

    def add_array_number(self, a, num):
        return np.add(a,num)
        pass

    def multiply_elementwise_arrays(self, a, b):
        return np.multiply(a,b)
        pass

    def dot_product_arrays(self, a, b):
        return np.dot(a,b)
        pass

    def dot_1d_array_2d_array(self, a, m):
        # consider the 2d array to be like a matrix
        return np.dot(a,m)
        pass
