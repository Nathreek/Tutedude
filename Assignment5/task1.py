marksheet = {
    "Ram": 89,
    "Rita": 92,
    "John": 85,
    "Alice": 95,
    "Bob": 78
}
name = input("Enter the name of the student: ")
capitalize_name = name.capitalize()
if capitalize_name in marksheet:
    print(f'{capitalize_name}\'s marks: {marksheet[capitalize_name]}')
else:
    print("Student not found in the marksheet.")
