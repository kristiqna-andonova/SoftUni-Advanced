from string import punctuation

with open("input_file.txt") as input_file, open("output_file.txt", "w") as output_file:
    result = []
    for row, line in enumerate(input_file):
        chars = 0
        punctuation_marks = 0
        for ch in line:
            if ch.isalpha():
                chars += 1
            elif ch in punctuation:
                punctuation_marks += 1
        result.append(f"Line {row + 1}: {line.strip()} ({chars})({punctuation_marks})")
    output_file.write("\n".join(result))
