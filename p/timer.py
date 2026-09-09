import time
class Timer():
    def __init__(self):
        self.startime=time.time_ns()
    def timeit(self):
        print( "Time taken: ",time.time_ns()-self.startime)
        self.startime=time.time_ns()
