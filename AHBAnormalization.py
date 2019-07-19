#!/usr/bin/env python#                      

import os                            
import numpy as np                                   
import pandas as pd
import nibabel as nb
import numpy.linalg as npl
import csv
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
from scipy import stats
from scipy.stats.stats import pearsonr, ttest_1samp, percentileofscore,linregress



#PARAMETERS
Ngenes=16906 #default options: 1 to 16906

#FILE PATHS
dir_path = "/Users/PK/Desktop/C-lab/[01] Neurogenetics/Candidate-gene-cognition-discovery/"
input_path = os.path.join(dir_path, "input/")
output_path = os.path.join(dir_path,"output/")

#OUTPUT FILE
output_file = (os.path.join(output_path,"AHBA_16906_genes_normalized.csv")) #full data output

#INPUT FILES
#Allen Human Brain Atlas inputs
print "Loading input files..."
df0 = pd.read_csv(input_path+"AHBA_16906_genes.csv", nrows=Ngenes)


X=df0.iloc[:, 2:948]
df0.iloc[:, 2:948]=stats.zscore(X,axis=1, ddof=1)
print "1st"

X=df0.iloc[:, 948:1841]
df0.iloc[:, 948:1841]=stats.zscore(X,axis=1, ddof=1)
print "1st"

X=df0.iloc[:, 1841:2204]
df0.iloc[:, 1841:2204]=stats.zscore(X,axis=1, ddof=1)
print "3rd"

X=df0.iloc[:, 2204:2733]
df0.iloc[:, 2204:2733]=stats.zscore(X,axis=1, ddof=1)
print "1st"

X=df0.iloc[:, 2733:3203]
df0.iloc[:, 2733:3203]=stats.zscore(X,axis=1, ddof=1)
print "1st"

X=df0.iloc[:, 3203:3704]
df0.iloc[:, 3203:3704]=stats.zscore(X,axis=1, ddof=1)
print "6th"

normdata=pd.concat([df0.iloc[:, 0:948],df0.iloc[:, 948:1841],df0.iloc[:, 1841:2204],df0.iloc[:, 2204:2733],df0.iloc[:, 2733:3203],df0.iloc[:, 3203:3704]], axis=1)
df = pd.DataFrame(normdata)
df.to_csv(output_file, index=False, encoding='utf-8')