""" Python script to extract archived files with 
    formats like`tar` and `zip`. 
    Requring shell commands to be work.
    author: Saeed Gholami
    date: 2/28/2025
"""
import subprocess
import sys



if len(sys.argv) <= 1:
    print("No archive file specified! Abroting...")
    sys.exit(1)

filename = sys.argv[1]


if filename.endswith(".zip"):
    fname = filename.replace(".zip", "")
    subprocess.run(["unzip", "-d", fname, filename])
    print(f"File {filename} extracted.")

if filename.endswith(".tar"):
    fname = filename.replace(".tar", "")
    subprocess.run(["tar", "-xf", filename, "-C", fname])
    print(f"File {filename} extracted.")






