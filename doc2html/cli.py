#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Doc2HTML CLI - Command Line Interface
"""

import os
import argparse
from .converter import MarkdownToHtmlConverter
from .__version__ import __version__


def main():
    """主入口函数"""
    parser = argparse.ArgumentParser(
        description='将文件夹下所有markdown文件转换成HTML页面',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  doc2html .                           # 转换当前目录
  doc2html /path/to/docs               # 转换指定目录
  doc2html /path/to/docs -o output     # 指定输出目录
  md2html docs --version               # 查看版本信息
        """
    )
    
    parser.add_argument(
        'source_dir', 
        help='源目录路径'
    )
    
    parser.add_argument(
        '-o', '--output', 
        help='输出目录路径，默认为源目录下的html_output'
    )
    
    parser.add_argument(
        '--version', 
        action='version', 
        version=f'doc2html {__version__}'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='显示详细输出'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='静默模式，只显示错误'
    )
    
    args = parser.parse_args()
    
    # 检查源目录是否存在
    if not os.path.exists(args.source_dir):
        print(f"错误: 源目录不存在: {args.source_dir}")
        return 1
    
    try:
        # 创建转换器并运行
        converter = MarkdownToHtmlConverter(args.source_dir, args.output)
        converter.run()
        return 0
        
    except KeyboardInterrupt:
        print("\n\n❌ 用户中断操作")
        return 1
        
    except Exception as e:
        print(f"❌ 发生错误: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
