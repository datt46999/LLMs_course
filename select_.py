import nbformat
import os

def clean_notebook(path):
    try:
        nb = nbformat.read(path, as_version=4)
        if "widgets" in nb.get("metadata", {}):
            del nb["metadata"]["widgets"]
            nbformat.write(nb, path)
            print(f"Fixed: {path}")
    except Exception as e:
        print(f"Error: {path} - {e}")

root_dir = "."  # thư mục gốc (đổi nếu cần)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".ipynb"):
            clean_notebook(os.path.join(root, file))