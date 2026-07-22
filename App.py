import json

def save_contacts():
    file=open('contacts.json','r')
    contacts=file.read()
    contacts_dictionary=json.load(contacts)
    print(contacts_dictionary,type(contacts_dictionary))
    contacts_to_save=contacts_dictionary['contacts']
    

def main():
    pass

if __name__ == '__main__':
    main()