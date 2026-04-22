import os

def rename_dirs(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        if '.git' in dirs:
            dirs.remove('.git')
        for name in dirs:
            new_name = name.lower()
            if new_name != name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                
                if os.path.exists(new_path) and old_path.lower() != new_path.lower():
                     print(f"Warning: Cannot rename {old_path} to {new_path} because it already exists.")
                     continue

                # On Linux, renaming 'Newsletter' to 'newsletter' works fine.
                # On case-insensitive systems, we need a temp name.
                temp_path = old_path + "_temp_rename"
                os.rename(old_path, temp_path)
                os.rename(temp_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    rename_dirs('.')
