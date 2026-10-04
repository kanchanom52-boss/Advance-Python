import itertools

def count_lines(file):
    with open(file, "r") as f:
        return sum(1 for _ in f)

def extract_first_lines(file, n=2):
    with open(file, "r") as f:
        # Using islice stops safely if the file has fewer than n lines
        return list(itertools.islice(f, n))

def write_lines(file, lines):
    with open(file, "w") as f:
        f.writelines(lines)

input_file = "input.txt"
output_file = "output_first_two_lines.txt"

# Create sample file
with open(input_file, "w") as f:
    f.write("Monday: Team stand-up at 9:00 AM\n")
    f.write("Tuesday: Client review meeting\n")
    f.write("Wednesday: Code review session\n")

# Process file
print("Total lines:", count_lines(input_file))

lines = extract_first_lines(input_file)
print("First two lines:")
for line in lines:
    print(line.strip())

write_lines(output_file, lines)
print("Written to:", output_file)
