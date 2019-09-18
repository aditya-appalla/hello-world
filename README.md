<!DOCTYPE html>
<html>
<body>

<h1>Synopsis</h1>

<p>In this experimental endeavor, the customers are provided with an option to upload their module designs. The designs are then broken down into the components within it (Eg: Chip SMD resistor – 20ohm; Film capacitor - 50µF ). Each component is then grouped by the quantity and rating required in the design and the result is then fed into the search engine – Endeca. The results of the search engine comprises of products which are priced as per the customer contract and sent back to the customers for them to reveiew and order.
</p>

<h2>Design Steps</h2>
<ul>
  <li>Reading the customer input</li>
  <ul>
    <li>
      The customers have the option of uploading their design related queries as a .pdf or .doc or .docx document. We read their inputs and convert it to plain text using two python modules – pdfminer and doc2text.
    </li>
  </ul>
  <li>Install pfdminer</li>
  <li>Extract text from PDF</li>
    <ul>
      <li>Iterate over all pages of the .pdf document.</li>
      <li>Create a resource manager.</li>
      <li>Create a file handle.</li>
      <li>Create a text converter object.</li>
      <li>Create a page interpreter.</li>
      <li>Process current page.</li>
      <li>Extract text</li>
      <li>Close the file handle</li>
    </ul>  
  <li>Extract text from .doc or .docx</li>
</ul>  


</body>
</html>




Reading the customer details
•	Extract the customer’s first and last name leveraging spaCy – an industrial strength natural language processing module by leveraging ‘Entity Recognition’.
o	Install spaCy
o	Download the pre-trained module – en_core_web_sm.
o	Perform a rule based matching
	Load the pre-trained module = en_core_web_sm
	Initialize a matcher with vocab
	Extract the first name and the last name (deemed proper nouns – PROPN)
	Return the matched names as span
•	Extract the customer phone number (leveraging regular expression)
•	Extract the customer email address (leveraging a regex which reads an alphanumeric string immediately followed by an ‘@’ which is then followed by a string and then a ‘.’ and finally another string. Eg: "([^@|\s]+@[^@]+\.[^@|\s]+)
•	Extracting the design inputs
o	A pre-defined data is already provided by the business teams for comparison (a .csv file)
o	Leverage tokenization – Sentence tokenization and Word tokenization.
	Install pandas.
	Load the pre-trained spaCy module – en_core_web_sm.
	Remove the stop words.
	Use word tokenization.
	Read the business provided .csv file carrying the pre-defined data and extract values.
	Check for one-grams, bi-grams and tri-grams.
	Return matches.
•	Extracting further inputs using nltk
o	Install nltk
o	Import spaCy
o	Load the pre-trained en_core_web_sm module
o	Remove all the stop words
o	Create a pre-defined set of data
o	Leverage sentence tokenizer
o	Extract data
o	Remove all special symbols
o	Return the data.
•	Pass the extracted details as search keywords into the search engine.
•	Retrieve results off the search engine.
•	Package the results and send it back to the customer for them to convert this into a purchase.
