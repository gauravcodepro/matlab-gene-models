# Author Gaurav
# Universitat Potsdam
# Date 2024-5-17 
/*
 a matlab function for the normalization of the gene expression levels for the 
 estimation of the upper bound and the lower bound levels. 
 reads a gene expression file and then log normalizes it and then estimated the gpr rules
 implemented the readtable instead of the readxls for faster reading of the files.
*/
 readfile = input(prompt, "please provide the gene expression file")
 sheet = input(prompt, "please provide the sheet number")
 column = input(prompt, "please provide the column number")
 if (~ column) 
    fileread = readtable(readfile, "sheet")
 elseif 
    fileredcolumn = readtable(readfile, "sheet", "column")
expressionadd = []
for i in 1:
 