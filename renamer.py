import os
import re

def shave_names(folder, words):
    """
    Renames files in the given folder by removing specified words from filenames (case-insensitive).
    Returns a list of skipped files (if any).
    """
    skipped_files = []
    # Sort words by length (longest first) to avoid partial overlaps
    words_sorted = sorted([w for w in words if w], key=len, reverse=True)
    words_lower = [w.lower() for w in words_sorted]
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
        if not os.path.isfile(old_path):
            continue  # Skip directories

        name, ext = os.path.splitext(filename)
        # Skip if the filename (without extension) matches any word to remove (case-insensitive)
        if name.lower() in words_lower:
            skipped_files.append(filename)
            continue

        new_name = filename
        for word in words_sorted:
            # Remove all occurrences of the word, case-insensitive
            new_name = re.sub(re.escape(word), '', new_name, flags=re.IGNORECASE)
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