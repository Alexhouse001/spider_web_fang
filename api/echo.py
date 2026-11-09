#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
echo.py —— 供"爬虫练习站点"使用的 GET/POST 参数回显脚本（可选）。
用途：配合实验手册第11章实验4，让学生把 GET/POST 请求发到自己的域名，
     直观看到服务端接收到的参数。

部署方式（二选一）：
1. 放在服务器 CGI 目录（如 /usr/lib/cgi-bin/ 或 Apache 的 cgi-bin），
   配置为可执行，访问 http://你的域名/cgi-bin/echo.py
2. 本地测试：
   python -m http.server --cgi 8000
   （把本文件放到 cgi-bin 子目录下）

注意：纯静态托管（如 GitHub Pages）不支持 CGI，此时请使用 README 中的方案A（httpbin.org）。
"""
import cgi
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/plain; charset=utf-8\n")

form = cgi.FieldStorage()

print("== 回显你提交的参数 ==")
if not form:
    print("(没有接收到任何参数)")

for key in form.keys():
    values = form.getlist(key)
    for v in values:
        print(f"{key} = {v}")

# 也展示原始查询串（GET）
import os
qs = os.environ.get('QUERY_STRING', '')
if qs:
    print(f"\nQUERY_STRING = {qs}")
