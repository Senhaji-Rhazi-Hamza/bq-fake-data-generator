import json

def open_json(filepath):
  with open(filepath, 'r') as f:
    data = json.load(f)
  return data
