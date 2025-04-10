from openai import OpenAI

client = OpenAI()

# exemplo html para resposta
html_template = """
<div class="card" style="width: 18rem;">
    <div class="card-body">
        <h5 class="card-title">Diagnosis Result</h5>
        <p class="card-text">{diagnosis}</p>
    </div>
</div>
"""
html_template = "{diagnosis}"

# Lista de sites para referência textual
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
                {"role": "system", "content": """Comporte-se como um sistema que vai retornar extritamente um json com indices prefefinidos,
                    você vai receber um texto com informações sobre um paciente que serão introduzidas em um sistema de CRUD de pacientes para um usuário médico, com o intuito de ajudar a 
                    diagnosticar a sindrome metabólica (Doenças hereditárias), as informações vão 
                    ser passadas como texto, e o sistema vai retornar um 
                    json com a resposta com os valores dos indices também sendo texto, contendo apenas as chaves: consideracoes_clinicas, recomendacoes_medicas, conclusao_do_caso e risco_de_sm (risco de sindrome metabólica em %).
                    para o risco de desenvolver sindrome metabólica, indique em porcentagem, o mais aproximada possível.
                    Utilize os seguintes sites como 
                    fonte de consulta: """ + ', '.join(reference_websites).join("""
                    , Template exemplificativo de uso estrito para resposta a ser usado:
                    consideracoes_clinicas:
                    O paciente --, -- anos, apresenta IMC ---- para sua altura e peso. Os sinais vitais estão ----, com glicose ----. É importante notar que o RCQ ----.

                    recomendacoes_medicas:
                    Recomenda-se que o paciente adote ----.

                    conclusao_do_caso:
                    Com os dados apresentados, -- possui um -- risco de desenvolver diabetes tipo 2, e sua pressão arterial está --. Recomendo ---.
                                                                                
                    risco_de_sm:
                    --%
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

