import glob
import os
import subprocess
from subprocess import run
from pypdf import PdfWriter
import sys
from pathlib import Path

'''
前提条件
PyPDF
pip install pypdf

QPDF
Windowsならダウンロードしてパスを通す（コマンドラインからたたけるようにする）
MacならHomebrewでインストール
'''

#アウトプットのディレクトリを指定
decrypt_filepath = r"/Users/hollimaple/Downloads/out"
out_file = decrypt_filepath + r"/out.pdf"
#インプットのディレクトリを指定
in_file = r"/Users/hollimaple/Downloads/in" + r"/*.pdf"

pdfs = glob.glob(in_file)

#print(pdfs)

#複合化
de_pdfs = []
i=0
for pdf in pdfs:
    decrypt_file = decrypt_filepath + r"/out" + str(i) + r".pdf"
    de_pdfs.append(decrypt_file)
    #Windows
    if os.name == 'nt':
        cmd = ['qpdf', '--decrypt', pdf, decrypt_file]
        cp = run(cmd,shell=True)
    #Mac or Linux
    elif os.name == 'posix':
        cmd = ['qpdf', '--decrypt', pdf, decrypt_file]
        cp = run(cmd,stdout = subprocess.PIPE,encoding = 'utf_8_sig')
        #print(cp.stdout)
    i=i+1

merger = PdfWriter()

# for文で結合
for de_pdf in de_pdfs:
    merger.append(de_pdf)
    
# 書き出し
merger.write(out_file)
merger.close()

#複合化した一時ファイルを削除
for de_pdf in de_pdfs:
    os.remove(de_pdf)
