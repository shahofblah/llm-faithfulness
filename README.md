# llm-faithfulness
Experiments investigating the performance of LLMs on Classification and Articulation tasks + faithfulness

## Code layout

- llm.py : Wrappers for Gemini API calls
- classification.py : Utility functions for classification tasks
- cities.py : Dataset that I use for the main task(dictionary keyed by continent name and with list of cities in that continent as value)
- notebook.ipynb : Code where I run the main experiment
- raw_results : Folder containing the console output dump from the main experiment