import os

def shave_names(folder, words):
    """
    Renames files in the given folder by removing specified words from filenames.
    Returns a list of skipped files (if any).
    """
    skipped_files = []
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
        if not os.path.isfile(old_path):
            continue  # Skip directories

        # --- PLACE FOR CUSTOM SKIP LOGIC ---
        # Example: skip files that start with 'skip_'
        # if filename.startswith('skip_'):
        #     skipped_files.append(filename)
        #     continue

        new_name = filename
        for word in words:
            new_name = new_name.replace(word, "")
        new_name = new_name.strip()
        if new_name == filename or not new_name:
            skipped_files.append(filename)
            continue
        new_path = os.path.join(folder, new_name)
        # Avoid overwriting existing files
        if os.path.exists(new_path):
            skipped_files.append(filename)
            continue
        os.rename(old_path, new_path)
    return skipped_files