import numpy as np 
import os 
import sys 
import re
import argparse

dict_names = {1: "1_markov_master", 
              2: "2_richiami_prob", 
              3: "3_func_caratt_mom_fatt",
              4: "4_markov_def",
              5: "5_markov_ex",
              6: "6_Rand_Walk",
              7: "7_Integr_stoca",
              8: "8_legame_SDE_FK",
              9: "9_Levy",
              10: "10_RW_Wierstrass", 
              11.1: "11_FK_analitica"}

def create_aux_tex(N, n):
    num_str = ''
    if n == 0 and N == 11:
        raise Exception('Lesson 11 is divided in 2 parts, please tell which part you want.')
    if n != 0:
        num_str = f'_{n}'

    repl = '\\includeonly{' + f'lezioni/lez_{N}' + num_str + '}'
    # Read in the file
    with open('master.tex', 'r') as file :
        with open('master_aux.tex', 'w') as auxfile:
            for line in file:
                if line.startswith("\\includeonly"):
                    auxfile.write(repl)
                else:
                    auxfile.write(line)

def compile_aux(N, n):
    if n != 0:
        n = n/10
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

    os.system(f"mv master_aux.pdf PDF/{dict_names[N+n]}.pdf")
    return

def clear_files():
    os.system("rm *.out *.aux *.log *.toc")
    os.system("rm master_aux.tex")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an auxiliary tex file to compile')
    parser.add_argument("N", default=1, type=int, const=1, nargs='?', help='Number of section (default: 1)')
    parser.add_argument("n", default=0, type=int, const=1, nargs='?', help='Number of section (default: 0)')
    N = vars(parser.parse_args())['N']
    n = vars(parser.parse_args())['n']
    if N+n/10 in dict_names:
        create_aux_tex(N, n)
        compile_aux(N, n)
        clear_files()
    else:
        print(f'No file {N} {n}')

