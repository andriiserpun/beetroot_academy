import sys

print("sys.path:")
for path in sys.path:
    print(path)
new_path = "/my/custom/path"
sys.path.append(new_path)

print("sys.path:")
for path in sys.path:
    print(path)