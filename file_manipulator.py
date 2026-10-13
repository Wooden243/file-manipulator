import sys

command = sys.argv[1]
input_path = sys.argv[2]

if command == "reverse":
    output_path = sys.argv[3]

    with open(input_path, "r") as file:
        content = file.read()

    reversed_content = content[::-1]

    with open(output_path, "w") as file:
        file.write(reversed_content)


elif command == "copy":
    output_path = sys.argv[3]

    with open(input_path, "r") as file:
        content = file.read()

    with open(output_path, "w") as file:
        file.write(content)


elif command == "duplicate-contents":
    output_path = sys.argv[4]
    times = int(output_path)

    with open(input_path, "r") as file:
        content = file.read()

    with open(input_path, "a") as file:
        file.write(content * times)


elif command == "replace-string":
    old_string = sys.argv[3]
    new_string = sys.argv[4]

    with open(input_path, "r") as file:
        content = file.read()

    replaced_content = content.replace(old_string, new_string)

    with open(input_path, "w") as file:
        file.write(replaced_content)
