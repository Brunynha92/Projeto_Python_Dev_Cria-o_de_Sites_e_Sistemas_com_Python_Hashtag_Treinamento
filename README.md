# Python Dev: Criação de Sites e Sistemas com Python - Hashtag Treinamentos - Jornada Python (Set/25)

Projeto de criação de um Chatbot com IA, utilizado as IA's da OpenAi e Gemini

## Bibliotecas utilizadas:
* **streamlit**: para criação da aplicação web;
* **openai**: para acesso a API da OpenAI (Chat GPT);
* **google**: para acesso a API da GoogleI (Gemini)

## Comandos Utilizados:

* **st.session_state:** para pcriação da lista (lista de mensagem);
* **st.chat_input:** para inclusao de um campo de chat para o usuario;
* **st.chat_message:** para extrair quem digitou e o conteudo da mensagem;
* **.chat.completions.create:** Openai - para enviar a mensagem do usuario para IA e escolher o modelo da IA;
* **modelo.choices[0].message.content:** Openai - para extrair a resposta da IA;
* **OpenAI(api_key= ""):** Openai - para  chamar a IA incluindo a chave API;
* **genai.Client(api_key= ""):** Gemini - para  chamar a IA incluindo a chave API;
* **.models.generate_content:** Gemini - - para enviar a mensagem do usuario para IA e escolher o modelo da IA;
* **.text:** Gemini - para extrair a resposta da IA.



_Para um melhor manuseio incluso os valores utilizados dentro de variaveis_