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
              11.1: "11_1_FK_analitica",
              11.2: "11_2_MFPT",
              12:   "12_MFPT_appl",
              13: "13_Processo_Salti",
              14: "14_ME-FK", 
              15: "15_Intro_dinamici",
              16: "16_Canoniche_AzioneAngolo",
              17: "17_KAM", 
              18: "18_Mappa_Poincare", 
              19: "19_Intro_Caos", 
              20: "20_Caos_Locale",
              21: "21_Caos_Globale",
              22: "22_Frattali",
              23: "23_Sistemi_Dissipativi",
              24: "24_Lorenz"}

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
                    print(line)
                    auxfile.write(repl)
                    print(repl)
                elif line.startswith("\\include{lezioni"):
                    splits = line.split("_")
                    aux_N = int(splits[1].split(".")[0])
                    if aux_N == 11:
                        aux_n = int(splits[2].split(".")[0])
                    else:
                        aux_n = 0
                    if N + n/10 < aux_N + aux_n/10:
                        auxfile.write("%" + line)
                    else:
                        auxfile.write(line)
                else:
                    auxfile.write(line)

def compile_aux(N, n):
    if n != 0:
        n = n/10
    print("Compiling file", N, n)
    with open('master_aux.tex', 'r') as file :
        filedata = file.read()
    # Replace the target string
#    filedata = re.sub("includeonly", '%includeonly', filedata)
    # Write the file out again
#    with open('master_aux.tex', 'w') as file:
#        file.write(filedata)
    os.system(f'pdflatex master_aux.tex')
    with open('master_aux.tex', 'r') as file :
        filedata = file.read()
    # Replace the target string
    filedata = re.sub("%includeonly", 'includeonly', filedata)
    # Write the file out again
    with open('master_aux.tex', 'w') as file:
        file.write(filedata)

    os.system(f'pdflatex master_aux.tex')
#    os.system(f'pdflatex -interaction="batchmode" master_aux.tex')
#    print("Done")

    os.system(f"mv master_aux.pdf PDF/{dict_names[N+n]}.pdf")
    return

def clear_files():
    os.system("rm *.out *.aux *.log *.toc")
    os.system("rm master_aux.tex")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an auxiliary tex file to compile')
    parser.add_argument("N", default=0, type=int, const=1, nargs='?', help='Number of section (default: 1)')
    parser.add_argument("n", default=0, type=int, const=1, nargs='?', help='Number of section (default: 0)')
    N = vars(parser.parse_args())['N']
    n = vars(parser.parse_args())['n']
    if N == 0:
        k = 0
        for i in list(dict_names.keys()):
            new_N = int(i)
            new_n = int(10 * round(i - new_N, 1))
            create_aux_tex(new_N, new_n)
            compile_aux(new_N, new_n)
            os.system("clear")
            k+=1
        clear_files()
    elif N+n/10 in dict_names:
        create_aux_tex(N, n)
        compile_aux(N, n)
        clear_files()
    else:
        print(f'No file {N} {n}')

