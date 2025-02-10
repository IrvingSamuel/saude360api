from openai import OpenAI

client = OpenAI()

def process(prompt):
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Comporte-se como um sistema que vai retornar respostas html para um usuário médico, com o intuito de ajudar a diagnosticar doenças hereditárias, as informações vão ser passadas como texto, e o sistema vai retornar um texto com a resposta."},
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            text = completion.choices[0].message.content
            return text
        except Exception as e:
            return str(e)
        
