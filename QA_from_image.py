# Importing the required libraries
import pytesseract  
from transformers import pipeline  
from PIL import Image

def read_image_content(image_path) -> str:
    '''
    Reads the content of an image and returns it as a string using OCR (Optical Character Recognition).

    Parameters:
    image_path (str): The path to the image file to be read.

    Returns:
    str: The text content extracted from the image.
    '''
    # Set the Tesseract command path
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    
    # Open the image file using PIL
    image = Image.open(image_path)
    
    # Use Tesseract to convert the image to a string
    return pytesseract.image_to_string(image)

def QA(context) -> None:
    '''
    Performs a question-answering task using a given context.

    Parameters:
    context (str): The context text used to answer questions.

    Returns:
    None
    '''
    # Initialize the question-answering pipeline
    qa = pipeline("question-answering")
    
    # Continuously ask for user input and provide answers based on the context
    while ask := input('ask something:'):
        # Get the answer from the pipeline and print it
        print('\n')
        print(qa(question=ask, context=context)['answer'])
        # Print a separator for better readability
        print(f'\n{"*"*100}')

# Execute the QA function with the text extracted from the image
QA(read_image_content(input('Enter image path: ')))
