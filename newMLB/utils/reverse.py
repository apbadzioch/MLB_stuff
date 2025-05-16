# Creating a function for reversing player names

def reverse_name(name):
    if ',' in name:
        last_name, first_name = name.split(', ')
        return f"{first_name} {last_name}"
    else:
        return name