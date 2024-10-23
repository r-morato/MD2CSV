import pandas as pd
import re

def markdown_table_to_csv(markdown_file_path, csv_file_path):
    """Converts a Markdown table from a file to a CSV file."""
    try:
        # Read Markdown from file
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()

        # Extract the table from the Markdown text
        table_pattern = re.compile(r'\|.*\|\n\|.*\|\n((\|.*\|\n)+)')
        match = table_pattern.search(markdown_text)
        if not match:
            print("Error: No table found in the Markdown file.")
            return

        table_text = match.group(0)

        # Convert the Markdown table to a list of lists
        rows = table_text.strip().split('\n')
        table_data = [row.strip('|').split('|') for row in rows]

        # Create a DataFrame from the table data
        df = pd.DataFrame(table_data[2:], columns=table_data[0])  # Skip the separator row

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)
        print(f"Data successfully written to {csv_file_path}")

    except FileNotFoundError:
        print(f"Error: Markdown file not found at {markdown_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Make sure 'my_markdown_file.md' exists in the same directory
markdown_file_path = "my_markdown_file.md"
csv_file_path = "output.csv"

markdown_table_to_csv(markdown_file_path, csv_file_path)