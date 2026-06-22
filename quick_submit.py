# Author: bibberzz
# Created: 2026/6/8 16:39
# Project: day11
# File: quick_submit.py
# Description:

import os
import zipfile
import sys
import subprocess

def zip_ipynb_in_day_dir(day_num, output_zip_name='周强.zip'):
    """
    在 day{day_num} 目录下查找所有以 task 开头且以 .ipynb 结尾的文件，打包为 output_zip_name，
    并将 zip 存放在 day{day_num} 目录下。
    返回 zip 路径。
    """
    day_dir = f"day{day_num}"
    if not os.path.isdir(day_dir):
        print(f"未找到目录: {day_dir}")
        sys.exit(1)
    ipynb_files = [f for f in os.listdir(day_dir) if f.startswith('task') and f.endswith('.ipynb')]
    if not ipynb_files:
        print(f"{day_dir} 下未找到以 task 开头且以 .ipynb 结尾的文件")
        sys.exit(1)
    output_zip_path = os.path.join(day_dir, output_zip_name)
    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        for file in ipynb_files:
            file_path = os.path.join(day_dir, file)
            # 在压缩包内部仅保留文件名，不含上层目录
            zipf.write(file_path, arcname=file)
    print(f"打包完成：{output_zip_path}")
    return output_zip_path

def scp_zip_to_server(zip_path, day_num):
    server = "py12@8.155.27.170"
    remote_dir = f"~/day{day_num}/"
    scp_cmd = ["scp", zip_path, f"{server}:{remote_dir}"]
    print(f"正在通过scp传输 {zip_path} 到 {server}:{remote_dir}")
    try:
        subprocess.check_call(scp_cmd)
        print("传输完成。")
    except subprocess.CalledProcessError as e:
        print(f"SCP 传输失败: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python quick_submit.py <day数字>")
        sys.exit(1)
    day_num = sys.argv[1]
    zip_path = zip_ipynb_in_day_dir(day_num)
    # 可选参数: 如果传入 --with-scp，则执行 scp
    if "--with-scp" in sys.argv:
        scp_zip_to_server(zip_path, day_num)