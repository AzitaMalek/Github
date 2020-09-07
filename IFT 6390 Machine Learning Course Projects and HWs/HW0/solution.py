import numpy as np


def make_array_from_list(some_list):
    print(np.array(some_list))
    pass


def make_array_from_number(num):
    num_array=np.array([num])
    print(num_array)
    pass


class NumpyBasics:
    def add_arrays(self, a, b):
        res=np.add(a,b)
        print(res)
        pass

    def add_array_number(self, a, num):
        pass

    def multiply_elementwise_arrays(self, a, b):
        print(np.multiply(a,b))
        pass

    def dot_product_arrays(self, a, b):
        print(np.dot(a,b))
        pass

    def dot_1d_array_2d_array(self, a, m):
        # consider the 2d array to be like a matrix
        print(np.dot(a,m))
        pass
