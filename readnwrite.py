f = open('\link', 'r')
out = open('\link', 'w')

for line in f:
    email_addr = line
    at_index = email_addr.find('@')
    user_name = email_addr[0:at_index]
    