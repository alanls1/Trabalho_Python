#--------------db-----------------
courseRegistre = []

disciplineRegistre = []

studentRegistre = []


#--------------Menu-----------------

def menu():
    print(60 * "\n")
    print("=========================")

    print("1 - Cursos")
    print("2 - Disciplinas")
    print("3 - Área do Aluno")
    print(" ")
    print("0 - Encerrar o programa")

    print("=========================")


def courseMenu():
    print(60 * "\n")
    print("=========================")

    print("1 - Cadastrar curso")
    print("2 - Alterar Curso cadastrado")
    print("3 - Consultar Curso pelo Id")
    print("4 - Consultar Cursos disponíveis")
    print(" ")
    print("0 - Voltar")

    print("=========================")

    option = int(input("\n\nDigite uma opção: "))

    if(option == 1):
        registerCourse()

    elif(option == 2):
        changeCourse()

    elif(option == 3):
        consultCourse()

    elif(option == 4):
        coursesInfo()

    else:
        main()
       

def disciplineMenu():
    print(60 * "\n")
    print("=========================")

    print("1 - Cadastrar Disciplinas")
    print("2 - Alterar Disciplinas cadastradas")
    print("3 - Consultar Disciplinas pelo Id")
    print("4 - Consultar Disciplinas disponíveis")
    print(" ")
    print("0 - Voltar")

    print("=========================")

    option = int(input("\n\nDigite uma opção: "))

    if(option == 1):
        registerDiscipline()

    elif(option == 2):
        changeDiscipline()

    elif(option == 3):
        consultDiscipline()

    elif(option == 4):
        disciplinesInfo()

    else:
        main()


def studentMenu():
    print(60 * "\n")
    print("=========================")

    print("1 - Cadastrar Aluno")
    print("2 - Alterar Aluno cadastrado")
    print("3 - Consultar Aluno pelo Id")
    print("4 - Consultar Alunos disponíveis")
    print(" ")
    print("0 - Voltar")

    print("=========================")

    option = int(input("\n\nDigite uma opção: "))

    if(option == 1):
        registerStudent()

    elif(option == 2):
        changeStudent()

    elif(option == 3):
        consultStudent()

    elif(option == 4):
        studentsInfo()

    else:
        main()

#--------------filtrar-----------------

def filter(value, matrix):
    for x in matrix:
        if value in x:
            return x          
    return False

def toBack(function):
    back = int(input("\n\n0 - Voltar: "))

    if back == 0:
        function()
    else:
        menu()

def changeCourse():
    print(60 * "\n")

    if len(courseRegistre) == 0:
        registre = input("Nenhum curso cadastrado!\n\nDeseja cadastrar um curso novo? ")
        if registre == "s":
            registerCourse()
        else:
            toBack(courseMenu)


    id = int(input("\nInforme o Id que deseja alterar: "))
    findCourse = filter(id, courseRegistre)
    

    if findCourse != False:
        print("\n\n=========================")

        print("\nID: {}\nNome: {}\nDuração: {}"
            .format(findCourse[0], findCourse[1], findCourse[2]))

        print("\n=========================")
        findCourse[1] = str(input("\n\nInforme o Nome para alteração\nNome: "))
        findCourse[2] = int(input("\nInforme a duração para alteração\nDuração: "))
    
    else:
        print("\nCurso não encontrado!\n")
        changeCourse()

    print(60 * "\n")
    print("\nAlteração feita com sucesso!")

    print("\n\n=========================")

    print("\nID: {}\nNome: {}\nDuração: {}"
            .format(findCourse[0], findCourse[1], findCourse[2]))

    print("\n=========================")

    toBack(courseMenu)


def changeDiscipline():
    print(60 * "\n")
    if len(courseRegistre) == 0 :
        registre = input("Nenhum curso cadastrado!\n\nDeseja cadastrar um curso novo? ")
        if registre == "s":
            registerCourse()
        else:
            toBack(disciplineMenu)

    if len(disciplineRegistre) == 0:
        registre = input("Nenhuma disciplina cadastrada!\n\nDeseja cadastrar uma nova disciplina? ")
        if registre == "s":
            registerDiscipline()
        else:
            toBack(disciplineMenu)

    else:
        id = int(input("\nInforme o ID que deseja alterar: "))
        findDiscipline = filter(id, disciplineRegistre)
        findCourse = filter(id, courseRegistre)

        if disciplineRegistre == 0:
            print("Nenhum curso cadastrado!")

        if findDiscipline != False:
            print("\n\n=========================")

            print("\nID: {}\nNome: {}\ncurso: {}"
                .format(findDiscipline[0], findDiscipline[1], findCourse[1]))

            print("\n=========================")

            findDiscipline[1] = str(input("\n\nInforme o nome para alteração\nNome: "))
        
        else:
            print("\nId não encontrado!\n")
            changeDiscipline()

        print(60 * "\n")
        print("\nAlteração feita com sucesso!")
        print("\n=========================")

        print("\nID: {}\nNome: {}\nCurso: {}"
                .format(findDiscipline[0], findDiscipline[1], findCourse[1]))
        print("\n=========================")

        toBack(disciplineMenu)  



def changeStudent():
    print(60 * "\n")
    if len(studentRegistre) == 0 :
        registre = input("Nenhum curso cadastrado!\n\nDeseja cadastrar um curso novo? ")
        if registre == "s":
            registerStudent()
        else:
            toBack(studentMenu)

    ra = int(input("\nInforme o RA que deseja alterar: "))
    findStudent = filter(ra, studentRegistre)
    findCourse = filter(ra, courseRegistre)

   
    if findStudent != False:
        print("\n\n=========================")
        print("\nRA: {}\nNome: {}\nCPF: {}\nCurso: {}"
            .format(findStudent[0], findStudent[1], findStudent[2], findCourse[1],))
        print("\n=========================")
        findStudent[1] = str(input("\n\nInforme o Nome para alteração\nNome: "))
        findStudent[2] = int(input("\nInforme o CPF para alteração\nCPF: "))
    
    else:
        print("\nRA não Encontrado!\n")
        changeStudent()

    print(60 * "\n")
    print("\nAlteração feita com sucesso!")
    print("\n\n=========================")
    print("\nRA: {}\nNome: {}\nCPF: {}\nCurso: {}"
            .format(findStudent[0], findStudent[1], findStudent[2], findCourse[1],))
    print("\n=========================")

    toBack(studentMenu)



def consultCourse(): 
    print(60 * "\n")
    findId = int(input("\nInforme o ID que deseja consultar: "))
    findCourse = filter(findId, courseRegistre)
    findDiscipline = filter(findId, disciplineRegistre)

    if findCourse != False:
        print("\n\n=========================")
        print("\nID: {}\nNome: {}\nDuração: {}\nDisciplinas: {}"
                .format(findCourse[0], findCourse[1], findCourse[2], findDiscipline[1],))
        print("\n=========================")
    else:
        print("\nId não Encontrado!\n")
        changeStudent()
    
    toBack(courseMenu)


    
def consultDiscipline():
    print(60 * "\n")
    id = int(input("\nInforme o ID que deseja consultar: "))
    findDiscipline = filter(id, disciplineRegistre)
    
    if findDiscipline != False:
        findCourse = filter(id, courseRegistre)

        print("\n=========================")

        print("\nID: {}\nNome: {}\nCurso: {}"
            .format(findDiscipline[0], findDiscipline[1], findCourse[1]))

        print("\n=========================")

    else:
        print("\nID não Encontrado!\n")
        changeDiscipline()
    
    toBack(disciplineMenu)




def consultStudent():
    print(60 * "\n")
    ra = int(input("\nInforme o RA que deseja consultar: "))
    findStudent = filter(ra, studentRegistre)
    
    if findStudent != False:
        findCourse = filter(ra, courseRegistre)
        print("\n\n=========================")

        print("\nRA: {}\nNome: {}\nCPF: {}\nCurso: {}"
            .format(findStudent[0], findStudent[1], findStudent[2], findCourse[1],))

        print("\n=========================")
    else:
        print("\nRA não Encontrado!\n")
        changeStudent()
    
    toBack(studentMenu)



def coursesInfo():
    print(60 * "\n")
    for line in courseRegistre:
        findDiscipline = filter(line[0], disciplineRegistre)
        print("\n\n=========================")
        print("\n     Curso: {}\n\nID: {}\nDisciplina: {}\nDuração: {}"
                .format(line[1], line[0], findDiscipline[1], line[2]))
        print("\n=========================")

    toBack(courseMenu)


def disciplinesInfo():
    print(60 * "\n")
    
    for line in disciplineRegistre:
        findCourse = filter(line[2], courseRegistre)
        print("\n\n=========================")

        print("\n    Nome: {}\n\nID: {}\nCurso: {}"
                .format(line[1], line[0], findCourse[1]))

        print("\n=========================")

    toBack(disciplineMenu)



def studentsInfo():
    print(60 * "\n")

    for line in studentRegistre:
        findCourse = filter(line[3], courseRegistre)
        print("\n=========================")

        print("\n     Nome: {}\n\nRA: {}\nCPF: {}\nCurso: {}"
                .format(line[1], line[0], line[2], findCourse[1]))

        print("\n=========================") 

    toBack(studentMenu)

#--------------Registro-----------------

def checkCourse(): 
    courseID = int(input("\nID do curso: "))
    courseFiltered = filter(courseID, courseRegistre) 

    while courseFiltered == False:
            print("Curso Inexistente!")
            courseID = int(input("\nID do curso: "))
            courseFiltered = filter(courseID, courseRegistre) 

    return courseID


def registerCourse():
    cont = "s"
    courseArray = []
    courseIdRegistre = []

    while (cont == "s"):
        print(60 * "\n")

        courseID = int(input("ID do curso: "))
        courseName = str(input("\nCurso: "))
        courseDuration = int(input("\nDuração do curso: "))
        
        if courseID in courseIdRegistre:
            while courseID in courseIdRegistre:
                print("\nID do curso já registrado!\n tente Novamente!\n")
                courseID = int(input("Id do Curso: "))
            courseArray = [courseID, courseName, courseDuration]
            courseRegistre.append(courseArray)
            courseIdRegistre.append(courseID)

        else:
            courseArray = [courseID, courseName, courseDuration]
            courseRegistre.append(courseArray)
            courseIdRegistre.append(courseID)
            

        cont = input("\n\nCurso Cadastrado com sucesso!\n\nDeseja Cadastrar outro Curso?\n\ncontinuar: ")
    
    toBack(courseMenu)




def registerDiscipline():
    cont = "s"
    disciplineArray = []
    idDiscipline = []

    while (cont == "s"):
        print(60 * "\n")

        disciplineID = int(input("ID disciplina: "))
        disciplineName = str(input("\nNome da disciplina: "))
        courseID = checkCourse()

        if disciplineID in idDiscipline:
            while disciplineID in idDiscipline:
                print("\nDisciplina já registrada!\n tente Novamente!\n")
                disciplineID = int(input("ID da disciplina: "))
            
            disciplineArray = [disciplineID, disciplineName, courseID]
            disciplineRegistre.append(disciplineArray)
            idDiscipline.append(disciplineID)

        else:
            disciplineArray = [disciplineID, disciplineName, courseID]
            disciplineRegistre.append(disciplineArray)
            idDiscipline.append(disciplineID)
            

        cont = input("\n\nDisciplina Cadastrado com sucesso!\n\nDeseja Cadastrar outro Disciplina?\n\ncontinuar: ")
    
    toBack(disciplineMenu)
        


def registerStudent():
    cont = "s"
    studentArray = []
    raStudent = []

    while (cont == "s"):
        print(60 * "\n")

        studentRa = input("RA: ")
        studentName = str(input("\nnome: "))
        studentCpf = int(input("\nCPF: "))
        courseID = checkCourse()


        if studentRa in raStudent:
            while studentRa in raStudent:
                print("\nRA já registrado!\n tente Novamente!\n")
                studentRa = input("RA: ")

            studentArray = [studentRa, studentName, studentCpf, courseID]
            studentRegistre.append(studentArray)
            raStudent.append(studentRa)

        else:  

            studentArray = [studentRa, studentName, studentCpf, courseID]
            studentRegistre.append(studentArray)
            raStudent.append(studentRa)

        cont = input("\n\nAluno Cadastrado com sucesso!\n\nDeseja Cadastrar outro aluno?\n\ncontinuar: ") 

    toBack(studentMenu) 

           

def main():
    menu()

    option = int(input("\nDigite uma opção: "))

    if(option == 1):
        courseMenu()

    elif(option == 2):
        disciplineMenu()

    elif(option == 3):
        studentMenu()

    else:
        print("Ate mais!")
       

main()