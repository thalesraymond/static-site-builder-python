import os
import shutil
import sys
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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_public, base_path="/"):
    print(
        f"Generating pages from {dir_path_content} to {dest_dir_public} using {template_path}"
    )

    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_public, item)

        if os.path.isfile(from_path):
            if item.endswith(".md"):
                print(f"Current file: {from_path}")
                dest_path = dest_path[:-3] + ".html"
                generate_page(from_path, template_path, dest_path, base_path)
        else:
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            generate_pages_recursive(from_path, template_path, dest_path, base_path)


def main():
    # root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    path = Path(__file__).resolve()
    root_dir = str(path.parent.parent.resolve().absolute())

    print(root_dir)
    static_path = os.path.join(root_dir, "static")
    public_path = os.path.join(root_dir, "docs")

    print(f"Cleaning public directory at {public_path}...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print(f"Copying static files from {static_path} to {public_path}...")
    copy_recursive(static_path, public_path)

    # generate pages from content

    content_path = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")
    generate_pages_recursive(content_path, template_path, public_path, base_path)


if __name__ == "__main__":
    main()
