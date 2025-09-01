salaries=[]
#CRUD -Create,Read All,Read by Id,update,delete
#                       Read by Salary

def create_salary(salary):
    global salaries
    salaries.append(salary)


def read_all():
    return salaries

def read_by_salaries(salary):#RANGE(STOP) | RANGE(START,STOP)| RANGE(START,STOP,STEP) return first occureence of salary
    for I in range(len(salaries)): #len(salaries)=5, I=0,1,2,3,4
        if salaries[I]==salary:
            return I
    return -1

def update(old_salary,new_salary):
    global salaries
    index=read_by_salaries(old_salary)
    salaries[index]=new_salary

def delete_by_salary(salary):
    global salaries
    index=read_by_salaries(salary)
    salaries.pop(index)

#test code
create_salary(1000)
create_salary(5000)
create_salary(8000)
create_salary(3000)
result_salaries=read_all()
for salary in result_salaries:
    print(salary)

print(read_by_salaries(8000))
print(read_by_salaries(4000))
print(salaries[read_by_salaries(8000)])

update(8000,8500)
print(read_all())
delete_by_salary(1000)
print(read_all())