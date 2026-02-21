# Instagram 图片下载器 - 重要说明

## ⚠️ 法律和伦理警告

**此程序仅供教育学习用途,使用前请务必了解以下事项:**

1. **Instagram 服务条款**: 未经授权的自动化爬取违反 Instagram 服务条款
2. **隐私保护**: 个人照片受隐私权保护,下载他人内容需获得明确授权
3. **法律责任**: 未经授权抓取可能面临法律风险
4. **账号安全**: 自动化操作可能导致账号被封禁

## 合法替代方案

### 1. 使用 Instagram 官方 API
```python
# Instagram Basic Display API (官方)
# 文档: https://developers.facebook.com/docs/instagram-basic-display-api
```

### 2. 合法的第三方服务
- **Unsplash**: 免费高质量图片 (需标注作者)
- **Pexels**: 免费图库
- **Pixabay**: 免费图库

### 3. 仅下载自己的内容
如果你要下载**自己账号**的内容,可以:
- 使用 Instagram 官方"数据下载"功能
- 通过官方 API 访问自己的媒体

## 安装依赖

```bash
pip install requests beautifulsoup4
```

## 使用方法

```bash
# 示例 (仅用于你拥有版权的内容)
python instagram_image_downloader.py "your_tag" /path/to/save -n 10
```

## 更好的替代方案

### 使用 Unsplash API (免费合法)

```python
import requests

def download_from_unsplash(keyword, save_path, count=10):
    """从 Unsplash 下载免费图片"""
    import os
    from pathlib import Path

    Path(save_path).mkdir(parents=True, exist_ok=True)

    url = "https://api.unsplash.com/search/photos"
    params = {
        'query': keyword,
        'per_page': count,
        'client_id': 'your_unsplash_access_key'  # 免费注册获取
    }

    response = requests.get(url, params=params)
    data = response.json()

    for i, photo in enumerate(data['results']):
        img_url = photo['urls']['regular']
        filename = f"{keyword}_{i+1}.jpg"
        filepath = os.path.join(save_path, filename)

        # 下载图片
        img_data = requests.get(img_url).content
        with open(filepath, 'wb') as f:
            f.write(img_data)

        # 标注作者信息
        print(f"下载: {filename} | 作者: {photo['user']['name']}")
```

### 使用 Pexels API

```python
def download_from_pexels(keyword, save_path, count=10):
    """从 Pexels 下载免费图片"""
    import requests

    Path(save_path).mkdir(parents=True, exist_ok=True)

    url = "https://api.pexels.com/v1/search"
    headers = {
        'Authorization': 'your_pexels_api_key'  # 免费注册
    }
    params = {
        'query': keyword,
        'per_page': count
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    for i, photo in enumerate(data['photos']):
        img_url = photo['src']['medium']
        filename = f"{keyword}_{i+1}.jpg"
        filepath = os.path.join(save_path, filename)

        img_data = requests.get(img_url).content
        with open(filepath, 'wb') as f:
            f.write(img_data)
```

## 总结

**推荐做法:**
1. 使用 Unsplash、Pexels 等免费图库
2. 仅下载你自己拥有版权的内容
3. 获得明确授权后再下载他人内容
4. 遵守所有平台的服务条款

**不要:**
- 未经授权爬取他人内容
- 侵犯个人隐私
- 违反服务条款
- 用于商业用途而未获得许可

---

*本代码仅用于教育目的,使用者需自行承担法律责任*
