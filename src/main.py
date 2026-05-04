import os
import shutil
from pathlib import Path

from src.markdown.converter import generate_page

def copy_recursive(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            print(f"Copying {src_path} to {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            copy_recursive(src_path, dest_path)


def main():
    #root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = Path(__file__).resolve()
    root_dir = str(path.parent.parent.resolve().absolute())
    print(root_dir)
    static_path = os.path.join(root_dir, "static")
    public_path = os.path.join(root_dir, "public")

    print(f"Cleaning public directory at {public_path}...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print(f"Copying static files from {static_path} to {public_path}...")
    copy_recursive(static_path, public_path)
    
    # generate pages from content

    content_path = os.path.join(root_dir, "content")
    for filename in os.listdir(content_path):
        if filename.endswith(".md"):
            from_path = os.path.join(content_path, filename)
            template_path = os.path.join(root_dir, "template.html")
            dest_filename = filename[:-3] + ".html"
            dest_path = os.path.join(public_path, dest_filename)
            generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()