import fitz # pymupdf
import os
from dotenv import load_dotenv
from google.generativeai import generativeai

load_dotenv()

GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
os.environ['GEMINI_API_KEY']=GEMINI_API_KEY

client=generativeai(api_key=GEMINI_API_KEY)

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file.
    
    Args:
       uploaded_file(str): The path to the PDF file.
        
    Returns:
        str: The extracted text.
    """

    text=""
    doc=fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        text+=page.get_text()
    return text

def ask_gemini(prompt, max_tokens=500):
    """Ask a question to the Gemini API.
    
    Args:
       prompt(str): The question to ask.
       max_tokens(int): The maximum number of tokens to generate.
        
    Returns:
        str: The response from the Gemini API.
    """
    response=client.chat.completions.create(
        model="gemini-2.5-pro",
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ],
        temperature=0.2,
        max_output_tokens=max_tokens
    )
    return response.choices[0].message.content
# ----------------------------------------------------------------------------------------------------------

