from ConstraintUtilities import select_general, unique_general, prompt_for_date
from Utilities import Utilities
from CommandLogger import CommandLogger, log
from pymongo import monitoring
from Menu import Menu
from Option import Option
from menu_definitions import menu_main, add_select, list_select, select_select, delete_select, update_select
import CommonUtilities as CU  # Utilities that work for the sample code & the worked HW assignment.
from decimal import Decimal

from Course import Course
from Department import Department
from Major import Major
from Section import Section
from Student import Student
from StudentMajor import StudentMajor

from ProgramData import VALIDS, BUIDLINGS, SCHEDULES, SEMESTERS


VALID_BUILDINGS = VALIDS[BUIDLINGS]
VALID_SCHEDULES = VALIDS[SCHEDULES]
VALID_SEMESTERS = VALIDS[SEMESTERS]

def menu_loop(menu: Menu):
    """Little helper routine to just keep cycling in a menu until the user signals that they
    want to exit.
    :param  menu:   The menu that the user will see."""
    action: str = ''
    while action != menu.last_action():
        action = menu.menu_prompt()
        print('next action: ', action)
        exec(action)


def add():
    menu_loop(add_select)


def list_members():
    menu_loop(list_select)


def select():
    menu_loop(select_select)


def delete():
    menu_loop(delete_select)


def update():
    menu_loop(update_select)

# ---------- Select Functions ------------
def select_department() -> Department:
    return select_general(Department)

def select_course() -> Course:
    return select_general(Course)

def select_major() -> Major:
    return select_general(Major)

def select_section() -> Section:
    return select_general(Section)

def select_student() -> Student:
    return select_general(Student)


# ---------- Add Functions ----------
def add_course():

    pass

def add_department():
    success = False
    while not success:    
        name = input("Department name: ")
        abbreviation = input("Department abbreviation: ")
        chair = input("Department chair")
        
        building = ''
        while building not in VALID_BUILDINGS:
            building = input("Department building: ")
            if building not in VALID_BUILDINGS:
                print(f"Invalid Input: Building must be one of the following -> {VALID_BUILDINGS}")
        
        office = ''
        while True:
            try:
                office = int(input("Department office: "))
                break
            except:
                print("Invalid Input: Office must be an integer")

        description = input("Department description: ")

        new_dept = Department(name, abbreviation, chair, building, office, description)
        violated_constraints = unique_general(new_dept)
        if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input values violated constraint: ', violated_constraint)
                print('try again')
        else:
            try:
                new_dept.save()
                success = True
            except Exception as e:
                print('Errors storing the new order:')
                print(Utilities.print_exception(e))



def add_major():
    pass

def add_section():
    pass

def add_student():
    pass

def add_student_major():
    pass

# ---------- Delete Functions ----------
def delete_course(): ##
    course = select_course()
    try:
        course.delete()
    except Exception as e:
        print(f"Failure to delete course:\n{e}")
# done
def delete_department():
    department = select_department()
    has_no_references = True

    if len(department.majors) != 0:
        print("ALERT: Selected department has associated majors. Delete majors first, then try again.")
        has_no_references = False
    
    if len(department.courses) != 0:
        print("ALERT: Selected department has associated courses. Delete courses first, then try again.")
        has_no_references = False
    
    if not has_no_references:
        print("OUPUT: No deletes made.")
        return

    try:
        department.delete()
    except Exception as e:
        print(f"Failure to delete department:\n{e}")

# done
def delete_major():
    major = select_major()
    try:
        major.delete()
    except Exception as e:
        print(f"Failure to delete major:\n{e}")


def delete_section():
    section = select_section()
    try:
        section.delete()
    except Exception as e:
        print(f"Failure to delete section:\n{e}")

def delete_student():
    student = select_student()
    try:
        student.delete()
    except Exception as e:
        print(f"Failure to delete student:\n{e}")

# done
def delete_student_major():
    student = select_student()
    majors = student.majors

    menu_items: [Option] = []
    for major in majors:
        menu_items.append(major.__str__(), major)
    
    chosen_major = Menu("Student Majors", "Choose which major to remove from this student", menu_items).menu_prompt()
    try:    
        student.remove_major(chosen_major)
    except Exception as e:
        print(f"Failure to delete student major:\n{e}")

# ---------- List Functions ----------
def list_all_courses():
    count = 1
    for course in Course.__objects:
        print(f"{count}. --------------\n{course.__str__()}")
        count += 1

def list_dept_courses():
    dept = select_department()
    count = 1
    for course in Course.__objects(deptAbbreviation=dept.abbreviation):
        print(f"{count}. --------------\n{course.__str__()}")
        count += 1

def list_all_departments():
    count = 1
    for department in Department.__objects:
        print(f"{count}. --------------\n{department.__str__()}")
        count += 1

def list_all_majors():
    count = 1
    for major in Major.__objects:
        print(f"{count}. --------------\n{major.__str__()}")
        count += 1

def list_all_sections():
    count = 1
    for section in Section.__objects:
        print(f"{count}. --------------\n{section.__str__()}")
        count += 1

def list_all_students():
    count = 1
    for student in Student.__objects:
        print(f"{count}. --------------\n{student.__str__()}")
        count += 1


if __name__ == '__main__':
    print('Starting in main.')
    monitoring.register(CommandLogger())
    db = Utilities.startup()
    main_action: str = ''
    while main_action != menu_main.last_action():
        main_action = menu_main.menu_prompt()
        print('next action: ', main_action)
        exec(main_action)
    log.info('All done for now.')