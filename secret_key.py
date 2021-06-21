import pprint
import numpy as np
from numpy.lib.shape_base import split


def juge_4times(line:str): 
    """
    四倍かどうかを判定し,四倍でないなら
    最小の四の倍数に調節する
    line: 0110など
    return: 最小の四の倍数
    """
    bin_length = len(line)
    modular = bin_length % 4
    if modular != 0:
        bin_length = bin_length + 4 - modular
        return bin_length
    else:
        return bin_length

def bin_converter(key:int):
    """
    秘密鍵を２進数変換し先頭を取り除く
    return:二進数の列（str型）
    key: ８など
    """
    bin_key = bin(key)
    int_bin_key = bin_key[2:]
    return int_bin_key

def fill_zero(bin_line:str,four_times:int):
    """
    二進数変換した列の長さを求めた最小の四の倍数
    と同じになるように右詰めで0をいれる
    return:ゼロのついた二進数の列
    bin_line:10000
    four_times:8(00010000)
    """
    zero_bin_line = bin_line.zfill(four_times)
    return zero_bin_line

def full_bin_line(secret_key:int):
    """
    今までのをまとめたもの
    return: int型のゼロ詰めされた二進数の列
    """
    return list(fill_zero(bin_converter(secret_key),juge_4times(bin_converter(secret_key))))

def list_converter(str_list:list):
    """
    listの要素がstr型になっているのをint型に変換します
    return:要素がintのlist
    """
    int_list = list(map(int,str_list))
    return int_list

def split_list(l:list,split_num:int):
    """
    listをsplit_num分割するプログラム
    return: list in list で返す
    """
    for i in range(0, len(l), split_num):
        yield l[i:i + split_num]

def matrix_format(split_lists:list):
    """
    list in list を行列形式にへんこうします
    """
    print(split_lists)
    if len(split_lists) == 4:
        matrix_list = np.array(split_lists)
        return matrix_list    
    elif len(split_lists) < 4:
        lack_row = 4 - len(split_lists)
        for i  in range(lack_row):
            split_lists.append([0,0,0,0])
        matrix_list = np.array(split_lists)
        return matrix_list

def matrix_print(key_num:int,splits_num:int):
    """
    全てを求めたもの
    秘密鍵から2進数変換したものを行列に変換したもの
    """
    line = full_bin_line(key_num)
    int_line = list_converter(line)
    int_split_list = list(split_list(int_line,splits_num))
    matrix = matrix_format(int_split_list)
    return print(matrix)


matrix_print(68,4)