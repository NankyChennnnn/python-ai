#!/bin/bash

if [ $# -lt 1 ]; then
    echo "用法: $0 <day数字>"
    exit 1
fi

DAY_NUM="$1"

# 调用同目录下的 Python 脚本，传入天数参数
python3 "$(dirname "$0")/quick_submit.py" "$DAY_NUM" --with-scp
