import os
import shutil
def get_all_filepaths(root_path, check_path, output_path):
    all_files = []
    file_sizes = []
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            all_files.append(os.path.join(root, filename))
            file_sizes.append(os.path.getsize(os.path.join(root, filename)))
    for i in range (len(all_files)):
        temp_string = all_files[i]
        check = temp_string.replace(root_path, check_path)
        if os.path.exists(check):
            if file_sizes[i] != os.path.getsize(check):
                shutil.copy(check, output_path)
        elif not os.path.exists(check):
            shutil.copy(all_files[i], output_path)

get_all_filepaths("C:\\root", "C:\\check", "C:\\output")