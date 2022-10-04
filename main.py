import numpy as np 
import os 
import sys 
import re
import argparse

dict_names = {1: "1_markov_master", 
              2: "2_richiami_prob", 
              3: "3_func_caratt_mom_fatt",
              4: "4_markov_def",
              5: "5_markov_ex"}

def create_aux_tex(n):
    # Read in the file
    with open('master.tex', 'r') as file :
      filedata = file.read()
    
    # Replace the target string
    filedata = re.sub("includeonly{lezioni/lez_\d", 'includeonly{' + f'lezioni/lez_{n}', filedata)
    
    # Write the file out again
    with open('master_aux.tex', 'w') as file:
      file.write(filedata)
    return

def compile_aux(n):
    print("Compile all files")
    with open('master_aux.tex', 'r') as file :
        filedata = file.read()
    # Replace the target string
    filedata = re.sub("includeonly", '%includeonly', filedata)
    # Write the file out again
    with open('master_aux.tex', 'w') as file:
        file.write(filedata)
    print("First compilation...")
    os.system(f'pdflatex -interaction="batchmode" master_aux.tex')
    print("Done")

    print("Compile only the required file")
    with open('master_aux.tex', 'r') as file :
        filedata = file.read()
    # Replace the target string
    filedata = re.sub("%includeonly", 'includeonly', filedata)
    # Write the file out again
    with open('master_aux.tex', 'w') as file:
        file.write(filedata)

    print("Second compilation...")
    os.system(f'pdflatex -interaction="batchmode" master_aux.tex')
    print("Done")
    print("Third compilation...")
    os.system(f'pdflatex -interaction="batchmode" master_aux.tex')
    print("Done")

    os.system(f"mv master_aux.pdf PDF/{dict_names[n]}.pdf")
    return

def clear_files():
    os.system("rm *.out *.aux *.log *.toc")
    os.system("rm master_aux.tex")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an auxiliary tex file to compile')
    parser.add_argument("N", default=1, type=int, const=1, nargs='?', help='Number of section (default: 1)')
    n = vars(parser.parse_args())['N']
    if n in dict_names:
        create_aux_tex(n)
        compile_aux(n)
        clear_files()
    else:
        print(f'No file {n}')

