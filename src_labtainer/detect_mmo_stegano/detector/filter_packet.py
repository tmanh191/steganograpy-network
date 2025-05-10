import ast

def extract_ascii_sequence(input_file, output_file):
    numbers = []
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            try:
                # Sử dụng ast.literal_eval để parse byte literal an toàn
                raw = ast.literal_eval(line)
                if isinstance(raw, bytes) and len(raw) >= 1:
                    ascii_val = raw[0]
                    numbers.append(str(ascii_val))
            except Exception as e:
                print(f"Lỗi dòng: {line} => {e}")

    with open(output_file, "w") as f:
        f.write(",".join(numbers))

extract_ascii_sequence("result.txt", "sequence.txt")
