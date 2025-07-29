#ANCHOR - Find Preposition -> Intersection

# Implement a function which takes a quote as a parameter to find out which given prepositions have been used in the quote. 
# The function should return the set of prepositions that are used in the quote.

# Example

# quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, 
# love of what you are doing or learning to do."""
# prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
 
# find_prep(quote)
# Output

# {'of', 'to'}


quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, 
love of what you are doing or learning to do."""

def find_prep(p_quote):
  prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
  v_word = p_quote.split()
  quote_set = set(v_word)
  v_intersection = prep.intersection(quote_set)
  
  return v_intersection

print(find_prep(quote))
  