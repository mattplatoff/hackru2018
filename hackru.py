from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
import re

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    #needs to be hosted and twillio webhook needs to be linked to this application

    body = request.values.get('Body', None)
    titlere = 'title:\s*\w+\s*'
    contentre = 'content:\s*\w+\s*'
    urlre = 'url:\s*\w+\s*'

    title = re.findall(titlere,body)
    contentre = re.findall(contentre,body)
    urlre= re.findall(urlre,body)


    print(body)
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)


def send_to_fakebox(url,title,content):
    r = requests.post('http://localhost:8080/fakebox/check',data={'url':url , 'content':content,'title':title})
    data = r.json()
    title_decision = data['title']['decision']
def parse_content_from_url(url):
    url=url
    content =


if __name__ == "__main__":
    app.run(debug=True)