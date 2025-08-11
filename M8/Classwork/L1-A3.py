def test(first):
    result = {}
    for item in first:
        result[item[0]] = item[1:] 
    return result
students = [[1,'Jean Castro','v'],[2,'Lula Powell','v'],[3,'Sam Green','v'],[4,'John Doe','v']]
print("\nOriginal list of lists:")
print(students)
print("\nConverted lists to a dictionary:")
print(test(students))