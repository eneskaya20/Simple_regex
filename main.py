from functions import find_com, extract_email_addresses, par_low, find_url, find_input, replace_date_format


read_file = lambda x: open(x, 'r').read()
paragraph1 = read_file('Paragraph1.txt')
paragraph2 = read_file('Paragraph2.txt')
paragraph3 = read_file('Paragraph3.txt')


find_com(paragraph1=paragraph1, paragraph2=paragraph2, paragraph3=paragraph3)

print(extract_email_addresses(paragraph1))
print(extract_email_addresses(paragraph2))
print(extract_email_addresses(paragraph3))

par_low(paragraph1=paragraph1, paragraph2=paragraph2, paragraph3=paragraph3)

find_url(paragraph1)
find_url(paragraph2)
find_url(paragraph3)

# str_input1 = input("Give the string you want to find count in paragraph1: ")
# find_input(str_input1,paragraph1)

# str_input2 = input("Give the string you want to find count in paragraph2: ")
# find_input(str_input2,paragraph2)

# str_input3 = input("Give the string you want to find count in paragraph3: ")
# find_input(str_input3,paragraph3)

replace_date_format(paragraph1)
replace_date_format(paragraph2)
replace_date_format(paragraph3)
