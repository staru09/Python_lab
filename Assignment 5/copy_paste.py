def copy_lowercase_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line[0].islower():
                outfile.write(line)

input_file = r'Z:\Desktop\Python_lab\Assignment 5\Demo.txt'
output_file = r'Z:\Desktop\Python_lab\Assignment 5\Demo2.txt'
copy_lowercase_lines(input_file, output_file)
print(f"Lines starting with lowercase letters copied to {output_file}.")
