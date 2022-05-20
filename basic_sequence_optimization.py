import time
import sys
from   utils import Utils, Constants

class SequenceAlignmentBasic(Constants):

    def sequenceAlignment(self, str1, str2):
        xlen, ylen = len(str1), len(str2)
        seq_align_mat = []
        for i in range(xlen + 1):
            seq_align_mat.append([0] * (ylen+1))
        for j in range(ylen + 1):
            seq_align_mat[0][j] = j * self.delta
        for i in range(xlen + 1):
            seq_align_mat[i][0] = i * self.delta
        for i in range(1, xlen + 1):
            for j in range(1, ylen + 1):
                seq_align_mat[i][j] = min(seq_align_mat[i - 1][j - 1] + self.alpha[self.alpha_enum[str1[i - 1]]][self.alpha_enum[str2[j - 1]]], 
                                seq_align_mat[i][j - 1] + self.delta, 
                                seq_align_mat[i - 1][j] + self.delta)

        alignment_one = ""
        alignment_two = ""
        i, j = xlen, ylen
        while i and j:
            score, scoreUp, scoreLeft, scoreDiag = seq_align_mat[i][j], seq_align_mat[i - 1][j], seq_align_mat[i][j - 1], seq_align_mat[i - 1][j - 1]
            if score == scoreDiag + self.alpha[self.alpha_enum[str1[i - 1]]][self.alpha_enum[str2[j - 1]]]:
                alignment_one += str1[i - 1]
                alignment_two += str2[j - 1]
                i -= 1
                j -= 1
            elif score == scoreLeft + self.delta:
                alignment_one += '_'
                alignment_two += str2[j - 1]
                j -= 1
            elif score == scoreUp + self.delta:
                alignment_one += str1[i - 1]
                alignment_two += '_'
                i -= 1
        while i:
            alignment_one += str1[i - 1]
            alignment_two += '_'
            i -= 1
        while j:
            alignment_one += '_'
            alignment_two += str2[j - 1]
            j -= 1

        return alignment_one, alignment_two, seq_align_mat[xlen][ylen]
    

if __name__ == "__main__":

    file_name     = sys.argv[1]
    file          = open(file_name, 'r')

    file_input    = file.readlines()

    alignment_obj = SequenceAlignmentBasic()
    utils_obj     = Utils()

    file_input    = [ip.rstrip('\n') for ip in file_input]
    
    str1, idx     = utils_obj.stringGenerator(file_input, 0)
    str2, _       = utils_obj.stringGenerator(file_input, idx)

    #start CPU time and memory usage tracking
    start_time_basic = utils_obj.start_time_tracking()
    utils_obj.start_memory_tracking()

    res_strings            = alignment_obj.sequenceAlignment(str1, str2)
    result1, result2, cost = res_strings[0], res_strings[1], res_strings[2]

    peak_memory     = utils_obj.get_peak_traced_memory()
    time_diff_basic = time.time() - start_time_basic
    utils_obj.stop_memory_tracking()

    with open('output.txt', 'w') as f:
        f.write(result1[0:50] + " " + result1[-50:] + "\n")
        f.write(result2[0:50] + " " + result2[-50:] + "\n")
        f.write(str(cost) + "\n")
        f.write(str(time_diff_basic) + "\n")
        f.write(str(peak_memory) + "\n")