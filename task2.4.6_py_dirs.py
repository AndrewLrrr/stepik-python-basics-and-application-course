import os.path

for current_dir, dirs, files in os.walk('task2.4.6'):
    for file in files:
        if file.endswith('.py'):
            print(current_dir)
            break
