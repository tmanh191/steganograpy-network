import argparse
import os

def text_to_binary(text):
    binary_str=''
    for char in text:
        binary_str += format(ord(char), '07b') +'0'
    return binary_str

def encode_binary_LP(binary_str):
    return ','.join(str(i) for i, bit in enumerate(binary_str) if bit == '1')

# sửa thành mã sinh viên của bạn
message="B21......"
print(encode_binary_LP(text_to_binary(message)))
