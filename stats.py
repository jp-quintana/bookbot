def get_num_words(text):
  return len(text.split())

def get_char_count(text):
  d = {}
  text = text.lower() 
  for char in text:
    if char in d:
      d[char] = d[char] + 1
    else:
      d[char] = 1
  return d