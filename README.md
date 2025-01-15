# **AI-Powered Knowledge Management: RAG Chatbot for 24/7 Information Efficiency**

Welcome to the **AI-Powered Knowledge Management: RAG Chatbot for 24/7 Information Efficiency** repository. This project implements a Retrieval-Augmented Generation (RAG) chatbot designed to provide information efficiently and accurately around the clock.

For detailed background and explanations, please refer to the [Medium article](#).

---

## Repository Structure
Below is an explanation of the files in this repository:

### 1. **`.env`**
   - **Purpose**: Stores sensitive environment variables such as API keys or database credentials. This file is excluded from version control to ensure security.
   - **Usage**: Update this file with the required API keys and configurations before running the application.

### 2. **`README.md`**
   - **Purpose**: Provides an overview of the project, including setup instructions and repository details.
   - **Usage**: You are reading it now. Use this document as a guide for setup and usage.

### 3. **`init_db.py`**
   - **Purpose**: A script to initialize the database. This file sets up the necessary tables and ensures the database is ready to store and retrieve data.
   - **Usage**: Run this file once to prepare the database before starting the chatbot.

### 4. **`main.py`**
   - **Purpose**: The main script to run the RAG chatbot. This file integrates the retrieval and generation components, connects to the OpenAI API, and handles user interactions.
   - **Usage**: Execute this script to start the chatbot application.

### 5. **`onboard.txt`**
   - **Purpose**: A sample file used as input data for the RAG model. Contains example information to be stored in the vector database for retrieval.
   - **Usage**: Modify or add to this file with domain-specific data to customize the chatbot's knowledge base.

### 6. **`requirements.txt`**
   - **Purpose**: Lists all Python dependencies required for this project.
   - **Usage**: Install dependencies using the following command:  
     ```bash
     pip install -r requirements.txt
     ```

### 7. **`vector_store.py`**
   - **Purpose**: Contains functions and utilities to manage the vector database. Handles storage and retrieval of embeddings for efficient information access.
   - **Usage**: Used internally by `main.py` to manage knowledge base queries.

---

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your `.env` file with the required variables (see the `.env` section above).

4. Initialize the database:
   ```bash
   python init_db.py
   ```

5. Start the chatbot:
   ```bash
   uvicorn main:app --reload
   ```

### Setting Up the Vector Database with Docker
1. Pull the container image:
   ```bash
   docker pull username/pgvector
   ```

2. Run the container:
   ```bash
   docker run -p 5432:5432 -e POSTGRES_PASSWORD=Image Password --name my_pgvector -d username/pgvector
   ```

---

For further questions, feedback, or collaboration opportunities, feel free to reach out via the social media or email listed in the bio. Let’s build something amazing together!


