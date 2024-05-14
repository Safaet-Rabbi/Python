import re
from PyPDF2 import PdfReader

def extract_text_from_file(file):
    if file.endswith('.pdf'):
        return extract_text_from_pdf(file)
    else:
        with open(file, 'r') as f:
            return f.read()

def extract_text_from_pdf(file):
    text = ""
    with open(file, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def tokenize_into_sentences(text):
    # Define a regex pattern to split text into sentences
    sentence_endings = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s')

    # Use the regex pattern to split text into sentences
    sentences = sentence_endings.split(text)
    return sentences

def check_plagiarism(files):
    similarities = []
    for i, file1 in enumerate(files):
        for file2 in files[i+1:]:
            text1 = extract_text_from_file(file1).lower()  # Convert to lowercase
            text2 = extract_text_from_file(file2).lower()  # Convert to lowercase

            similarity_percentage, similar_sentences = calculate_similarity_and_similar_sentences(text1, text2)

            similarities.append((file1, file2, similarity_percentage, similar_sentences))

    for similarity in similarities:
        file1, file2, similarity_percentage, similar_sentences = similarity
        print(f"Plagiarism between {file1} and {file2}: {similarity_percentage:.2f}%")
        print("Similar sentences:")
        for sentence in similar_sentences:
            print(sentence)

def calculate_similarity_and_similar_sentences(text1, text2):
    sentences1 = set(tokenize_into_sentences(text1))
    sentences2 = set(tokenize_into_sentences(text2))
    similar_sentences = sentences1.intersection(sentences2)
    similarity_score = len(similar_sentences) /  len(sentences2)
    return similarity_score * 100, similar_sentences

files = []
while True:
    file_path = input("Enter path to file (enter 'end' when finished): ")
    if file_path.lower() == 'end':
        break
    files.append(file_path)

if len(files) < 2:
    print("At least two files are required for comparison.")
else:
    check_plagiarism(files)
