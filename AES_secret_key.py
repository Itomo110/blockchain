import string
import random

from Crypto.Cipher import AES

# 対象文字列
plaintext = 'Pythonのpycryptoによる文字列の暗号化・復号化'
print(f'対象文字列：{plaintext}')

print(f'AESブロックサイズ：{AES.block_size}')
print(f'ASCII文字：{string.ascii_letters}')

# AESブロックサイズ分のランダムなASCII文字列を作成する
key = ''.join(
    [random.choice(string.ascii_letters) for _ in range(AES.block_size)])
print(f'key: {key}')

# 初期ベクトル(initialization vector)を生成
iv = ''.join(
    [random.choice(string.ascii_letters) for _ in range(AES.block_size)])
print(f'iv: {iv}')

print('===== 暗号化 =====')
# 暗号化用オブジェクトの準備
cipher = AES.new(key, AES.MODE_CBC, iv)
# バイト数がブロックサイズの倍数になるように詰め物(padding)の長さを計算する
padding_len = AES.block_size - len(plaintext.encode('UTF-8')) % AES.block_size
# 対象文字列にpadding長だけ文字列を追加する
plaintext += chr(padding_len) * padding_len
print(f'暗号化対象文字列：{plaintext}')
print(f'暗号化対象文字列バイト長：{len(plaintext.encode("UTF-8"))}')
# 文字列を暗号化する
cipher_text = cipher.encrypt(plaintext)
print(f'暗号化文字列：{cipher_text}')

print('===== 復号化 =====')
# 復号化用オブジェクトの準備
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
# 復号化を実施
decrypted_text = cipher_dec.decrypt(cipher_text)
print(f'復号化直後：{decrypted_text.decode()}')
decrypted_text = decrypted_text[:-decrypted_text[-1]]
print(f'padding文字列除去：{decrypted_text.decode()}')

"""
import string
import random

from Crypto.Cipher import AES

print(f'AESブロックサイズ: {AES.block_size}')
print(f'ASCII文字: {string.ascii_letters}')
#AESブロックサイズ分のランダムなASCII文字列を作成する
key = ''.join([random.choice(string.ascii_letters)
for _ in range(AES.block_size)])
print(f'key: {key}')

#初期ベクトル(initial vector)を生成
iv =''.join([random.choice(string.string.ascii_letters)
for _ in range(AES.block_size)])
print(f'iv: {iv}')

# 暗号化用オブジェクトの準備
cipher = AES.new(key, AES.MODE_CBC, iv)

# バイト数がブロックサイズの倍数になるように詰め物(padding)の長さを計算する
padding_len = AES.block_size - len(plaintext.encode('UTF-8')) % AES.block_size
# 対象文字列にpadding長だけ文字列を追加する
plaintext += chr(padding_len) * padding_len
print(f'暗号化対象文字列：{plaintext}')
print(f'暗号化対象文字列バイト長：{len(plaintext.encode("UTF-8"))}')

# 文字列を暗号化する
cipher_text = cipher.encrypt(plaintext)
print(f'暗号化文字列：{cipher_text}')


# 復号化用オブジェクトの準備
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
# 復号化を実施
decrypted_text = cipher_dec.decrypt(cipher_text)

print(f'復号化直後：{decrypted_text.decode()}')
decrypted_text = decrypted_text[:-decrypted_text[-1]]
print(f'padding文字列除去：{decrypted_text.decode()}')
"""