from basic_sequence_optimization import SequenceAlignmentBasic
from utils                                  import Utils
import time
import sys
class SequenceAlignmentEfficient(SequenceAlignmentBasic):

    def efficientSequenceAlignment(self, str1, str2):
        xlen = int(len(str1))
        ylen = int(len(str2))
        if xlen < 2 or ylen < 2:
            return self.sequenceAlignment(str1, str2)

        else:
            forward, backward = self.forward(str1[:xlen // 2], str2), self.backward(str1[xlen // 2:], str2)

            partition = [forward[j] + backward[ylen - j] for j in range(ylen + 1)]

            cut = partition.index(min(partition))

            forward, backward, partition = [], [], []

            left  = self.efficientSequenceAlignment(str1[ :xlen // 2], str2[ :cut])
            right = self.efficientSequenceAlignment(str1[xlen // 2: ], str2[cut: ])

            return [left[r] + right[r] for r in range(3)]

    def forward(self, str1, str2):
        xlen, ylen = len(str1), len(str2)

        forward_mat = []
        for i in range(xlen + 1):
            forward_mat.append([0] * (ylen + 1))
        
        for j in range(ylen + 1):
            forward_mat[0][j] = j * self.delta
        
        for i in range(1, xlen + 1):
            forward_mat[i][0] = forward_mat[i - 1][0] + self.delta
            
            for j in range(1, ylen + 1):
                forward_mat[i][j] = min(forward_mat[i - 1][j - 1] + self.alpha[self.alpha_enum[str1[i - 1]]][self.alpha_enum[str2[j - 1]]],
                                 self.delta + forward_mat[i - 1][j], self.delta + forward_mat[i][j - 1])

            forward_mat[i - 1] = []
        return forward_mat[xlen]
    
    def backward(self, str1, str2):
        xlen, ylen = len(str1), len(str2)

        backward_matrix = []
        for i in range(xlen + 1):
            backward_matrix.append([0]*(ylen + 1))

        for j in range(ylen + 1):
            backward_matrix[0][j] = j * self.delta

        for i in range(1, xlen + 1):
            backward_matrix[i][0] = backward_matrix[i - 1][0] + self.delta

            for j in range(1, ylen + 1):
                backward_matrix[i][j] = min(backward_matrix[i - 1][j - 1] + self.alpha[self.alpha_enum[str1[xlen - i]]][self.alpha_enum[str2[ylen - j]]],
                                self.delta + backward_matrix[i - 1][j] , self.delta + backward_matrix[i][j - 1])
            
            backward_matrix[i - 1] = []

        return backward_matrix[xlen]

if __name__ == "__main__":

    file_name  = sys.argv[1]
    file       = open(file_name, 'r')

    file_input = file.readlines()

    efficient_alignment_obj = SequenceAlignmentEfficient()
    utils_obj               = Utils()

    file_input    = [ip.rstrip('\n') for ip in file_input]
    
    str1, idx     = utils_obj.stringGenerator(file_input, 0)
    str2, _       = utils_obj.stringGenerator(file_input, idx)

    start_time_efficient   = utils_obj.start_time_tracking()
    utils_obj.start_memory_tracking()
    res_strings            = efficient_alignment_obj.efficientSequenceAlignment(str1, str2)
    result1, result2, cost = res_strings[0], res_strings[1], res_strings[2]

    peak_memory         = utils_obj.get_peak_traced_memory()
    time_diff_efficient = time.time() - start_time_efficient
    utils_obj.stop_memory_tracking()
    
    with open('output.txt', 'w') as f:
        f.write(result1[0:50] + " " + result1[-50:] + "\n")
        f.write(result2[0:50] + " " + result2[-50:] + "\n")
        f.write(str(cost) + "\n")
        f.write(str(time_diff_efficient) + "\n")
        f.write(str(peak_memory) + "\n")
