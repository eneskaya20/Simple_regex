import regex as re

# counts the total number of occurrences of the words containing the subtext "com"
def find_com(paragraph1, paragraph2, paragraph3):
    print("'com' keyword count in paragraph 1: " + str(len(re.findall("com", paragraph1))))
    print("'com' keyword count in paragraph 2: " + str(len(re.findall("com", paragraph2))))
    print("'com' keyword count in paragraph 3: " + str(len(re.findall("com", paragraph3))))


def extract_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    # \b is for word boundary and 

    email_addresses = re.findall(pattern, text)
    return email_addresses

def par_low(paragraph1, paragraph2, paragraph3):
    t1 = re.findall('([A-Z][a-z]+)', paragraph1)
    t2 = re.findall('([A-Z][a-z]+)', paragraph2)
    t3 = re.findall('([A-Z][a-z]+)', paragraph3)
    print(t1)
    print(t2)
    print(t3)
    
    for i in range(len(t1)):
        t1[i] = t1[i].lower()
    for i in range(len(t2)):
        t2[i] = t2[i].lower()
    for i in range(len(t3)):
        t3[i] = t3[i].lower()

    print(t1)
    print(t2)
    print(t3)   



