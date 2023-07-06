# Conditionals
# Before
allowed_extensions = ['jpg', 'gif']
file_name = 'image.png'
extension = file_name.split('.').pop()
if extension not in allowed_extensions:
    print(f"File type not allowed: {extension}")


# After
allowed_extensions = ['jpg', 'gif']
file_name = 'image.png'
if (extension := file_name.split('.').pop()) not in allowed_extensions:
    print(f"File type not allowed: {extension}")


# While loops
# Before
with open("textfile.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

# After
with open("textfile.txt") as f:
    while line := f.readline():
        print(line)
