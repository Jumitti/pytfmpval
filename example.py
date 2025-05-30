from pytfmpval import tfmp

mat = (" 3  7  9  3 11 11 11  3  4  3  8  8  9  9 11  2"
       " 5  0  1  6  0  0  0  3  1  4  5  1  0  5  0  7"
       " 4  3  1  4  3  2  2  2  8  6  1  4  2  0  3  0"
       " 2  4  3  1  0  1  1  6  1  1  0  1  3  0  0  5"
       )

m = tfmp.read_matrix(mat)
print("Score calculated :", tfmp.pval2score(m, 0.00001, mem_thresh=1),
      "| Expected :", 8.773708000000001)
print("Pvalue calculated :", tfmp.score2pval(m, 8.7737, mem_thresh=1),
      "| Expected :", 9.992625564336777e-06)