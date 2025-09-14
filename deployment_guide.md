# ChemDatabase 部署指南

## Media文件同步方案

### 方案1: 云存储 (推荐生产环境)

#### AWS S3 配置
```python
# requirements.txt 添加
boto3==1.26.137
django-storages==1.13.2

# settings.py 生产环境配置
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    # 媒体文件URL
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
```

#### 阿里云OSS 配置
```python
# requirements.txt 添加
oss2==2.17.0
django-oss-storage==0.1.0

# settings.py 配置
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'
    STATICFILES_STORAGE = 'django_oss_storage.backends.OssStaticStorage'
    
    OSS_ACCESS_KEY_ID = os.environ.get('OSS_ACCESS_KEY_ID')
    OSS_ACCESS_KEY_SECRET = os.environ.get('OSS_ACCESS_KEY_SECRET')
    OSS_BUCKET_NAME = os.environ.get('OSS_BUCKET_NAME')
    OSS_ENDPOINT = 'oss-cn-hangzhou.aliyuncs.com'
```

### 方案2: 本地同步 (开发环境)

#### 使用rsync同步
```bash
# 创建同步脚本
cat > sync_media.sh << 'EOF'
#!/bin/bash
# 从主服务器同步media文件
rsync -avz --delete \
    --exclude='*.tmp' \
    --exclude='*.log' \
    user@main-server:/path/to/ChemDatabase/media/ \
    ./media/

echo "Media files synced at $(date)"
EOF

chmod +x sync_media.sh

# 设置定时同步 (可选)
# crontab -e
# */30 * * * * /path/to/sync_media.sh
```

#### 使用Git LFS (大文件支持)
```bash
# 安装Git LFS
git lfs install

# 跟踪大文件
git lfs track "media/**/*.png"
git lfs track "media/**/*.jpg"
git lfs track "media/**/*.pdf"

# 提交配置
git add .gitattributes
git commit -m "Add Git LFS tracking for media files"
```

### 方案3: Docker部署

#### docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - media_data:/app/media
      - static_data:/app/static
    environment:
      - DEBUG=False
      - AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
      - AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
      - AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME}
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: chemdatabase
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  media_data:
  static_data:
  postgres_data:
```

#### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 安装Python依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["gunicorn", "task1.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 环境变量配置

### .env 文件示例
```bash
# 数据库配置
DATABASE_URL=postgresql://user:password@localhost:5432/chemdatabase

# AWS S3 配置
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name

# Django配置
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 部署步骤

### 1. 生产环境部署
```bash
# 1. 克隆代码
git clone <repository-url>
cd ChemDatabase

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑.env文件

# 4. 数据库迁移
python manage.py migrate

# 5. 收集静态文件
python manage.py collectstatic

# 6. 创建超级用户
python manage.py createsuperuser

# 7. 启动服务
gunicorn task1.wsgi:application --bind 0.0.0.0:8000
```

### 2. 使用Docker部署
```bash
# 1. 构建镜像
docker-compose build

# 2. 启动服务
docker-compose up -d

# 3. 执行数据库迁移
docker-compose exec web python manage.py migrate

# 4. 创建超级用户
docker-compose exec web python manage.py createsuperuser
```

## 备份策略

### 数据库备份
```bash
# PostgreSQL备份
pg_dump -h localhost -U postgres chemdatabase > backup_$(date +%Y%m%d).sql

# 恢复
psql -h localhost -U postgres chemdatabase < backup_20231201.sql
```

### Media文件备份
```bash
# 如果使用云存储，启用版本控制
# 如果使用本地存储，定期备份
tar -czf media_backup_$(date +%Y%m%d).tar.gz media/
```

## 监控和维护

### 日志配置
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### 健康检查
```python
# 创建健康检查端点
def health_check(request):
    return JsonResponse({'status': 'healthy', 'timestamp': timezone.now()})
```
