from PIL import Image
import os

def compress_image(file_path, quality):
    try:
        with Image.open(file_path) as im:
            im.save(file_path, quality=quality)
    except IOError:
        print(f"无法打开文件：{file_path}")

if __name__ == '__main__':
    # 要压缩的图片文件夹路径
    folder_path = "./Images"
    # 压缩质量
    quality = 30

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            file_path = os.path.join(folder_path, filename)
            compress_image(file_path, quality)
            print(f"{file_path} 压缩完成")