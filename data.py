# question data
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

question = requests.get(url="https://opentdb.com/api.php", params=parameters)
question.raise_for_status()
question_data = question.json()["results"]
