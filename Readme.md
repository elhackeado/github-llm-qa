# Github LLM Q&A
Vectorize Github discussions of your choice. Ask questions and get answers powered by LLM models.
You can plugin any LLM model of your choice. I have been using ollama.

## Run locally
1. Install ollama - https://ollama.com/download & litellm `pip install litellm`
2. Open terminal and run Gemma-2b model using `ollama run gemma:2b`. You can run any model of your choice here e.g. mistral:7b and llama:7b 
3. Open another terminal and run `litellm --model ollama/gemma:2b`. This command will start serving gemma:2b at http://0.0.0.0:8000
4. Clone this repository and run `make init`. This will install all the required libraries for this project and will ask for a link of the repository to scrape github discussions and store in chroma db in vector form. When asked enter repository of your choice which has github discussions e.g. `https://github.com/kong/kong`
5. Finally run inference using `make run` and ask your queries, All your queries will be answered only in the context of scraped github discussions.

**Enjoy**

#### Note: This repository also contains scraping of github issues so you can scrape the github issues and run inference on them using LLM models. Minor twekas in Makefile should do the job.