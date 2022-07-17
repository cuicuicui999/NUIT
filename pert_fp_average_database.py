import os
from re import L
import numpy as np

def nuclide_name(dir_name):
    if dir_name == '233U':
        line_number = int(1237)
        return '922330   U233    1237  3\n', line_number
    elif dir_name == '235U':
        line_number = int(1205)
        return '922350   U235    1205  3\n', line_number
    elif dir_name == '239Pu':
        line_number = int(1159)
        return '942390   Pu239   1159  2\n', line_number
    else:
        line_number = int(1076)
        return '942410   Pu241   1076  2\n', line_number


def pert_fp_average_value(dir_name, dir_path):
    sample_size = int(input('Please input the sample size: '))
    sample_library = { }
    for i in range(sample_size):
        file_name = str(i+1)
        file_path = os.path.join(dir_path, file_name)
        if os.path.exists(file_path):          
            with open (file_path, 'r', encoding='utf-8') as file_i:
                for reading_index, dataline in enumerate(file_i):
                    symbol_line, fp_number = nuclide_name(dir_name)
                    if dataline == symbol_line:
                        file_i.readline()
                        for j in range(fp_number):
                            fp_dataline = file_i.readline().split()
                            fp_symbol = fp_dataline[0]
                            fp_value = fp_dataline[1]
                            if i == 0:
                                sample_library[fp_symbol] = []
                            sample_library[fp_symbol].append(float(fp_value))
                            if j > fp_number:
                                break
        else:
            print(file_name + ' in ' + dir_name + ' is not exists!')
    return sample_library

def main():
    workdir = os.getcwd()
    dir_name = input('Please input the nuclide dir: ')
    dir_path = os.path.join(workdir, dir_name)

    if os.path.exists(dir_path):
        sample_library = pert_fp_average_value(dir_name, dir_path)
        print(len(sample_library))
        print(sample_library['10010'])
        print(sample_library['571500'])
        print(sample_library['802000'])

    else:
        print(dir_name + 'is not exists!')


if __name__ == '__main__':
    main()