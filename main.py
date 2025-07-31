import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing Function
def preprocess(text):
    # Lowercasing
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming
    ps = PorterStemmer()
    tokens = [ps.stem(word) for word in tokens]
    
    return " ".join(tokens)

# Example usage
feedback = "I am so happy with this product!"
preprocessed_feedback = preprocess(feedback)
print(preprocessed_feedback)
