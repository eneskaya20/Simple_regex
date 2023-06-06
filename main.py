from functions import find_com
from functions import extract_email_addresses
from functions import par_low
read_file = lambda x: open(x, 'r').read()
paragraph1 = read_file('Paragraph1.txt')
paragraph2 = read_file('Paragraph2.txt')
paragraph3 = read_file('Paragraph3.txt')


find_com(paragraph1=paragraph1, paragraph2=paragraph2, paragraph3=paragraph3)

print(extract_email_addresses(paragraph1))
print(extract_email_addresses(paragraph2))
print(extract_email_addresses(paragraph3))

par_low(paragraph1=paragraph1, paragraph2=paragraph2, paragraph3=paragraph3)