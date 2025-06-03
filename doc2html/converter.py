#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to HTML Converter Tool
将文件夹下所有markdown文件转换成HTML页面的工具
"""

import os
import re
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

try:
    import markdown
    from markdown.extensions import codehilite, toc, tables, fenced_code
except ImportError:
    raise ImportError("需要安装markdown库: pip install markdown")

class MarkdownToHtmlConverter:
    def __init__(self, source_dir: str, output_dir: str = None):
        """
        初始化转换器
        
        Args:
            source_dir: 源目录路径
            output_dir: 输出目录路径，默认为源目录下的html_output
        """
        self.source_dir = Path(source_dir).resolve()
        self.output_dir = Path(output_dir) if output_dir else self.source_dir / "html_output"
        self.md_files = []
        self.directory_structure = {}
        
        # 确保输出目录存在
        self.output_dir.mkdir(exist_ok=True)
        
        # 模板目录 - 使用包内的模板
        self.template_dir = Path(__file__).parent / "templates"
        
        # 配置markdown扩展
        self.md_extensions = [
            'codehilite',
            'toc',
            'tables',
            'fenced_code',
            'nl2br',
            'attr_list'
        ]
        
        # TOC配置
        self.md_extension_configs = {
            'toc': {
                'anchorlink': True,
                'baselevel': 1,
                'permalink': True
            }
        }
        
        # 加载HTML模板
        self._load_templates()

    def _load_templates(self) -> None:
        """加载HTML模板"""
        try:
            # 加载文档模板
            doc_template_path = self.template_dir / "document_template.html"
            with open(doc_template_path, 'r', encoding='utf-8') as f:
                self.html_template = f.read()
            
            # 加载索引模板
            index_template_path = self.template_dir / "index_template.html"
            with open(index_template_path, 'r', encoding='utf-8') as f:
                self.index_template = f.read()
                
            print(f"✅ 模板加载成功: {self.template_dir}")
            
        except FileNotFoundError as e:
            print(f"❌ 模板文件未找到: {e}")
            print("使用内置模板...")
            self._use_builtin_templates()
        except Exception as e:
            print(f"❌ 模板加载失败: {e}")
            print("使用内置模板...")
            self._use_builtin_templates()

    def _use_builtin_templates(self) -> None:
        """使用内置模板（备用方案）"""
        print("❌ 无法加载外部模板文件，程序无法继续运行")
        print("请确保templates目录下存在以下文件:")
        print("  - document_template.html")
        print("  - index_template.html")
        raise FileNotFoundError("模板文件未找到")

    def scan_directory(self) -> None:
        """扫描目录，建立索引"""
        print(f"正在扫描目录: {self.source_dir}")
        
        for root, dirs, files in os.walk(self.source_dir):
            # 跳过输出目录
            if self.output_dir.name in dirs:
                dirs.remove(self.output_dir.name)
            
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    relative_path = file_path.relative_to(self.source_dir)
                    
                    # 获取文件信息
                    file_info = {
                        'path': file_path,
                        'relative_path': relative_path,
                        'name': file_path.stem,
                        'size': file_path.stat().st_size,
                        'modified': datetime.fromtimestamp(file_path.stat().st_mtime),
                        'directory': relative_path.parent
                    }
                    
                    self.md_files.append(file_info)
        
        print(f"找到 {len(self.md_files)} 个 Markdown 文件")
        
        # 构建目录结构
        self._build_directory_structure()

    def _build_directory_structure(self) -> None:
        """构建目录结构"""
        self.directory_structure = {}
        
        for file_info in self.md_files:
            parts = file_info['relative_path'].parts
            current_dict = self.directory_structure
            
            # 构建目录树
            for part in parts[:-1]:  # 排除文件名
                if part not in current_dict:
                    current_dict[part] = {}
                current_dict = current_dict[part]
            
            # 添加文件
            if 'files' not in current_dict:
                current_dict['files'] = []
            current_dict['files'].append(file_info)

    def convert_file(self, file_info: Dict) -> str:
        """转换单个markdown文件"""
        try:
            # 读取markdown文件
            with open(file_info['path'], 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # 创建markdown实例
            md = markdown.Markdown(
                extensions=self.md_extensions,
                extension_configs=self.md_extension_configs
            )
            
            # 转换为HTML
            html_content = md.convert(md_content)
            
            # 生成目录
            toc_html = ""
            if hasattr(md, 'toc') and md.toc:
                toc_html = f'<div class="toc"><h3>目录</h3>{md.toc}</div>'
            else:
                # 如果没有目录，显示空的占位符
                toc_html = ''
            
            # 生成面包屑导航
            breadcrumb = self._generate_breadcrumb(file_info['relative_path'])
            
            # 计算相对于根目录的深度，用于生成正确的返回索引链接
            depth = len(file_info['relative_path'].parts) - 1
            index_path = "../" * depth + "index.html" if depth > 0 else "index.html"
            back_link = f'<a href="{index_path}" class="back-to-index"> 返回索引</a>'
            
            # 生成完整的HTML
            full_html = self.html_template.format(
                title=file_info['name'],
                breadcrumb=breadcrumb,
                back_link=back_link,
                toc=toc_html,
                content=html_content,
                timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
            
            # 保持目录结构 - 将.md扩展名替换为.html
            output_relative_path = file_info['relative_path'].with_suffix('.html')
            output_file = self.output_dir / output_relative_path
            
            # 确保输出目录存在
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入HTML文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_html)
            
            print(f"✅ 转换完成: {file_info['relative_path']} -> {output_relative_path}")
            
            # 将生成的文件路径保存到file_info中以便索引页面使用
            file_info['html_relative_path'] = output_relative_path
            
            return str(output_relative_path)
            
        except Exception as e:
            print(f"❌ 转换失败: {file_info['relative_path']} - {str(e)}")
            return None

    def _generate_breadcrumb(self, relative_path: Path) -> str:
        """生成面包屑导航"""
        parts = ['<a href="index.html">首页</a>']
        
        if relative_path.parent != Path('.'):
            for part in relative_path.parent.parts:
                parts.append(part)
        
        parts.append(relative_path.name)
        return ' / '.join(parts)

    def _generate_directory_tree_html(self, structure: Dict, prefix: str = "") -> str:
        """生成目录树HTML"""
        html = ""
        
        for key, value in structure.items():
            if key == 'files':
                # 显示文件
                for file_info in value:
                    html_relative_path = file_info.get('html_relative_path', f"{file_info['name']}.html")
                    file_link = f'<a href="{html_relative_path}">{file_info["relative_path"].name}</a>'
                    html += f'<div class="tree-item tree-file">{prefix}📄 {file_link}</div>\n'
            else:
                # 显示目录
                html += f'<div class="tree-item tree-folder">{prefix}📁 {key}/</div>\n'
                html += self._generate_directory_tree_html(value, prefix + "  ")
        
        return html

    def generate_index_page(self) -> None:
        """生成索引页面"""
        print("正在生成索引页面...")
        
        # 生成文件卡片
        file_cards = ""
        for file_info in sorted(self.md_files, key=lambda x: x['relative_path']):
            # 尝试读取文件开头作为预览
            preview = ""
            try:
                with open(file_info['path'], 'r', encoding='utf-8') as f:
                    content = f.read(200)
                    # 移除markdown标记
                    preview = re.sub(r'[#*`\[\]()]', '', content).strip()
                    if len(preview) > 100:
                        preview = preview[:100] + "..."
            except:
                preview = "无法读取预览"
            
            file_card = f"""
            <div class="file-card">
                <div class="file-title">
                    <a href="{file_info.get('html_relative_path', f'{file_info["name"]}.html')}"> {file_info['name']}</a>
                </div>
                <div class="file-path">{file_info['relative_path']}</div>
                <div class="file-info">
                    大小: {file_info['size']} 字节 | 
                    修改时间: {file_info['modified'].strftime('%Y-%m-%d %H:%M')}
                </div>
                <div style="margin-top: 10px; font-size: 14px; color: #666;">
                    {preview}
                </div>
            </div>
            """
            file_cards += file_card
        
        # 生成目录树
        directory_tree_html = self._generate_directory_tree_html(self.directory_structure)
        
        # 统计信息
        total_dirs = len(set(file_info['directory'] for file_info in self.md_files))
        total_size = sum(file_info['size'] for file_info in self.md_files)
        
        # 格式化总大小
        if total_size < 1024:
            size_str = f"{total_size} B"
        elif total_size < 1024 * 1024:
            size_str = f"{total_size / 1024:.1f} KB"
        else:
            size_str = f"{total_size / (1024 * 1024):.1f} MB"
        
        # 计算生成时间（假设平均每个文件需要一定时间）
        generation_time = f"{len(self.md_files) * 0.1:.1f}s"
        
        # 生成索引页面
        index_html = self.index_template.format(
            source_dir=self.source_dir,
            total_files=len(self.md_files),
            total_dirs=total_dirs,
            total_size=size_str,
            generation_time=generation_time,
            directory_tree=directory_tree_html,
            file_cards=file_cards,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        
        # 写入索引文件
        index_file = self.output_dir / "index.html"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_html)
        
        print(f"✅ 索引页面生成完成: {index_file}")

    def convert_all(self) -> None:
        """转换所有文件"""
        print("开始转换所有Markdown文件...")
        
        successful_conversions = 0
        failed_conversions = 0
        
        for file_info in self.md_files:
            result = self.convert_file(file_info)
            if result:
                successful_conversions += 1
            else:
                failed_conversions += 1
        
        print(f"\n转换完成!")
        print(f"✅ 成功: {successful_conversions} 个文件")
        print(f"❌ 失败: {failed_conversions} 个文件")
        print(f"📁 输出目录: {self.output_dir}")

    def run(self) -> None:
        """运行转换流程"""
        print("=== Markdown to HTML 转换器 ===\n")
        
        # 1. 扫描目录建立索引
        self.scan_directory()
        
        # 2. 转换所有markdown文件
        self.convert_all()
        
        # 3. 生成索引页面
        self.generate_index_page()
        
        print(f"\n🎉 所有任务完成! 请打开 {self.output_dir}/index.html 查看结果")
