def get_file_content(working_directory, file_path):
    
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, f)] != abs_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(f):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    f.read(CHAR_LIMIT)
    if 
