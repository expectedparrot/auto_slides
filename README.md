# Intro to `auto_slides`

This little command line tool lets you create markdown-based slides on any topic. 
You'll need `pandoc` on your system.

## Set-up 

```
python3 -m venv venv 
source venv/bin/active  
pip install edsl 
pip install typer
```

## OpenAI keys
Put your OpenAI API key in a `.env` file like so: 

```
OPENAI_API_KEY=<Your KEY>
```

## Usage 

Getting help
```
python auto_slides.py --help
```

### Basic use 
```
python auto_slides.py --filename 'bees' --topic 'How to keep yourself from getting stung by bees' --num-slides 4
```