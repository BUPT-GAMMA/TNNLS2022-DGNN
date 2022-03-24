import subprocess
import os
import numpy as np

eps = [0.7, 0.8, 0.9]
use_alpha = [0, 1]
lambda1 = [0.01,0.1,1,10,100]
lambda2 = [0.01,0.1,1,10,100]

for i in lambda1:
  for j in lambda2:
    for k in range(10):
      subprocess.run("CUDA_VISIBLE_DEVICES=1 python train.py --dataset=pubmed_medium --lambda1="+str(i)+" --lambda2="+str(j), shell=True)
    f = open("pubmed_medium.txt","r")
    ff = f.readlines()
    f.close()
    poly = []
    for k in range(len(ff)):
      one = ff[k].strip().split()
      poly.append(float(one[0]))
    poly = np.array(poly)
    print(poly.mean(), poly.std())
    f=open("pubmed_medium_all.txt", "a")
    f.write(str(i)+"\t"+str(j)+"\t"+str(poly.mean())+"\t"+str(poly.std())+"\n")
    f.close()
    os.remove("pubmed_medium.txt")