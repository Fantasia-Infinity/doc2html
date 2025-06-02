# Markdown to HTML 转换器

这是一个将文件夹下所有markdown文件转换成HTML页面的工具。

## 功能特性

- 🔍 **智能扫描**: 自动扫描目录下的所有markdown文件
- 📁 **目录索引**: 建立完整的目录结构索引
- 🌐 **单独页面**: 为每个markdown文件生成单独的HTML页面
- 📋 **综合索引**: 生成美观的综合索引页面
- 🎨 **现代UI**: 响应式设计，支持移动端
- 🔗 **导航系统**: 面包屑导航和返回索引链接
- 📖 **目录生成**: 自动生成文档目录
- 🚀 **快速处理**: 高效批量转换

## 使用方法

### 基本用法

```bash
python mk2html.py <源目录路径>
```

### 指定输出目录

```bash
python mk2html.py <源目录路径> -o <输出目录路径>
```

### 示例

```bash
# 转换当前目录下的所有markdown文件
python mk2html.py .

# 转换指定目录并输出到自定义位置
python mk2html.py /path/to/docs -o /path/to/output

# 转换整个代码仓库
python mk2html.py /Users/shufanzhang/Documents/coderepos -o html_docs
```

## 安装依赖

```bash
pip install markdown
```

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

## 版本信息

当前版本: 1.0.0

## 作者

Created by GitHub Copilot

## 许可证

MIT License
