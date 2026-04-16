import nbformat
import os

def clean_notebook(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        # chỉ xóa widgets metadata, không đụng gì khác
        if "widgets" in nb.metadata:
            del nb.metadata["widgets"]

            with open(path, "w", encoding="utf-8") as f:
                nbformat.write(nb, f)

            print(f"Fixed: {path}")
        else:
            print(f"Skip (no widgets): {path}")

    except Exception as e:
        print(f"Error: {path} - {e}")


root_dir = "."

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".ipynb"):
            clean_notebook(os.path.join(root, file))