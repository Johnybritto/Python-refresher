# Gemini Free Tier Day 5 basics problem
# Write code that:
# - loops through the values
# - converts valid numbers to int
# - skips invalid values
# - prints the final total

values = ["10", "20", "x", "30"]
total = 0 
for i in values:
    try:
        number=int(i)
        total += number
    except ValueError:
        pass
print(total) 
