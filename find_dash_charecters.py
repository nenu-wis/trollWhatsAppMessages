def add_newline_before_dash(input_file, output_file=None):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Add a newline before every "—" that doesn't already have one
    updated_content = content.replace('—', '\n—')

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f"Updated file saved as: {output_file}")
    else:
        with open(input_file, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f"Original file updated: {input_file}")
# Example usage
add_newline_before_dash('O_Banqueiro_Anarquista.js')  # Overwrites the original file
# Or
# add_newline_before_dash('yourfile.js', 'updated_file.js')  # Saves to a new file
