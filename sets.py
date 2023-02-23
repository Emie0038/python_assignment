# Creating sets
board_of_directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

#who in the board of directors is not an employee?
not_employees = board_of_directors - employees
print("Members of the board of directors who are not employees:", not_employees)

#who in the board of directors is also an employee?
board_and_employees = board_of_directors.intersection(employees)
print(board_and_employees)


#how many of the management is also member of the board?
management_and_board = management.intersection(board_of_directors)
print("Number of members of the management who are also members of the board:", len(management_and_board))

#All members of the management also an employee
if management.issubset(employees):
    print("All members of the management are also employees.")
else:
    print("Not all members of the management are also employees.")

#All members of the management also in the board?
if management.issubset(board_of_directors):
    print("All members of the management are also members of the board.")
else:
    print("Not all members of the management are also members of the board.")

#Who is an employee, member of the management, and a member of the board?
employee_management_board = employees.intersection(management).intersection(board_of_directors)
print("Employees who are also members of the management and the board:", employee_management_board)

#Who of the employee is neither a member or the board or management?
not_board_or_management = employees.difference(board_of_directors).difference(management)
print("Employees who are not members of the board or management:", not_board_or_management)


