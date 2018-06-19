import requests
from bs4 import BeautifulSoup as bs

# combine above steps into a function
def ai_response(question):
    
    try:
        question = "_".join(question.split())
        url = 'http://www.answers.com/Q/' + question
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        ans = soup.find('div', {'class' : 'answer_text'}).text.strip().replace('\n', " ").replace('/', " ")
    except:
        ans = "I don't know. Please ask another question."
    
    return ans

