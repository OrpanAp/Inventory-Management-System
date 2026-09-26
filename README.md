# 📦 Inventory Management System

A simple web-based **Inventory Management System** built with **Django** for managing laptops, desktops, and mobile devices.

The application provides CRUD operations for inventory items, allowing users to add, view, edit, and delete devices while tracking their **type, price, availability status, and issues**.

The project uses Django's server-side rendering, ModelForms, Django ORM, SQLite, and Bootstrap for the user interface.

---

## ✨ Features

* 📦 Manage laptops
* 🖥️ Manage desktops
* 📱 Manage mobiles
* ➕ Add inventory items
* 👁️ View inventory items
* ✏️ Edit existing items
* 🗑️ Delete inventory items
* 💰 Store device prices
* 📊 Track inventory status
* ⚠️ Track device issues
* 🧩 Reusable model structure using an abstract base model
* 📝 Django ModelForms for data entry
* 🔐 CSRF protection through Django forms
* 🛠️ Django Admin integration
* 📥📤 Import/export support through `django-import-export`
* 📱 Bootstrap-based responsive interface

The repository currently exposes separate inventory sections for laptops, desktops, and mobiles.

---

# 🛠️ Technology Stack

| Technology                     | Purpose                        |
| ------------------------------ | ------------------------------ |
| **Python**                     | Programming language           |
| **Django 6.0.2**               | Web framework                  |
| **Django ORM**                 | Database operations            |
| **SQLite**                     | Database                       |
| **Django Templates**           | Server-side HTML rendering     |
| **Django ModelForms**          | Form generation and validation |
| **Bootstrap 5.3.8**            | UI styling                     |
| **django-import-export 4.4.0** | Admin data import/export       |
| **HTML5**                      | Page structure                 |
| **CSS3**                       | Custom styling                 |

The exact dependency versions currently listed by the repository include Django 6.0.2 and django-import-export 4.4.0.

Bootstrap 5.3.8 is included in the project's static files.

---

# 🏗️ Project Architecture

The project follows Django's standard structure:

```text
Inventory-Management-System/
│
├── IMS/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── inventory/
│   ├── migrations/
│   │   └── 0001_initial.py
│   │
│   ├── static/
│   │   └── css/
│   │       ├── bootstrap.min.css
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── forms.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── CSV Test/
│
├── manage.py
├── requirements.txt
└── README.md
```

The Django project is named `IMS`, while the main application is named `inventory`. `manage.py` loads `IMS.settings` as the project's settings module.

---

# 🧩 Data Model

One of the important design decisions in this project is the use of an **abstract base model**.

## Device

The common inventory fields are defined in:

```python
class Device(models.Model):
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available for purchase'),
        ('SOLD', 'Sold'),
        ('RESTOCKING', 'Restocking soon'),
    )

    type = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="SOLD"
    )
    issues = models.CharField(
        max_length=20,
        default="None"
    )

    class Meta:
        abstract = True
```

Because `Device` is declared with:

```python
abstract = True
```

Django does not create a separate `Device` database table.

Instead, its fields are inherited by the concrete models.

---

## 💻 Laptop

```python
class Laptop(Device):
    pass
```

The `Laptop` model inherits:

* `type`
* `price`
* `status`
* `issues`

---

## 🖥️ Desktop

```python
class Desktop(Device):
    pass
```

The `Desktop` model also inherits the same inventory fields.

---

## 📱 Mobile

```python
class Mobile(Device):
    pass
```

The `Mobile` model follows the same structure.

This approach avoids duplicating the common inventory fields across all three models.

---

# 📊 Inventory Status

Each device can have one of three predefined statuses:

| Value        | Meaning                |
| ------------ | ---------------------- |
| `AVAILABLE`  | Available for purchase |
| `SOLD`       | Sold                   |
| `RESTOCKING` | Restocking soon        |

The current model uses `SOLD` as the default status.

---

# 📝 Device Information

Each inventory item contains:

| Field    | Type         | Description                         |
| -------- | ------------ | ----------------------------------- |
| `id`     | BigAutoField | Automatically generated primary key |
| `type`   | CharField    | Device model/type                   |
| `price`  | IntegerField | Device price                        |
| `status` | Choice field | Current inventory status            |
| `issues` | CharField    | Device issue information            |

The initial migration confirms that Django creates separate database tables for `Laptop`, `Desktop`, and `Mobile`, each containing these inherited fields.

---

# 📝 Forms

The project uses Django `ModelForm` classes for each device category.

## Laptop Form

```python
class AddLaptopForm(forms.ModelForm):
    class Meta:
        model = models.Laptop
        fields = '__all__'
```

## Desktop Form

```python
class AddDesktopForm(forms.ModelForm):
    class Meta:
        model = models.Desktop
        fields = '__all__'
```

## Mobile Form

```python
class AddMobileForm(forms.ModelForm):
    class Meta:
        model = models.Mobile
        fields = '__all__'
```

Using ModelForms allows Django to generate the form fields directly from the models and perform model-based validation.

---

# 🔄 CRUD Logic

The inventory application implements the four basic CRUD operations:

```text
Create
  ↓
Read
  ↓
Update
  ↓
Delete
```

---

## ➕ Create

Separate views handle adding each type of device:

```text
add_laptops
add_desktops
add_mobiles
```

For example:

```python
if request.method == "POST":
    form = forms.AddLaptopForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('inventory:display_laptops')
```

The form is validated before the object is saved to the database.

---

# 👁️ Read

The application provides separate views for displaying:

```text
display_laptops
display_desktops
display_mobiles
```

For example:

```python
laptops = models.Laptop.objects.all()
```

The resulting objects are passed to the `home.html` template.

---

# ✏️ Update

Each inventory category has its own edit view:

```text
edit_laptops/<pk>
edit_desktops/<pk>
edit_mobiles/<pk>
```

The application retrieves the requested object using:

```python
get_object_or_404()
```

and then initializes the corresponding ModelForm with the existing object:

```python
form = forms.AddLaptopForm(instance=laptop)
```

When the submitted form is valid, the existing record is updated with:

```python
form.save()
```

---

# 🗑️ Delete

The project also implements separate deletion views:

```text
delete_laptops/<pk>
delete_desktops/<pk>
delete_mobiles/<pk>
```

Each view:

1. Retrieves the object.
2. Deletes it.
3. Redirects back to its inventory listing.

For example:

```python
laptop = get_object_or_404(models.Laptop, pk=pk)
laptop.delete()

return redirect('inventory:display_laptops')
```

---

# 🔗 URL Structure

The main Django URL configuration connects the `inventory` application to the root URL:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls', namespace='inventory')),
]
```

Therefore, the application does not use an `/inventory/` prefix. The inventory pages are directly accessible from the root of the website.

---

# 🌐 Application Routes

## Home

```text
/
```

Displays the main inventory page.

---

## Laptops

```text
/display_laptops
```

Displays all laptop records.

```text
/add_laptops
```

Creates a new laptop.

```text
/edit_laptops/<id>
```

Edits an existing laptop.

```text
/delete_laptops/<id>
```

Deletes a laptop.

---

## Desktops

```text
/display_desktops
```

Displays all desktop records.

```text
/add_desktops
```

Creates a new desktop.

```text
/edit_desktops/<id>
```

Edits an existing desktop.

```text
/delete_desktops/<id>
```

Deletes a desktop.

---

## Mobiles

```text
/display_mobiles
```

Displays all mobile records.

```text
/add_mobiles
```

Creates a new mobile.

```text
/edit_mobiles/<id>
```

Edits an existing mobile.

```text
/delete_mobiles/<id>
```

Deletes a mobile.

These routes are explicitly defined in `inventory/urls.py`.

---

# 🎨 User Interface

The application uses Django's template system.

The base template contains the common layout:

```text
base.html
   │
   ├── Navigation
   ├── Main content block
   └── Footer
```

Other templates extend the base template:

```django
{% extends "base.html" %}
```

---

## Inventory Listing

The `home.html` template displays the inventory in a Bootstrap table.

The table contains:

```text
#
Model
Price
Status
Issues
Actions
```

Each device also has:

```text
Edit
Delete
```

actions.

---

# 🧾 Add/Edit Form

The `forms.html` template is reused for both creating and editing devices.

For a new item:

```text
POST → add view → validate form → save → redirect
```

For an existing item:

```text
POST → edit view → validate form → update → redirect
```

The template includes Django's CSRF token:

```django
{% csrf_token %}
```

and renders the ModelForm with:

```django
{{ form }}
```

---

# 🎨 Bootstrap

The interface uses **Bootstrap 5.3.8**.

The base template loads:

```html
<link rel="stylesheet"
      href="{% static '/css/style.css' %}">

<link rel="stylesheet"
      href="{% static '/css/bootstrap.min.css' %}">
```

The Bootstrap stylesheet included in the repository identifies itself as version 5.3.8.

---

# 🛠️ Django Admin

The project also integrates the inventory models with Django Admin.

The admin class uses:

```python
from import_export.admin import ImportExportModelAdmin
```

and registers:

```python
@admin.register(
    models.Laptop,
    models.Desktop,
    models.Mobile
)
class InventoryAdmin(ImportExportModelAdmin):
    pass
```

This means the three inventory models can be managed from Django Admin and can use the import/export functionality supplied by `django-import-export`.

---

# 📥📤 Import & Export

The project includes:

```text
django-import-export==4.4.0
```

and extends Django Admin with `ImportExportModelAdmin`.

This provides import/export functionality for the registered inventory models through the admin interface.

---

# 🗄️ Database

The project uses **SQLite**.

The database configuration is:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

SQLite is suitable for this project because it requires no separate database server and works directly with Django.

---

# 🔐 Security

The application uses Django's built-in security middleware and CSRF protection.

The middleware includes:

```text
SecurityMiddleware
SessionMiddleware
CommonMiddleware
CsrfViewMiddleware
AuthenticationMiddleware
MessageMiddleware
XFrameOptionsMiddleware
```

The inventory forms explicitly include:

```django
{% csrf_token %}
```

which protects POST form submissions against CSRF attacks.

---

# ⚙️ Django Configuration

The project is configured with:

```text
Django 6.0.2
SQLite
Django Templates
django-import-export
Bootstrap 5.3.8
```

The settings file was generated for Django 6.0.2 and registers the `inventory` and `import_export` applications.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd Inventory-Management-System
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

The repository provides a `requirements.txt` containing the project's Django and import/export dependencies.

---

## 4. Apply migrations

```bash
python manage.py migrate
```

---

## 5. Create an admin account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your Django administrator account.

---

## 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The existing project setup uses the same development-server workflow.

---

# 🖥️ Using the Application

After starting the development server:

### Home

```text
/
```

From the navigation interface you can choose:

```text
Laptops
Desktops
Mobiles
```

Each category provides an option to add a new device.

### Example Workflow

```text
Open Application
      ↓
Choose Laptops
      ↓
View Existing Laptops
      ↓
Add / Edit / Delete
      ↓
Database Updated
      ↓
Return to Inventory List
```

The same workflow applies to desktops and mobiles.

---

# 🧠 Application Logic

The application's core logic can be summarized as:

```text
Browser
   │
   ▼
Django URL Router
   │
   ▼
Inventory View
   │
   ├── GET
   │    └── Query database
   │
   └── POST
        │
        ▼
     ModelForm
        │
        ├── Invalid
        │      └── Display form errors
        │
        └── Valid
               │
               ▼
            Save Model
               │
               ▼
            Redirect
```

For editing, the existing database object is passed into the ModelForm using `instance=...`, allowing Django to update the existing record rather than creating a new one.

---

# 📌 Current Scope

The current implementation focuses on basic inventory management for three categories:

```text
Laptop
Desktop
Mobile
```

Each item stores:

```text
Device Type
Price
Status
Issues
```

The current codebase does **not** implement a separate sales-management workflow, customer management system, authentication-based inventory ownership, or a dedicated reporting dashboard. The existing repository README mentions some of these concepts, but they are not represented in the current inventory application's Python views/models.

---

# 🚧 Possible Future Improvements

Possible extensions to the current system include:

* 🔐 User authentication and authorization
* 👥 Multiple inventory users
* 🔎 Inventory search
* 🏷️ Categories and brands
* 📦 Quantity/stock-count tracking
* 📈 Dashboard statistics
* 📊 Inventory reports
* 💰 Sales management
* 🧾 Invoice generation
* 📥📤 Dedicated CSV import/export pages
* 🔔 Low-stock notifications
* 🧪 Automated tests
* 🔒 Environment-based secret configuration
* 🚀 Production deployment configuration

These are potential extensions rather than features currently implemented in the repository.

---

# 🔒 Production Notes

The current project is configured as a Django development application.

The settings currently contain:

```python
DEBUG = True
```

and a secret key directly in `settings.py`.

Before deploying publicly, the following should be changed:

* Set `DEBUG = False`
* Move `SECRET_KEY` to environment variables
* Configure `ALLOWED_HOSTS`
* Use a production-ready database where appropriate
* Configure static files for production
* Configure HTTPS
* Review Django's deployment security checklist
* Add authentication/authorization where required

---

# 📚 What This Project Demonstrates

This project provides practical examples of several Django concepts:

### Django Fundamentals

* Project/app structure
* Settings
* URL routing
* Views
* Templates
* Static files
* Models
* Migrations
* Django ORM

### Database

* SQLite
* Model inheritance
* Abstract base models
* QuerySets
* Object retrieval
* Create/update/delete operations

### Forms

* ModelForms
* Form validation
* POST handling
* CSRF protection

### Frontend

* Django templates
* Template inheritance
* Bootstrap
* Responsive navigation
* Bootstrap tables
* Reusable form templates

### Administration

* Django Admin
* Model registration
* `django-import-export`
* Import/export-enabled admin

---

# 📁 Core Files Explained

| File                             | Responsibility                  |
| -------------------------------- | ------------------------------- |
| `manage.py`                      | Django command-line entry point |
| `IMS/settings.py`                | Project configuration           |
| `IMS/urls.py`                    | Root URL routing                |
| `inventory/models.py`            | Inventory database models       |
| `inventory/forms.py`             | ModelForms                      |
| `inventory/views.py`             | CRUD application logic          |
| `inventory/urls.py`              | Inventory URL routes            |
| `inventory/admin.py`             | Django Admin configuration      |
| `inventory/templates/base.html`  | Shared page layout              |
| `inventory/templates/home.html`  | Inventory listing UI            |
| `inventory/templates/forms.html` | Add/edit form UI                |
| `inventory/static/css/`          | Frontend styles                 |
| `requirements.txt`               | Python dependencies             |

The core application structure and relationships are reflected directly in the repository files.

---

# 👨‍💻 Author

**OrpanAp**

GitHub: `OrpanAp`

---

# 📄 License

No explicit license file is currently visible in the repository root.

If this project is intended to be reused or distributed, an appropriate open-source license can be added.

---

## ⭐ Project Summary

**Inventory Management System** is a Django-based CRUD application for managing laptop, desktop, and mobile inventory.

Its core architecture is:

```text
Django
   │
   ├── Models
   │      ├── Device (Abstract)
   │      ├── Laptop
   │      ├── Desktop
   │      └── Mobile
   │
   ├── ModelForms
   │      ├── AddLaptopForm
   │      ├── AddDesktopForm
   │      └── AddMobileForm
   │
   ├── Views
   │      ├── Display
   │      ├── Add
   │      ├── Edit
   │      └── Delete
   │
   ├── Templates
   │      ├── Base
   │      ├── Inventory
   │      └── Forms
   │
   ├── SQLite
   │
   └── Django Admin
          └── Import / Export
```

The project demonstrates a clean beginner-friendly Django workflow from **database model → ModelForm → view → URL → template → database**, while also introducing abstract model inheritance and Django Admin import/export functionality.
