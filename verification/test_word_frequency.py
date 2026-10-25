import sys
sys.path.insert(0, 'workspace')

from word_frequency import word_frequency

sample_text = "Hello, world! Hello... This is a test. A test, this is."

# Create sample file
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write(sample_text)

# Call the function
result = word_frequency('sample.txt')

# Print the result
print(result)
