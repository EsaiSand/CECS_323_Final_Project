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



"""
This protects Order from deletions in OrderItem of any of the objects reference by Order
in its order_items list.  We could not include this in Order itself since that would 
make a cyclic delete_rule between Order and OrderItem.  I've commented this out because
it makes it impossible to remove OrderItem instances.  But you get the idea how it works."""


# OrderItem.register_delete_rule(Order, 'orderItems', mongoengine.DENY)

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
    pass

def add_major():
    pass

def add_section():
    pass

def add_student():
    pass

def add_student_major():
    pass

# ---------- Delete Functions ----------
def delete_course():
    course = select_course()
    try:
        course.delete()
    except Exception as e:
        print(f"Failure to delete course:\n{e}")

def delete_department():
    department = select_department()
    try:
        department.delete()
    except Exception as e:
        print(f"Failure to delete department:\n{e}")

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

    # Need to delete all student major items too

    try:
        student.delete()
    except Exception as e:
        print(f"Failure to delete student:\n{e}")

def delete_student_major():
    pass

# ---------- List Functions ----------
def list_courses():
    pass

def list_departments():
    pass

def list_majors():
    pass

def list_sections():
    pass

def list_students():
    pass


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