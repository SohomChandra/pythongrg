import re
import requests
import spacy
import logging

# Initialize spaCy model
nlp = spacy.load("en_core_web_sm")

# Configure logging
logging.basicConfig(filename='chatbot.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# NLP module
class NLP:
    def tokenize(self, text):
        doc = nlp(text)
        return [token.text for token in doc]

    def clean(self, tokens):
        return [token.lower() for token in tokens if token.is_alpha]

    def pos_tag(self, tokens):
        doc = nlp(' '.join(tokens))
        return [(token.text, token.pos_) for token in doc]

    def ner_tag(self, tokens):
        doc = nlp(' '.join(tokens))
        return [(ent.text, ent.label_) for ent in doc.ents]

    def parse_sentence(self, tokens):
        return ' '.join(tokens)

nlp_model = NLP()

# Database module
class Database:
    def query_database(self, parsed_sentence):
        responses = []
        responses.append(self.query_ayush(parsed_sentence))
        responses.append(self.query_researchgate(parsed_sentence))
        responses.append(self.query_bastyr(parsed_sentence))
        responses.append(self.query_ncbi_1(parsed_sentence))
        responses.append(self.query_nlam(parsed_sentence))
        responses.append(self.query_ncbi_2(parsed_sentence))
        responses.append(self.query_grin(parsed_sentence))
        responses.append(self.query_global_wellness(parsed_sentence))
        responses.append(self.query_nccih(parsed_sentence))
        responses.append(self.query_ayurveda_nama(parsed_sentence))
        responses.append(self.query_ayurveda_healthcare(parsed_sentence))

        # Filter out None responses
        responses = [response for response in responses if response]
        
        # Combine or select the best response
        if responses:
            return ' '.join(responses)
        else:
            return 'Sorry, I am not able to find information for your query.'

    def query_ayush(self, query):
        url = 'https://ayushportal.nic.in/api/query'
        return self.query_api(url, query)

    def query_researchgate(self, query):
        url = 'https://www.researchgate.net/api/query'
        return self.query_api(url, query)

    def query_bastyr(self, query):
        # Placeholder for actual implementation
        url = 'https://bastyr.libguides.com/api/query'
        return self.query_api(url, query)

    def query_ncbi_1(self, query):
        url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4895749/'
        return self.query_api(url, query)

    def query_nlam(self, query):
        url = 'https://nlam.in/api/query'
        return self.query_api(url, query)

    def query_ncbi_2(self, query):
        url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3371566/'
        return self.query_api(url, query)

    def query_grin(self, query):
        url = 'https://www.grin.com/api/query'
        return self.query_api(url, query)

    def query_global_wellness(self, query):
        url = 'https://globalwellnessinstitute.org/api/query'
        return self.query_api(url, query)

    def query_nccih(self, query):
        url = 'https://www.nccih.nih.gov/api/query'
        return self.query_api(url, query)

    def query_ayurveda_nama(self, query):
        url = 'https://www.ayurvedanama.org/api/query'
        return self.query_api(url, query)

    def query_ayurveda_healthcare(self, query):
        url = 'https://ayurvedahealthcare.info/api/query'
        return self.query_api(url, query)

    def query_api(self, url, query):
        try:
            params = {'search': query}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get('result', 'No information found.')
            else:
                return f'Error accessing {url}'
        except Exception as e:
            return f'Error: {e}'

database = Database()

# Machine Learning module
class MachineLearning:
    def generate_response(self, analysis):
        return f"Based on my knowledge of Ayurveda: {analysis}"

machine_learning = MachineLearning()

def start_chatbot():
    print("Welcome to the Ayurvedic medical assistant chatbot!")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Thank you for using the Ayurvedic medical assistant chatbot. Take care!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

def generate_response(user_input):
    try:
        # Natural language processing and text analysis
        tokens = nlp_model.tokenize(user_input)
        cleaned_tokens = nlp_model.clean(tokens)
        pos_tags = nlp_model.pos_tag(cleaned_tokens)
        ner_tags = nlp_model.ner_tag(cleaned_tokens)
        parsed_sentence = nlp_model.parse_sentence(cleaned_tokens)

        # Database query and analysis
        analysis = database.query_database(parsed_sentence)

        # Machine learning and response generation
        response = machine_learning.generate_response(analysis)

        logging.info(f"User input: {user_input}, Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error: {e}")
        return "Sorry, there was an error processing your request."

if __name__ == "__main__":
    start_chatbot()
