# GenAI-Project-E-commerce-chatbot (project using LLama3.3 and GROQ)

This is POC of an intelligent chatbot tailored for an e-commerce platform, enabling seamless user interactions by accurately identifying the intent behind user queries. It leverages real-time access to the platform's database, allowing it to provide precise and up-to-date responses.

This project combines LLM Fine-Tuning, Retrieval-Augmented Generation (RAG), and semantic intent classification to deliver fast, accurate, and human-like responses.

📂 Folder Structure:

- app/faq.py → FAQ retrieval & RAG pipeline
- app/sql.py → SQL generation & execution
- app/route.py → Semantic intent routing
- app/small_talk.py → Casual conversation handling
- app/main.py → Streamlit chatbot interface

📊 This chatbot currently supports two intents:

- **faq**: Triggered when users ask questions related to the platform's policies or general information. eg. Is online payment available?
- **sql**: Activated when users request product listings or information based on real-time database queries. eg. Show me all nike shoes below Rs. 3000.
- **Small Talk Mode**: Directly handled by the LLM for a human-like response

<img width="1871" height="860" alt="Image" src="https://github.com/user-attachments/assets/9d3e75f4-997e-4c92-8d9d-456d964e8946" />

## Architecture

<img width="2320" height="856" alt="Image" src="https://github.com/user-attachments/assets/dad06ad5-d05d-4b91-ad32-3c6bbb5b3d95" />

## 📈 Future Improvements  

- [ ] Product recommendation system  
- [ ] Voice-enabled search  
- [ ] Multi-language support  
- [ ] Integration with payment & order APIs  

### Set-up & Execution

1. Run the following command to install all dependencies. 

    ```bash
    pip install -r app/requirements.txt
    ```

1. Inside app folder, create a .env file with your GROQ credentials as follows:
    ```text
    GROQ_MODEL=<Add the model name, e.g. llama-3.3-70b-versatile>
    GROQ_API_KEY=<Add your groq api key here>
    ```

1. Run the streamlit app by running the following command.

    ```bash
    streamlit run app/main.py
    ```

---
