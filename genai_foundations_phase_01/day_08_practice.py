"""
Day 8 Practice
Problem:
Write a function that returns a dictionary with two keys:
"ok" and "reply".

If prompt is not empty, return:
{"ok": True, "reply": prompt}

If prompt is empty, return:
{"ok": False, "reply": "Fallback reply"}
"""


def build_reply(prompt):
    if prompt:
        return {"ok": True, "reply": prompt}
    else:
        return {"ok": False, "reply": "Fallback reply"}
        
    # Hint:
    # 1. Check whether prompt is empty.
    # 2. If it is not empty, return a dictionary with ok=True.
    # 3. If it is empty, return a dictionary with ok=False and a fallback reply.
    pass


if __name__ == "__main__":
    print(build_reply("Explain lists"))  # expected: {'ok': True, 'reply': 'Explain lists'}
    print(build_reply(""))  # expected: {'ok': False, 'reply': 'Fallback reply'}
