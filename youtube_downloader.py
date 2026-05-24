import yt_dlp
import os
import sys

def main():
    print("=" * 40)
    print("  YouTube 视频下载器")
    print("=" * 40)
    
    url = input("\n请粘贴视频链接: ").strip()
    if not url:
        input("链接不能为空，按回车退出...")
        return
    
    # 下载到桌面
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    save_path = os.path.join(desktop, "YouTube下载")
    os.makedirs(save_path, exist_ok=True)
    
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    print(f"\n📁 保存位置: {save_path}")
    print("⏬ 开始下载...\n")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✅ 下载完成！")
    except Exception as e:
        print(f"\n❌ 下载失败: {e}")
        print("\n可能原因：网络问题或视频链接无效")
    
    input("\n按回车退出...")

if __name__ == "__main__":
    main()
