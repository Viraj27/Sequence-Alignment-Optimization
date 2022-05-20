import tracemalloc
import time
class Utils:
    def __init__(self):
        pass

    def stringGenerator(self, strings, index):
        if strings[index].isalpha():
            str = strings[index]
            index += 1
        
        while (strings[index].isnumeric()):
            num = int(strings[index])
            begin = str[:num+1]
            end = str[num+1:]
            str = begin + str + end
            index += 1
            if index == len(strings):
                break

        return str, index

    def start_time_tracking(self):
        return time.time()

    def start_memory_tracking(self):
        tracemalloc.start()
    
    def stop_memory_tracking(self):
        tracemalloc.stop()

    def get_peak_traced_memory(self):
        _, peak = tracemalloc.get_traced_memory()
        # Return peak memory in KBs
        return peak/1024.0

class Constants:
    def __init__(self):
        self.delta = 30
        self.alpha = [[0, 110, 48, 94],
                        [110, 0, 118, 48],
                        [48, 118, 0, 110],
                        [94, 48, 110, 0]]
        
        self.alpha_enum = {'A': 0, 
                            'C': 1, 
                            'G': 2, 
                            'T': 3}    
