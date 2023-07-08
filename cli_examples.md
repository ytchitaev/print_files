```cmd
python print_files.py --start_directory C:/git/your_project/ --filter file1.py file2.py file3.json --list_files
python print_files.py --start_directory C:/git/your_project/ --filter *archive\v3\file1.py* *archive\v3\file2.py* --list_files
python print_files.py --start_directory C:/git/your_project/ --filter *archive\v1\* *archive\v2\* --extension .py --list_files
python print_files.py --start_directory C:/git/your_project/ --filter *archive\v1\* --extension .py --list_files
python print_files.py --start_directory C:/git/your_project/ --filter *archive\v1\* *archive\v2\*  --extension .py --list_files
python print_files.py --start_directory C:/git/your_project/ --filter *archive/v3/file1.py* *archive/v3/file2.py* --write --list_files
python print_files.py --start_directory C:/git/your_project/ --filter *archive/v3/file1.py* *archive/v3/file2.py* --write
```