#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Doc2HTML - Markdown to HTML Converter
将文件夹下所有markdown文件转换成HTML页面的工具
"""

from .__version__ import __version__, __author__, __email__, __description__
from .converter import MarkdownToHtmlConverter

__all__ = [
    "MarkdownToHtmlConverter",
    "__version__",
    "__author__",
    "__email__",
    "__description__",
]

# 简化的API
def convert_directory(source_dir, output_dir=None):
    """
    快速转换目录下的所有Markdown文件
    
    Args:
        source_dir (str): 源目录路径
        output_dir (str, optional): 输出目录路径，默认为源目录下的html_output
    
    Returns:
        MarkdownToHtmlConverter: 转换器实例
    """
    converter = MarkdownToHtmlConverter(source_dir, output_dir)
    converter.run()
    return converter
