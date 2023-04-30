def split_text(text):
    text_chunks = []
    while len(text) > 500:
        chunk = text[:500]
        text = text[500:]
        text_chunks.append(chunk)
    text_chunks.append(text)
    return text_chunks
text = open(input("enter file to read with final exm (text.txt)"),"r").read()
text_chunks = split_text(text)
msg=f"hey gpt i need ur help i send u msg in parts all parts is 500 character len of parts is {len(text_chunks)} and " \
    f"update me in  the messege how much parts remain: \n____________________________________________________________________"
print(msg)
i=1
for chunk in text_chunks:
    print(f"this part {i}-remain parts {len(text_chunks)-i}")
    print(chunk)
    i+=1
