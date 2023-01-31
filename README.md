# text_summarization_api :  


## About  
This is a project developed to create a code template and to understand different text summarization techniques.  


### NLP and MLOps techniques used in project:
1. implement different methods of text summarization     
2. build inference api   
3. create streamlit application    
4. write unit test cases and performance test cases
5. code documentation
6. code formatting 
7. code deployment using docker and circleci



The basic code template for this project is derived from my another repo <a href="https://github.com/sarang0909/Code_Template">code template</a>    

I've also used my text cleaning library <a href="https://pypi.org/project/nlp-text-cleaner/">nlp-text-cleaner</a>   


The project considers following phases in ML project development lifecycle:  
Requirement    
Model Building   
Inference   
Testing     
Deployment   

We have not considered model evaluation and monitoring.   


### Requirement

Create a text summarization api which accepts a json file and returns its summarization.
(More details about json schema can't be disclosed right now.)

### Model Building   

The idea is to build a podcast text summarization.
There are many opensource as well as paid services are available to perform podcast analysis.

My goal is to create 2 methods.  
1.Use any idea/code/model from the internet
2.Implement my own idea and code 

Now,for first approach:     
Gensim,nltk,Sumy,oneai,hugging face etc. options are available. I used Sumy.

For second appraoch:    
Idea: I am not planning to use any transformer based approach. The reason is in abstractive summarization new text is generated.   
I don't want to create new text because in our use case original audio of summarized text will be used as trailer/summary of a podcast(this is my assumption).So I just want to find the most important sentences in a podcast.       
I want to come up with simple solution focusing mainly on domain informations i.e podcast.    
To summarize podcast,I will be using only text features and not audio.    

1. I think intial few sentences and last few sentences of a podcast usually contain summary/most important part of a podcast.   
2. Find the top n topics at top and bottom of a transcript.
   and get the sentences with those topics as a summary.
3. Other rules: Include sentences with Person names (they are most likely the speakers of a podcast)    

I found an opensource library<a href=" https://github.com/DerwenAI/pytextrank">pytextrank </a> for above approach using TextRank algorithm where original sentences are kept as it is in a summary.    

Ideas considered but not implemented:   
1. text summary can be converted to audio(voice of a speaker) by using text to audio tools/libraries      
2. Audio featues like duration of a spoken sentence can be considered to decide importance of that sentence   
3. Extract named entities,topics as a part of summary of podcast along with text summary.   

### Inference   
There are 2 ways to deploy this application.   
1. API using FastAPI.
2. Streamlit application

### Testing     
Unit test cases are written   

### Deployment 
Deployment is done locally using docker.   


## Code Oraganization   
Like any production code,this code is organized in following way:   
1. Keep all Requirement gathering documents in docs folder.       
2. Keep Data Collection and exploration notebooks  in src/training folder.   
3. Keep datasets in data folder.    
4. Keep model building notebooks at src/training folder.      
5. Keep generated model files at src/models.  
6. Write and keep inference code in src/inference.   
7. Write Logging and configuration code in src/utility.      
8. Write unit test cases in tests folder.<a href="https://docs.pytest.org/en/7.1.x/">pytest</a>,<a href="https://pytest-cov.readthedocs.io/en/latest/readme.html">pytest-cov</a>    
9. Write performance test cases in tests folder.<a href="https://locust.io/">locust</a>     
10. Build docker image.<a href="https://www.docker.com/">Docker</a>  
11. Use and configure code formatter.<a href="https://black.readthedocs.io/en/stable/">black</a>     
12. Use and configure code linter.<a href="https://pylint.pycqa.org/en/latest/">pylint</a>     
13. Use Circle Ci for CI/CD.<a href="https://circleci.com/developer">Circlci</a>    
 
Since we have used different design patterns like singleton,factory.It is easy to add/remove model to this code.      

## Project Organization


├── README.md         		<- top-level README for developers using this project.    
├── pyproject.toml         		<- black code formatting configurations.    
├── .dockerignore         		<- Files to be ognored in docker image creation.    
├── .gitignore         		<- Files to be ignored in git check in.    
├── .circleci/config.yml         		<- Circleci configurations       
├── .pylintrc         		<- Pylint code linting configurations.    
├── Dockerfile         		<- A file to create docker image.    
├── environment.yml 	    <- stores all the dependencies of this project    
├── main.py 	    <- A main file to run API server.    
├── main_streamlit.py 	    <- A main file to run API server.  
├── src                     <- Source code files to be used by project.    
│       ├── inference 	        <- model output generator code   
│       ├── model	        <- model files   
│       ├── training 	        <- model training code  
│       ├── utility	        <- contains utility  and constant modules.   
├── logs                    <- log file path   
├── config                  <- config file path   
├── data              <- datasets files   
├── docs               <- documents from requirement,team collabaroation etc.   
├── tests               <- unit and performancetest cases files.   
│       ├── cov_html 	        <- Unit test cases coverage report    

## Installation
Development Environment used to create this project:  
Operating System: Windows 10 Home  

### Softwares
Anaconda:4.8.5  <a href="https://docs.anaconda.com/anaconda/install/windows/">Anaconda installation</a>   
 

### Python libraries:
Go to location of environment.yml file and run:  
```
conda env create -f environment.yml
```

 

## Usage
Here we have created ML inference on FastAPI server with dummy model output.

1. Go inside 'text_summarization_api' folder on command line.  
   Run:
  ``` 
      conda activate text_summarization_api  
      python main.py       
  ```
  Open 'http://localhost:5000/docs' in a browser.
![alt text](docs/fastapi_first.jpg?raw=true)
![alt text](docs/fastapi_second.jpg?raw=true)
 
2. Or to start Streamlit application  
5. Run:
  ``` 
      conda activate text_summarization_api  
      streamlit run main_streamlit.py 
  ```  
![alt text](docs/streamlit_first.jpg?raw=true)
![alt text](docs/streamlit_second.jpg?raw=true)
 
### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
      pytest --cov-report html:tests/cov_html --cov=src tests/ 
  ```
 
### Performance Testing
1. Open 2 terminals and start main application in one terminal  
  ``` 
      python main.py 
  ```

2. In second terminal,Go inside 'tests' folder on command line.
3. Run:
  ``` 
      locust -f locust_test.py  
  ```

### Black- Code formatter
1. Go inside 'text_summarization_api' folder on command line.
2. Run:
  ``` 
      black src 
  ```

### Pylint -  Code Linting
1. Go inside 'text_summarization_api' folder on command line.
2. Run:
  ``` 
      pylint src  
  ```

### Containerization
1. Go inside 'text_summarization_api' folder on command line.
2. Run:
  ``` 
      docker build -t myimage .  
      docker run -d --name mycontainer -p 5000:5000 myimage         
  ```


### CI/CD using Circleci
1. Add project on circleci website then monitor build on every commit.



## License


NOTE: This software depends on other packages that are licensed under different open source licenses.

