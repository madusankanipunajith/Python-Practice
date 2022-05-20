from pathlib import Path

# return the current directory
path = Path("ecommerce")
print(path)
print(path.exists())


for file in path.glob("*.py"):
    print(file)


