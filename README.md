# Text Converter for Notion

This Python program is designed to transform text into Markdown format. This program allows you to convert numbered titles, italic/bold text, and bullet lists into their Markdown equivalents, making it easier to create documents in this format.

## Features

- Converts numbered titles to Markdown headers (`#`, `##`, `###`)
- Converts bullet lists from hyphen (`-`) to Markdown list format (`*`)
- Cleans up some trailing periods and whitespaces
- Easily extendable for future text conversion needs

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Clone this repository or download the script.

## Usage

1. Add the text you want to convert into the file `data/input.txt`.
2. Run the main script main.py.
3. The converted output text will be saved in `data/output.txt`.

### Input Format

This text should contain structured text formatted with numbered titles and bullet lists. For example:

```
1.- Introduction
2.- Software Overview

- Item one
- Item two
3.- Hardware Components
3.1.- Motherboard
3.2.- CPU
4.- Conclusion
This is a *bold* text conversion.
**Italic** for emphasis.
```

### Output

The output will format the titles, italic/bold text, and lists appropriately for Notion. For example, the input above would be converted to:

```
# 1. Introduction
# 2. Software Overview
* Item one
* Item two
# 3. Hardware Components
## 3.1. Motherboard
## 3.2. CPU
# 4. Conclusion
This is a _bold_ text conversion
__Italic__ for emphasis
```

## Code Structure

The program consists of several classes:
- **TextConverter**: An abstract base class that defines methods for cleaning and processing lines of text. It requires all subclasses to implement the process_line method.
- **MultiConverter**: A class that groups multiple converters and applies their functionality in sequence to each line of text.
- **NumberedTitleConverter**: Converts numbered titles into Markdown headers.
- **ItalicBoldConverter**: Transforms italic and bold text markers into their corresponding Markdown format.
- **BulletListConverter**: Converts bullet points into Markdown format.

## Contributions

Contributions are welcome! If you would like to contribute, please open an issue or submit a pull request.
