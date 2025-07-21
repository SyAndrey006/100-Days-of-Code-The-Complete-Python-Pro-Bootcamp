'''def my_function():
    result = 5*2
    return result

print(my_function())'''

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("Andrii","synElnyk")
print(formated_string)