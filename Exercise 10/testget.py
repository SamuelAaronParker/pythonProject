import getpass

def pwinput(prompt='Password: ', mask='*'):
    return getpass.getpass(prompt=prompt, stream=None).replace(mask, '')

# Example usage:
password = pwinput()
print(password)

password = pwinput(mask='X')
print(password)

password = pwinput(prompt='PW: ', mask='*')
print(password)

password = pwinput(mask='')
print(password)
