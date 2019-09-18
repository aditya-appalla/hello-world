<p><strong>Synopsis</strong></p>
<p>In this experimental endeavor, the customers are provided with an option to upload their module designs. The designs are then broken down into the components within it (Eg: Chip SMD resistor &ndash; 20ohm; Film capacitor - <a href="https://uk.farnell.com/c/passive-components/capacitors/film-capacitors/motor-run-motor-start-capacitors?capacitance=50uf">50&micro;F</a> ). Each component is then grouped by the quantity and rating required in the design and the result is then fed into the search engine &ndash; Endeca. The results of the search engine comprises of products which are priced as per the customer contract and sent back to the customers for them to reveiew and order.</p>
<p><strong><u>&nbsp;</u></strong></p>
<p><strong><u>Design Steps</u></strong></p>
<p><strong>Reading the customer input</strong></p>
<p>The customers have the option of uploading their design related queries as a .pdf or .doc or .docx document. We read their inputs and convert it to plain text using two python modules &ndash; pdfminer and doc2text.</p>
<ul>
<li>Install pfdminer:</li>
<li>Install doc2text:</li>
<li>Extract text from PDF
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
</li>
<li>Extract text from .doc or .docx</li>
</ul>
<p><strong>&nbsp;</strong></p>
<p><strong>Reading the customer details</strong></p>
<ul>
<li>Extract the customer&rsquo;s first and last name leveraging spaCy &ndash; an industrial strength natural language processing module by leveraging &lsquo;Entity Recognition&rsquo;.
<ul>
<li>Install spaCy</li>
<li>Download the pre-trained module &ndash; en_core_web_sm.</li>
<li>Perform a rule based matching
<ul>
<li>Load the pre-trained module = en_core_web_sm</li>
<li>Initialize a matcher with vocab</li>
<li>Extract the first name and the last name (deemed proper nouns &ndash; PROPN)</li>
<li>Return the matched names as span</li>
</ul>
</li>
<li>Extract the customer phone number (leveraging regular expression)</li>
<li>Extract the customer email address (leveraging a regex which reads an alphanumeric string immediately followed by an &lsquo;@&rsquo; which is then followed by a string and then a &lsquo;.&rsquo; and finally another string. Eg: "([^@|\s]<a href="mailto:+@[%5e@]+\.%5b%5e@|\s">+@[^@]+\.[^@|\s</a>]+)</li>
<li>Extracting the design inputs
<ul>
<li>A pre-defined data is already provided by the business teams for comparison (a .csv file)</li>
<li>Leverage tokenization &ndash; Sentence tokenization and Word tokenization.
<ul>
<li>Install pandas.</li>
<li>Load the pre-trained spaCy module &ndash; en_core_web_sm.</li>
<li>Remove the stop words.</li>
<li>Use word tokenization.</li>
<li>Read the business provided .csv file carrying the pre-defined data and extract values.</li>
<li>Check for one-grams, bi-grams and tri-grams.</li>
<li>Return matches.</li>
</ul>
</li>
<li>Extracting further inputs using nltk
<ul>
<li>Install nltk</li>
<li>Import spaCy</li>
<li>Load the pre-trained en_core_web_sm module</li>
<li>Remove all the stop words</li>
<li>Create a pre-defined set of data</li>
<li>Leverage sentence tokenizer</li>
<li>Extract data</li>
<li>Remove all special symbols</li>
<li>Return the data.</li>
</ul>
</li>
<li>Pass the extracted details as search keywords into the search engine.</li>
<li>Retrieve results off the search engine.</li>
<li>Package the results and send it back to the customer for them to convert this into a purchase.</li>
</ul>
</li>
</ul>
</li>
</ul>
