import io
import os
import re
import nltk
import spacy
import pandas as pd
import docx2txt
import subprocess

from datetime import datetime
from dateutil import relativedelta
from spacy.matcher import Matcher
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFSyntaxError
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords



# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

def text_extractor(pdf_path):
    with open(pdf_path, 'rb') as filehandler:
        # iterate over all pages of PDF document
        for page in PDFPage.get_pages(filehandler, caching=True, check_extractable=True):

            # create resoure manager
            resource_manager = PDFResourceManager()
            
            # file handle
            pseudo_handle = io.StringIO()
            
            # create text converter
            converter = TextConverter(
                                resource_manager, 
                                pseudo_handle, 
                                codec='utf-8', 
                                laparams=LAParams()
                        )

            # create a page interpreter
            page_reader = PDFPageInterpreter(
                                resource_manager, 
                                converter
                            )

            # process current page
            page_reader.process_page(page)
            
            # extract text
            text = pseudo_handle.getvalue()
            yield text

            converter.close()
            pseudo_handle.close()

print("EMAIL ADDRESSES")
print("----------------------------")

# extracting email address from the basket pdf
# enter the actual file path of the pdf below
for page in text_extractor("XXX"):
   email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", page)
   if email:
        print(email[0].split()[0].strip(';'))
print("----------------------------")

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)
nlp_text = nlp(page)
    
# first name and last names are proper nouns
pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
matcher.add('NAME', None, pattern)
matches = matcher(nlp_text)

print("PROPER NOUNS")
print("----------------------------")

for match_id, start, end in matches:
    span = nlp_text[start:end]
    print(span.text)
print("----------------------------")

nlp = spacy.load('en_core_web_sm')
#noun_chunks = nlp.noun_chunks

doc = nlp(page)    
for chunk in doc.noun_chunks:       
   #print(chunk.text)

    # removing stop words and leverage word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    # enter the actual file path of the .csv below
    data = pd.read_csv("XXX") 
  
    # extract values
    skills = list(data.columns.values)
    skillset = []

    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)

    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in doc.noun_chunks:
        token = token.text.lower().strip()
        #print(token)
        if token in skills:
            skillset.append(token)

print("INPUT MATCHES")
print(skillset)
            #return [i.capitalize() for i in set([i.lower() for i in skillset])]
            #print(i.capitalize() for i in set([i.lower() for i in skillset]))

print("----------------------------")
