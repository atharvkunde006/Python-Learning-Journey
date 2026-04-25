import os

folder = "clusterfolder"
files = os.listdir(folder)
i = 1

for file in files:
    if file.lower().endswith((".jpg", ".jpeg")):
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, f"clusterfolder{i}.jpg")
        print(f"{file} -> clusterfolder{i}.jpg")
        os.rename(old_path, new_path)
        i += 1
