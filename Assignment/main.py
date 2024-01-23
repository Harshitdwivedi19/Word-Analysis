from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pdfplumber


def read_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""

        for page in pdf.pages:
            text += page.extract_text()

    return text


# example usage
pdf_path = r"D:\Users\Dell\Downloads\Assignment_int.pdf"
pdf_text = read_pdf(pdf_path)

# sample preprocessing


def preprocess_text(text):
    # Remove special characters and extra whitespaces
    processed_text = ' '.join(text.split())

    return processed_text


# example usage
processed_text = preprocess_text(pdf_text)

# tokenization
tokens = processed_text.split()

# count the number of words
word_count = len(tokens)

# display some basic information
print(f"Total Words: {word_count}")


# data exploration - Word Cloud
wordcloud = WordCloud(width=800, height=400,
                      background_color='white').generate(processed_text)

# Display the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Document your findings
analysis_report = """
Analysis Report:

1. Total Words: {}
2. Word Cloud: (see attached visualization)

Summary:
key observations and insights go here.
Total Word Count:

The script calculates and displays the total number of words in the PDF document. This quantitative measure provides a basic understanding of the document's length and complexity.
Word Cloud Visualization:

The Word Cloud generated from the most frequently occurring words in the text offers qualitative insights.
Prominent words in the Word Cloud are larger, indicating higher frequency. Users can visually identify key terms or topics that stand out.
Text Preprocessing:

The script preprocesses the text by removing special characters and extra whitespaces. This step ensures a cleaner and more standardized representation of the text for analysis.
These insights are fundamental and serve as a starting point for more advanced analyses. While the provided script does not delve into specific content-related analyses (e.g., sentiment analysis, topic modeling), it lays the groundwork by providing an overview of the text's structure and frequently occurring terms.

For a more in-depth understanding of the document's content, additional analyses tailored to specific goals or questions would be necessary.
"""

print(analysis_report.format(word_count))


# Save results to a text file
with open("analysis_results.txt", "w") as file:
    file.write(analysis_report)
