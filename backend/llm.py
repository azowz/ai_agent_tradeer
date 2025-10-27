from openai import OpenAI

class LLM:
    def __init__(self):
        self. client = OpenAI(api_key='OPENAI_API_KEY')

    def give_response(self, prompt):

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",  # You can also use "gpt-4o", "gpt-4-turbo", etc.
            messages=[
                {"role": "system", "content": "You are a helpful assistant. who is a top Trader in Stocks."},
                {"role": "user",
                 "content": f"Here is the json file containing all the informations along with the technical "
                            f"calculations. give me predictions for next 2 weeks: {prompt}"}
            ]
        )
        return response.choices[0].message.content