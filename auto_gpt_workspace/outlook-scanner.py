import json

def scan_email(email_data_dict):
    # scan logic here
    
    #if email is spam then return True, else False
    return True

if __name__ == '__main__':
    with open('email_data.json', 'r') as f:
        email_data_dict = json.load(f)

    if scan_email(email_data_dict):
        # delete email
        print('Email is spam. Deleting email...')
    else:
        # do nothing
        print('Email is not spam. No action taken.')