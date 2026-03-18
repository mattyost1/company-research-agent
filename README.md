# Company Research Agent

An AI agent that researches any company and returns a structured brief using live web search.

## What it does
- Takes a company name as input
- Searches the web in real time using Tavily
- Returns a structured overview including financials, recent news, and key facts

## Built with
- Python
- Anthropic Claude API
- Tavily Search API

## Setup
1. Clone this repo
2. Install dependencies:
   pip3 install anthropic tavily-python
3. Add your API keys to test.py
4. Run:
   python3 test.py

## Usage
Change the company name in the last line of test.py:
   run_agent("Research [company name] and give me a structured overview.")