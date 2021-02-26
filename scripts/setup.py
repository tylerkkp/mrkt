from os.path import exists

# Check to see if there is a config file
config_exists = exists('config.py')

def edit_test():
    if edit in ['Y', 'Yes', 'yes', 'y']:
        config()
    elif edit in ['N', 'No', 'no', 'n']:
        print('Exiting... Thank you for using MRKT')
    else:
        print('That is not an option - exiting')

def config():
    f = open("config.py", "w+")
    print(f.read())
    new_api = input('Enter new AlphaVantage API key:')
    f.write("# AlphaVantage API key\r\napi_key = " + "'" + new_api + "'")
    f.close()

if config_exists:
    print('Config file already exists:\n')
    f = open("config.py", "r")
    print(f.read() + '\n')
    f.close()
    edit = input('Do you want to edit? (this will overwrite old key)   Y/N --> ')
    edit_test()   
else:
    edit = input('No config file found - create new one with AlphaVantage API key?   Y/N --> ')
    edit_test()

