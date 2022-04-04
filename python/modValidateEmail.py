def isValidMSUMEmail(email):
    if email.count('@') != 1:
        return False
    tmp= email.split('@')
    if len(tmp) == 0:
        return False
    userName = tmp[0]
    if not userName[0].isalpha():
        return False
    for c in userName:
        if not c.isalpha() and c != '.':
            return False
    inst= tmp[1]
    if inst != 'mnstate.edu':
        return False
    else:
        return True

