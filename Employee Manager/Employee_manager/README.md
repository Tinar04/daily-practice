# Employee Management System

A full-stack employee management system built with Django, featuring role-based access control, relational database design, and complete CRUD operations for managing employees, departments, and projects.

## Features

- **Role-Based Access Control (RBAC)** — Separate Admin and Employee roles with restricted access using custom decorators
- **Employee Management** — Full CRUD for employee records (Admin only)
- **Department Management** — Full CRUD for departments, with `PROTECT` on delete to prevent orphaned employees
- **Project Management** — Full CRUD for projects, with many-to-many employee assignment
- **Employee Self-Service** — Employees can view their department, assigned projects, and edit their own profile (contact & address only)
- **Search, Filter & Pagination** — Search employees by name, filter by department, paginated list views
- **Authentication** — Django's built-in auth system extended via a OneToOne relationship to support role-based login redirection

## Tech Stack

- **Backend:** Python, Django
- **Database:** MySQL
- **Frontend:** HTML, CSS (Django Templates)

## Database Schema

![Employee Management System Schema](schema.png)

**Entities:**
- **Department** — `id`, `name`
- **Employee** — `id`, `name`, `salary`, `email`, `role`, `department_id` (FK)
- **Profile** — `id`, `employee_id` (OneToOne FK), `address`, `phone`, `joining_date`
- **Project** — `id`, `name`, `start_date`, `status`
- **Employee_Project** — junction table for the Employee ↔ Project many-to-many relationship

**Relationships:**
- Department → Employee: One-to-Many (`PROTECT` on delete — a department with employees cannot be deleted)
- Employee → Profile: One-to-One
- Employee ↔ Project: Many-to-Many

## Roles

| Role | Access |
|---|---|
| **Admin** | Full CRUD on Employees, Departments, and Projects; can assign employees to projects |
| **Employee** | View own department and assigned projects; view/edit own profile (contact & address only) |

## Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/Tinar04/employee-manager.git
   cd employee-manager
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
 
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your MySQL database in `settings.py`

5. Run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (first Admin account)
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/`

## Author

**Tina Rathore**
[GitHub](https://github.com/Tinar04) · [LeetCode](https://leetcode.com/u/tira_0419)
