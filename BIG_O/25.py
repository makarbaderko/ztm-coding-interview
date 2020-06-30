import time
array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(100000)]
def finding_nemo(array):
    #t0 = time.time()
    print(array[0])
    print(array[1]) 
    #t1 = time.time()
    #print(f'Time taken = {t1-t0}')
finding_nemo(array_small)  #O(n) --> linear time
finding_nemo(array_medium) #O(n) --> linear time
finding_nemo(array_large)  #O(n) --> linear time