# Gemini Free Tier Day 7 basics problem
# Write code that:
# - stores chunks = ["Py", "thon", " ", "rocks"]
# - joins the chunks into one string
# - prints the final string

chunks = ["Py", "thon", " ", "rocks"]

# Your code here
st = ""
p=""
for i in chunks:
    p += i
    st += "".join(i)

print(st)

print(p)

res = " ".join(chunks)


print(res)
