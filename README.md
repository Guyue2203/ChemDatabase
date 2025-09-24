# ChemDatabase - 化学分子数据库管理系统

## 项目简介

ChemDatabase 是一个基于 Django 框架开发的化学分子数据库管理系统，专门用于存储、管理和搜索化学分子信息。该系统提供了完整的化学数据管理功能，包括分子结构信息、物理化学性质、相似性分析等。

## 主要功能

### 🔍 数据搜索功能
- **模糊搜索**: 支持通过化合物名称、同义词等关键词进行模糊搜索
- **结构搜索**: 支持通过分子结构进行搜索
- **详细查询**: 提供详细的分子信息展示页面
- **相似性分析**: 基于 Tanimoto 相似度算法计算分子间相似性

### 📊 数据管理功能
- **数据录入**: 支持单个和批量数据录入
- **数据审核**: 提供待审核数据管理机制
- **数据导出**: 支持将数据导出为 CSV 格式
- **文件管理**: 支持文件上传和管理

### 🎨 用户界面
- **响应式设计**: 现代化的 Web 界面设计
- **分页显示**: 支持大量数据的分页展示
- **后台管理**: 完整的 Django Admin 后台管理界面

## 技术栈

- **后端框架**: Django 5.1.1
- **数据库**: SQLite3
- **化学计算**: RDKit
- **前端技术**: HTML5, CSS3, JavaScript
- **数据格式**: CSV, SMILES, InChI

## 项目结构

```
ChemDatabase/
├── manage.py                 # Django 管理脚本
├── requirements.txt          # 项目依赖
├── db.sqlite3               # SQLite 数据库文件
├── task1/                   # Django 项目配置
│   ├── settings.py          # 项目设置
│   ├── urls.py              # 主 URL 配置
│   └── wsgi.py              # WSGI 配置
├── Chemai_data/             # 主应用
│   ├── models/              # 数据模型
│   │   ├── Chem_Database.py      # 化学分子数据库模型
│   │   ├── Test_Chem_Database.py # 待审核数据模型
│   │   ├── Similarity_data.py    # 相似性数据模型
│   │   ├── File_data.py          # 文件数据模型
│   │   └── Web_Function_Databas.py # Web 功能数据库模型
│   ├── views/               # 视图函数
│   │   ├── Index.py              # 首页视图
│   │   ├── Search_htm.py         # 搜索页面视图
│   │   ├── Add_Test_htm.py       # 数据添加页面视图
│   │   └── Back_end_See_File.py  # 后端文件查看视图
│   ├── Search_Chem_Database/     # 搜索功能模块
│   │   └── Search.py             # 搜索逻辑实现
│   ├── Manage_Chem_Database/     # 数据库管理模块
│   │   ├── Add_Test_Chem_Database.py      # 单个数据添加
│   │   ├── Batch_Add_Chem_Database.py     # 批量数据添加
│   │   ├── Similarity_calculate_Chem_Database.py # 相似性计算
│   │   ├── To_CSV_Test_Chem_Database.py   # CSV 导出
│   │   ├── Data_CAS_see.py                # CAS 号重构
│   │   ├── Data_InchIkey_see.py           # InChIKey 重构
│   │   └── Data_Synonyms_see.py           # 同义词重构
│   ├── templates/           # HTML 模板
│   │   └── Chemai_data/
│   │       ├── index.html              # 首页模板
│   │       ├── indextext.html          # 搜索页面模板
│   │       ├── data_all.html           # 搜索结果展示模板
│   │       ├── data_details.html       # 详细数据展示模板
│   │       ├── data_details_de.html    # 详细数据展示模板（扩展版）
│   │       ├── Add_Test_Submit.html    # 数据提交表单模板
│   │       └── structure_to_smiles.html # 结构搜索模板
│   ├── static/              # 静态文件
│   ├── admin.py             # Django Admin 配置
│   ├── apps.py              # 应用配置
│   └── urls.py              # URL 路由配置
└── media/                   # 媒体文件存储目录
    └── Chemai_data/
        └── media/           # 用户上传文件
```

## 数据模型

### 1. Chem_mol (化学分子数据库)
存储完整的化学分子信息，包括：
- 基本信息：CAS号、分子式、SMILES、InChI、InChIKey
- 物理性质：沸点、熔点、密度、溶解度等
- 化学性质：分子量、氢键供体/受体数量等
- 光谱数据：NMR、质谱、红外光谱等
- 安全信息：化学品安全、稳定性等

### 2. Test_Chem_mol (待审核数据)
存储用户提交的待审核化学数据，结构与 Chem_mol 相同。

### 3. Sim (相似性数据)
存储分子间的相似性计算结果，包括相似度分数和相关分子信息。

### 4. Fil (文件数据)
管理用户上传的文件信息，包括文件名、上传时间、IP地址等。

## 安装和运行

### 环境要求
- Python 3.8+
- Django 5.1.1
- RDKit (用于化学计算)

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd ChemDatabase
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **数据库迁移**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **创建超级用户**
```bash
python manage.py createsuperuser
```

5. **运行开发服务器**
```bash
python manage.py runserver
```

6. **访问应用**
- 前端界面: http://127.0.0.1:8000/Chemai_data/
- 后台管理: http://127.0.0.1:8000/admin/

## 使用说明

### 数据搜索
1. 访问首页，在搜索框中输入化合物名称或关键词
2. 点击搜索按钮查看结果
3. 点击"更多信息"查看详细数据
4. 查看相似性分子推荐

### 数据管理
1. 登录后台管理系统
2. 在"化学分子数据库"中添加、编辑或删除数据
3. 使用批量操作功能进行数据管理
4. 查看和管理待审核数据

### 文件上传
1. 在后台管理系统中上传 CSV 文件
2. 使用"读文件数据至数据库"功能将数据导入系统
3. 支持批量数据导入和更新

## 主要特性

### 化学计算功能
- **分子相似性计算**: 使用 RDKit 的 Morgan 指纹和 Tanimoto 相似度算法
- **结构转换**: 支持 SMILES 到 InChI、InChIKey 的转换
- **分子验证**: 自动验证分子结构的有效性

### 数据完整性
- **CAS号验证**: 自动验证和格式化 CAS 号
- **数据重构**: 支持基于 SMILES 重构 InChIKey 和同义词
- **重复检测**: 基于 InChIKey 防止重复数据

### 用户体验
- **响应式设计**: 适配不同屏幕尺寸
- **分页功能**: 支持大量数据的分页显示
- **搜索优化**: 支持模糊搜索和精确匹配

## 开发团队

本项目由 RUC ChemAI 团队开发，专注于化学信息学领域的数据库管理系统开发。

## 许可证

本项目采用开源许可证，具体信息请查看 LICENSE 文件。

## 贡献指南

欢迎提交 Issue 和 Pull Request 来改进项目。在提交代码前，请确保：
1. 代码符合项目规范
2. 添加必要的测试
3. 更新相关文档

## 联系方式

如有问题或建议，请通过以下方式联系：
- 邮箱: [hi@guyue.me]

