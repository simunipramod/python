import os

os.chdir(r'C:\Users\pramo\OneDrive\Desktop\test')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    new_name = file_name.replace('.', '_')
    suffix = '.sql'
    os.rename(f, new_name+file_ext)
