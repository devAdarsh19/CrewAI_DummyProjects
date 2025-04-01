### CrewAI Learning Projects

## Creating a virtual environment
Create a virtual environment to install all dependencies using the command:
```
python -m venv <env_name>
```

Activate your virtual environment:
(On Windows)
```
<env_name>/Scripts/activate
```

(On Linux/MacOS)
```
source <env_name>/bin/activate
```

## Install dependencies
```
pip install crewai 'crewai[tools]'
```

Or if using uv, follow this [link](https://docs.crewai.com/installation)


## Next Steps
- Navigate into a directory
  ```
  cd <directory>
  ```
- Generate API keys and paste them in the .env file (or download Ollama model llama3.2:1b).
- Kickoff your crew
  ```
  python src/<directory>/main.py
  ```
