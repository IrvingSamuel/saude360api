from openai import OpenAI

client = OpenAI()

# Example HTML template
html_template = """
<div class="card" style="width: 18rem;">
    <div class="card-body">
        <h5 class="card-title">Diagnosis Result</h5>
        <p class="card-text">{diagnosis}</p>
    </div>
</div>
"""

# List of reference websites
reference_websites = [
    "https://epocanegocios.globo.com/inteligencia-artificial/noticia/2023/12/conheca-15-especialistas-em-inteligencia-artificial-empresarial-que-se-destacaram-em-2023.ghtml ",
    "https://abeso.org.br/conceitos/obesidade-e-sindrome-metabolica/",
    "https://bvsms.saude.gov.br/sindrome-metabolica/"
]

def process(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """Comporte-se como um sistema que vai retornar extritamente respostas html 
                 que serão introduzidas em um sistema de CRUD de pacientes para um usuário médico, com o intuito de ajudar a 
                 diagnosticar a sindrome metabólica (Doenças hereditárias), as informações vão 
                 ser passadas como texto, e o sistema vai retornar um 
                 texto com a resposta, contendo apenas: Considerações clinicas, Recomendações e conclusão.
                 Como um resultado final indique em porcentagem, o mais aproximada possível, o risco de se desenvolver cada tipo de sindrome metabólica no paciente 
                 O texto retornado vai vir como um html que vai ser introduzido dentro de um card.
                 Utilize os seguintes sites como 
                 fonte de consulta: """ + ', '.join(reference_websites).join("""
                , Template de uso estrito para resposta a ser usado:
                Considerações Clínicas
                O paciente --, -- anos, apresenta IMC ---- para sua altura e peso. Os sinais vitais estão ----, com glicose ----. É importante notar que o RCQ ----.

                Recomendações
                Recomenda-se que o paciente adote ----.

                Conclusão
                Com os dados apresentados, -- possui um -- risco de desenvolver diabetes tipo 2, e sua pressão arterial está --. Recomendo ---.

                Risco aproximado de desenvolver Síndrome Metabólica: --%
                """)
                 },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = completion.choices[0].message.content
        # Format the response into the HTML template
        html_response = html_template.format(diagnosis=text)
        return html_response
    except Exception as e:
        return str(e)

