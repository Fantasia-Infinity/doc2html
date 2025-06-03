# Doc2HTML - Markdown to HTML 转换器

[![PyPI version](https://badge.fury.io/py/doc2html.svg)](https://badge.fury.io/py/doc2html)
[![Python Support](https://img.shields.io/pypi/pyversions/doc2html.svg)](https://pypi.org/project/doc2html/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

这是一个将文件夹下所有markdown文件转换成HTML页面的工具，现已支持通过 pip 安装！

## 安装

### 通过 pip 安装（推荐）

```bash
pip install doc2html
```

### 从源码安装

```bash
git clone https://github.com/Fantasia-Infinity/doc2html.git
cd doc2html
pip install -e .
```

## 功能特性

- 🔍 **智能扫描**: 自动扫描目录下的所有markdown文件
- 📁 **目录索引**: 建立完整的目录结构索引
- 🌐 **单独页面**: 为每个markdown文件生成单独的HTML页面
- 📋 **综合索引**: 生成美观的综合索引页面
- 🎨 **现代UI**: 响应式设计，支持移动端
- 🔗 **导航系统**: 面包屑导航和返回索引链接
- 📖 **目录生成**: 自动生成文档目录
- 🚀 **快速处理**: 高效批量转换
- 📦 **易于安装**: 支持 pip 安装
- 🖥️ **命令行工具**: 提供 `doc2html` 和 `md2html` 命令

## 使用方法

### 命令行使用

安装后，你可以直接使用命令行工具：

```bash
# 转换当前目录
doc2html .

# 转换指定目录
doc2html /path/to/docs

# 指定输出目录
doc2html /path/to/docs -o /path/to/output

# 查看帮助
doc2html --help

# 查看版本
doc2html --version
```

### 在 Python 中使用

```python
from doc2html import convert_directory, MarkdownToHtmlConverter

# 快速转换
convert_directory("/path/to/docs")

# 更多控制
converter = MarkdownToHtmlConverter("/path/to/docs", "/path/to/output")
converter.run()
```

### 示例

```bash
# 转换当前目录下的所有markdown文件
doc2html .

# 转换指定目录并输出到自定义位置
doc2html /path/to/docs -o /path/to/output

# 转换整个代码仓库
doc2html /Users/shufanzhang/Documents/coderepos -o html_docs
```

## 依赖项

该工具会自动安装以下依赖：

- `markdown>=3.0.0` - Markdown 解析和转换
- `pygments>=2.0.0` - 代码语法高亮

## 输出结构

工具会生成以下文件：

- `index.html` - 主索引页面，包含所有文件的目录和预览
- `文件名_哈希值.html` - 每个markdown文件对应的HTML页面

## 功能说明

### 1. 目录扫描

- 递归扫描所有子目录
- 自动识别`.md`文件
- 跳过输出目录避免重复扫描

### 2. 文件转换

- 支持标准markdown语法
- 代码高亮
- 表格支持
- 目录生成
- 属性列表

### 3. 索引页面

- 文件统计信息
- 可视化目录树
- 文件卡片展示
- 文件预览
- 响应式布局

### 4. 导航功能

- 面包屑导航
- 返回索引链接
- 文件间跳转

## 支持的markdown扩展

- `codehilite` - 代码高亮
- `toc` - 目录生成
- `tables` - 表格支持
- `fenced_code` - 围栏代码块
- `nl2br` - 换行转换
- `attr_list` - 属性列表

## 样式特性

- 现代化UI设计
- 响应式布局
- 代码语法高亮
- 表格美化
- 引用块样式
- 文件卡片动效

## 开发

### 从源码安装开发版本

```bash
git clone https://github.com/Fantasia-Infinity/doc2html.git
cd doc2html
pip install -e ".[dev]"
```

### 构建包

```bash
python -m build
```

### 发布到 PyPI

```bash
python -m twine upload dist/*
```

## 版本信息

当前版本: 1.0.0

## 作者

Created by Fantasia-Infinity

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v1.0.0

- 🎉 首个正式版本
- ✨ 支持 pip 安装
- 🖥️ 提供命令行工具
- 📦 完整的 Python 包结构
- 🎨 美观的 HTML 模板
- 📚 完整的文档
