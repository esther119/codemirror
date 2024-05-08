import re

userInput = """
def pair_frequency(ids):

  counts = {}
  for pair in zip(ids, ids[1:]): # Pythonic way to iterate consecutive elements
    counts[pair] = counts.get(pair, 0) + 1
  return counts

stats = pair_frequency(tokens)
print(stats)
"""

# Attempt to extract the function using regex
# This pattern assumes consistent indentation with spaces for simplicity
# It looks for the function start, captures lines with at least one more space of indentation than the start, and stops when the indentation decreases or matches the start
match = re.search(r"(def pair_frequency\(.*?\):(?:\n\s+.+)+)", userInput, re.DOTALL)
print('match', match)
if match:
    pair_frequency_function = match.group(0)
    # print('pair_frequency_function')
    print("Function extracted successfully.")
else:
    print("Function extraction failed.")

print('pair_frequency_function', pair_frequency_function)
