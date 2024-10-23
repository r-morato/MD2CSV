# Markdown Table to CSV Converter

This Python script converts a table in a Markdown file into a CSV file. It extracts the table from the Markdown format and saves it as a CSV using `pandas`.

## Features:
- Reads a table from a Markdown file.
- Converts the Markdown table into a CSV.
- Automatically handles file I/O and formatting.

## How to Use:
1. Place the Markdown file in the same directory as the script.
2. Update the file paths in the script or pass your own paths.
3. Run the script to generate a CSV file.

### Example:
```python
markdown_file_path = "my_markdown_file.md"
csv_file_path = "output.csv"
markdown_table_to_csv(markdown_file_path, csv_file_path)
