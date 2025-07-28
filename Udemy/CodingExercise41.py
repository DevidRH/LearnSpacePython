#ANCHOR - Three Equal Chunks
"""
Given a list slice it into Three Equal Chunks and reverse each chunk.

sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
Output

Chunk-1 = [18, 55, 21]
Chunk-2 = [22, 24, 33]
Chunk-3 = [79, 35, 68]

"""

sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

first_chunks_list = list()
second_chunks_list = list()
third_chunks_list = list()
for i in range(len(sample_list)):
  if i < 3 :
    first_chunks_list.append(sample_list[i])
  elif i < 6 : 
    second_chunks_list.append(sample_list[i])
  else:
    third_chunks_list.append(sample_list[i])

print(f"{first_chunks_list[::-1]}, \n{second_chunks_list[::-1]}, \n{third_chunks_list[::-1]}")


print("----------------------------------OR----------------------------------")

sample_list_2 = sample_list

length_ = len(sample_list_2)
chunk_size = int(length_ / 3)

start_element = 0
end_element = chunk_size

for i in range(1, 4):
  chunk_list = list(sample_list_2[start_element: end_element])
  reversed_chunk = list(reversed(chunk_list))   #NOTE - converted to list using list() func, after thar reversed sequence of chunk list to descending
  print(f"Chunk - {i} = {reversed_chunk}")
  print(f"List : [{start_element}, {end_element}]")
  start_element = end_element
  end_element += chunk_size
  
