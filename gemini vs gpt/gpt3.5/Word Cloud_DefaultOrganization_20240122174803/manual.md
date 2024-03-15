# Word Cloud Generator User Manual

## Introduction
The Word Cloud Generator is a Python program that allows users to generate word clouds from input text. This program uses the wordcloud library in combination with matplotlib to create visualizations of word frequencies in the input text. The word cloud represents the frequency of words in the input text, with more frequent words appearing larger in the visualization.

## Installation
To use the Word Cloud Generator, you need to have Python installed on your system. You can download and install Python from the official website: https://www.python.org/downloads/

Once Python is installed, you can install the required dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

This will install the wordcloud and matplotlib libraries.

## Usage
To run the Word Cloud Generator, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the following command:

```
python main.py
```

4. A window will appear with a text entry field and a "Generate Word Cloud" button.
5. Enter the desired text in the text entry field.
6. Click the "Generate Word Cloud" button.
7. A new window will open displaying the word cloud visualization.

## Customization
The Word Cloud Generator allows you to customize the appearance of the word cloud. You can modify the following properties:

- Color scheme: The default color scheme is used, but you can modify it by editing the code in the `generate_word_cloud` method of the `WordCloudGenerator` class.
- Size: The size of the word cloud visualization can be adjusted by resizing the window that displays the word cloud.
- Font: The default font is used, but you can change it by modifying the code in the `generate_word_cloud` method of the `WordCloudGenerator` class.

## Example
Here is an example of how to use the Word Cloud Generator:

1. Run the program as described in the "Usage" section.
2. Enter the following text in the text entry field:

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl ac ultrices aliquet, velit odio lacinia nunc, id tincidunt tortor urna id justo. Sed euismod, nisl ac ultrices aliquet, velit odio lacinia nunc, id tincidunt tortor urna id justo.
```

3. Click the "Generate Word Cloud" button.
4. A new window will open displaying the word cloud visualization.

## Conclusion
The Word Cloud Generator is a user-friendly Python program that allows you to generate word clouds from input text. It provides a simple interface for entering text and customizing the appearance of the word cloud. By following the instructions in this user manual, you can easily create meaningful word cloud visualizations.