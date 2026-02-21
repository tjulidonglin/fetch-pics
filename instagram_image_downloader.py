#!/usr/bin/env python3
"""
Instagram 图片下载器 - 学习用途
注意: 使用前请确保遵守 Instagram 服务条款和相关法律法规
"""

import os
import re
import json
import argparse
import getpass
from pathlib import Path
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup


class InstagramImageDownloader:
    def __init__(self, save_path: str, username: str = None, password: str = None):
        """初始化下载器

        Args:
            save_path: 图片保存路径
            username: Instagram 用户名 (可选)
            password: Instagram 密码 (可选)
        """
        self.save_path = Path(save_path)
        self.save_path.mkdir(parents=True, exist_ok=True)

        # 设置请求头模拟浏览器
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.instagram.com/',
            'X-Requested-With': 'XMLHttpRequest',
        }

        # 初始化 session
        self.session = requests.Session()

        # 如果提供了用户名和密码，尝试登录
        if username and password:
            if self._login(username, password):
                print(f"[SUCCESS] 已成功登录 Instagram 账号: {username}")
            else:
                print(f"[ERROR] Instagram 登录失败")
                print("[WARNING] 将尝试使用未认证方式访问 (功能可能受限)")

    def search_and_download(self, keyword: str, max_images: int = 10):
        """
        搜索并下载图片

        Args:
            keyword: 搜索关键词
            max_images: 最大下载图片数量

        Returns:
            int: 成功下载的图片数量
        """
        print(f"[INFO] 搜索关键词: {keyword}")
        print(f"[INFO] 保存路径: {self.save_path}")
        print(f"[INFO] 最大下载数量: {max_images}")

        # 注意: Instagram 需要登录才能访问内容
        # 以下方法仅用于教育演示

        downloaded_count = 0

        try:
            # 方法1: 搜索 Instagram 公开标签页面 (需要登录cookie)
            # 这是一个简化示例
            search_url = f"https://www.instagram.com/explore/tags/{quote(keyword)}/"

            print(f"[INFO] 访问: {search_url}")

            # 注意: 这里需要添加你的 Instagram cookie 才能访问
            # response = requests.get(search_url, headers=self.headers)
            # 实际使用需要登录态

            print("[WARNING] Instagram 需要登录才能访问内容")
            print("[WARNING] 请参考官方 API 或使用合法的第三方服务")

        except Exception as e:
            print(f"[ERROR] 发生错误: {str(e)}")

        return downloaded_count

    def _login(self, username: str, password: str) -> bool:
        """
        Instagram 登录认证

        Args:
            username: 用户名
            password: 密码

        Returns:
            bool: 是否登录成功
        """
        try:
            # 第一步: 获取 CSRF token
            print("[INFO] 正在获取登录页面...")
            login_url = 'https://www.instagram.com/accounts/login/'
            response = self.session.get(login_url, headers=self.headers, timeout=30)

            # 从 cookie 中提取 CSRF token
            csrf_token = self.session.cookies.get('csrftoken')
            if not csrf_token:
                # 尝试从页面内容中提取
                match = re.search(r'"csrf_token":"([^"]+)"', response.text)
                if match:
                    csrf_token = match.group(1)
                else:
                    csrf_token = 'missing'

            self.headers['X-CSRFToken'] = csrf_token

            # 第二步: 提交登录表单
            print("[INFO] 正在登录...")
            # Instagram 加密密码格式: #PWD_INSTAGRAM_BROWSER:<时间戳>:<密码>
            # 使用固定的时间戳格式
            import time
            timestamp = int(time.time())
            login_data = {
                'username': username,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}'
            }

            login_api_url = 'https://www.instagram.com/accounts/login/ajax/'
            login_response = self.session.post(
                login_api_url,
                headers=self.headers,
                data=login_data,
                timeout=30
            )

            login_result = login_response.json()

            # 检查登录结果
            if login_result.get('authenticated') or login_result.get('status') == 'ok':
                print(f"[SUCCESS] 账号认证成功")
                # 更新 headers 使用认证后的 session
                self.session.headers.update(self.headers)
                return True
            elif login_result.get('message') == 'checkpoint_required':
                print("[ERROR] 需要进行账号安全验证 (两步验证/人机验证)")
                print("[INFO] 请在浏览器中登录 Instagram 完成验证后重试")
                return False
            else:
                print("[ERROR] 登录失败")
                error_message = login_result.get('message', '未知错误')
                print(f"[ERROR] 错误信息: {error_message}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] 网络请求失败: {str(e)}")
            return False
        except json.JSONDecodeError:
            print("[ERROR] 登录响应格式错误")
            return False
        except Exception as e:
            print(f"[ERROR] 登录过程发生错误: {str(e)}")
            return False

    def download_image(self, image_url: str, filename: str) -> bool:
        """
        下载单张图片

        Args:
            image_url: 图片 URL
            filename: 保存文件名

        Returns:
            bool: 是否下载成功
        """
        try:
            response = self.session.get(image_url, headers=self.headers, timeout=30)
            response.raise_for_status()

            file_path = self.save_path / filename

            with open(file_path, 'wb') as f:
                f.write(response.content)

            print(f"[SUCCESS] 下载完成: {filename}")
            return True

        except Exception as e:
            print(f"[ERROR] 下载失败 {image_url}: {str(e)}")
            return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='Instagram 图片下载器 - 学习用途'
    )
    parser.add_argument(
        'keyword',
        type=str,
        help='搜索关键词(标签)'
    )
    parser.add_argument(
        'save_path',
        type=str,
        help='图片保存路径'
    )
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=10,
        help='最大下载图片数量 (默认: 10)'
    )
    parser.add_argument(
        '-u', '--username',
        type=str,
        help='Instagram 用户名 (登录后可访问更多内容)'
    )
    parser.add_argument(
        '-p', '--password',
        type=str,
        help='Instagram 密码 (不提供则以访客身份访问)'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Instagram Image Downloader - Learning Purpose Only")
    print("=" * 60)
    print()

    # 如果提供了用户名但没有提供密码，提示用户输入密码 (隐藏输入)
    username = args.username
    password = args.password

    if username and not password:
        password = getpass.getpass(f"请输入 Instagram 账号 {username} 的密码: ")
    elif not username:
        print("[INFO] 未提供登录信息，将以访客身份访问 (功能可能受限)")
        print("[INFO] 使用 -u 和 -p 参数可以登录账号")
        print()

    # 创建下载器实例
    downloader = InstagramImageDownloader(
        save_path=args.save_path,
        username=username,
        password=password
    )

    # 执行搜索和下载
    count = downloader.search_and_download(
        keyword=args.keyword,
        max_images=args.number
    )

    print()
    print("=" * 60)
    print(f"完成! 成功下载 {count} 张图片")
    print("=" * 60)


if __name__ == "__main__":
    main()
