```cmd
python print_files.py --start_directory C:/git/project_dir/ --extension .py --list_files
python print_files.py --start_directory C:/git/project_dir/ --extension .py --list_files --recursive
python print_files.py --start_directory C:/git/project_dir/ --extension .py --list_files --recursive --ignore *env\*
python print_files.py --start_directory C:/git/project_dir/ --extension .py --write --recursive --ignore *env\*
python print_files.py --start_directory C:/git/project_dir/ --filter file1.py file2.py file3.json --list_files
python print_files.py --start_directory C:/git/project_dir/ --filter *dir1\dir2\main.py* *dir1\dir2\file1.py* --list_files
python print_files.py --start_directory C:/git/project_dir/ --filter *dir1\v1\* *dir1\v2\* --extension .py --list_files
python print_files.py --start_directory C:/git/project_dir/ --filter *dir1\v1\* --extension .py --list_files
python print_files.py --start_directory C:/git/project_dir/ --filter *dir1\v1\* *dir1\v2\*  --extension .py --list_files
python print_files.py --start_directory C:/git/project_dir/ --filter *dir1/dir2/main.py* *dir1/dir2/file1.py* --write --list_files
python print_files.py --start_directory C:/git/project_dir/ --filter *dir1/dir2/main.py* *dir1/dir2/file1.py* --write
```