import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not abs_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", abs_file_path]
        if args is not None:
            command.extend(args)
        process_obj = subprocess.run(command, capture_output=True, cwd=abs_working_dir, text=True, timeout=30)
        out_string_list = [] 
        if process_obj.returncode != 0:
            out_string_list.append(f'Process exited with code {process_obj.returncode}')
        if not process_obj.stdout and not process_obj.stderr:
            out_string_list.append("No output produced")
        if process_obj.stdout:
            out_string_list.append(f'STDOUT: {process_obj.stdout}')
        if process_obj.stderr:    
            out_string_list.append(f'STDERR: {process_obj.stderr}')
        return "\n".join(out_string_list)
    except Exception as e:
        return f"Error: executing Python file: {e}"

