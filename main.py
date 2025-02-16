import subprocess

input_file = "input.md"
output_file = "output.pdf"

subprocess.run(["pandoc", input_file, "-o", output_file])
print("Konversi selesai. File output:", output_file)
