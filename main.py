import sys

if len(sys.argv) == 1:
    print("Hello world!")

for name_index in range(1, len(sys.argv)):
    print(f"Hello {sys.argv[name_index]}!")