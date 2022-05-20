import pathlib

path = pathlib.Path("emails")
print(path.exists())
if not path.exists():
    path.mkdir()

path.rmdir()

path2 = pathlib.Path()
for file in path2.glob("*"):
    print(file)




