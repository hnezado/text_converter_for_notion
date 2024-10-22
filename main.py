from typing import List


class TextConverter:
    @staticmethod
    def clean_line(line: str) -> str:
        """
        Cleans the input line by stripping whitespace and handling specific characters.

        Parameters:
        line (str): The input line of text.

        Returns:
        str: The cleaned line with leading and trailing whitespace removed.
        """
        return line.strip()  # Remove whitespaces

    def process_line(self, line: str) -> None:
        pass


class MultiConverter:
    def __init__(self, converters_list: List[TextConverter]):
        """
        Initializes the MultiConverter with a list of converters.

        Parameters:
        converters (List[TextConverter]): A list of converter instances.
        """
        self.converters = converters_list

    def process_line(self, line: str) -> str:
        """
        Processes a line of text using all converters.

        Parameters:
        line (str): The input line of text.

        Returns:
        str: The processed line after applying all converters.
        """
        for converter in self.converters:
            line = converter.process_line(line)
        return line

    def process_file(self, input_path: str, output_path: str) -> None:
        """
        Processes the input file and writes the output to the specified output file.

        Parameters:
        input_path (str): The path to the input file.
        output_path (str): The path to the output file.
        """
        with open(input_path, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        processed_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:  # Only process non-empty lines
                processed_line = self.process_line(stripped_line)
                processed_lines.append(processed_line)

        self.write_output(processed_lines, output_path)

    @staticmethod
    def write_output(processed_lines: List[str], output_path: str) -> None:
        """
        Writes processed lines to the output file.

        Parameters:
        processed_lines (List[str]): The list of processed lines.
        output_path (str): The path to the output file.
        """
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(processed_lines) + "\n")


class NumberedTitleConverter(TextConverter):
    def __init__(self, scope: int = 1):
        """
        Initializes the NumberedTitleConverter with a given scope level.

        Parameters:
        scope (int): The starting level for titles (default is 1).
        """
        self.scope = scope

    def process_line(self, line: str) -> str:
        """
        Converts numbered titles into Markdown headers based on the scope.

        Parameters:
        line (str): The input line of text.

        Returns:
        str: The formatted line as a Markdown header with `#` depending on the level and scope.
             Limits the header level to a maximum of 3. If the calculated level exceeds 3, no header is added.
        """
        line = self.clean_line(line).replace(".-", ".")  # Clean line and remove a specific pattern
        parts = line.split(".")
        numeric_parts = [part for part in parts if part.isdigit()]
        level = len(numeric_parts)  # Count numeric parts

        # Calculate header level based on scope
        header_level = level + self.scope - 1

        # Limit the number of '#' to a maximum of 3, else return line without a header
        if 1 <= header_level <= 3:
            return f"{'#' * header_level} {line.rstrip('.')}"
        else:
            return line  # If level exceeds 3, return the original line without a header


class ItalicBoldConverter(TextConverter):
    def process_line(self, line: str) -> str:
        """
        Converts specific markers for italic and bold text.

        Parameters:
        line (str): The input line of text.

        Returns:
        str: The formatted line with Markdown replacements for
             italic and bold text.

        Process:
        1. Cleans the line using the `clean_line` method.
        2. Replaces bold markers (`**`) with underscores (`__`).
        3. Replaces italic markers (`*`) with single underscores (`_`).
        """
        line = self.clean_line(line)  # Clean line before processing
        # Convert specific markers for italic and bold
        return line.replace("**", "__").replace("*", "_")


class BulletListConverter(TextConverter):
    def process_line(self, line: str) -> str:
        """
        Converts bullet points into Markdown list format.

        Parameters:
        line (str): The input line of text.

        Returns:
        str: The formatted line as a Markdown bullet point if it starts with a dash,
             otherwise returns the original line.

        Process:
        1. Cleans the line using the `clean_line` method.
        2. If the line starts with a dash ("-"), it converts it to a Markdown bullet
           point format by replacing the dash with an asterisk ("*").
        """
        line = self.clean_line(line)
        if line.startswith("-"):
            return f"* {line[1:].strip()}"  # Convert bullet point to Markdown format
        return line


# Define paths for input and output files
input_file = "data/input.txt"
output_file = "data/output.txt"

# Define the starting scope level for titles
init_scope = 2

# Create instances of the converters
converters = [NumberedTitleConverter(scope=init_scope), ItalicBoldConverter(), BulletListConverter()]

# Create a MultiConverter instance to apply all converters
multi_converter = MultiConverter(converters)

# Process the input file
multi_converter.process_file(input_file, output_file)

print("Conversion completed successfully!")
