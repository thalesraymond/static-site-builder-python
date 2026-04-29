import os
import shutil


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
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_path = os.path.join(root_dir, "static")
    public_path = os.path.join(root_dir, "public")

    print(f"Cleaning public directory at {public_path}...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print(f"Copying static files from {static_path} to {public_path}...")
    copy_recursive(static_path, public_path)

if __name__ == "__main__":
    main()