## 1. Giới thiệu về

Một web cho phép người dùng ghi lại(có thể ảnh, video) những trải nghiệm trong ngày như một cuốn nhật ký viết tay.

## 2. Các chức năng chính

- Đăng nhập/ Đăng ký
- Viết nhật ký
- Chỉnh sữa nhật ký

## 3. Công cụ

- Backend: Django
- Fontend: HTML, CSS, JavaScript
- Database: PostgreSQL

## 4. Cấu trúc project

├── 📁 accounts
│ ├── 📁 templates
│ │ └── 📁 accounts
│ │ ├── 🌐 login.html
│ │ └── 🌐 register.html
│ ├── 🐍 **init**.py
│ ├── 🐍 apps.py
│ ├── 🐍 forms.py
│ ├── 🐍 urls.py
│ └── 🐍 views.py --> xử lý logic
├── 📁 diary
│ ├── 📁 migrations
│ │ ├── 🐍 0001_initial.py
│ │ └── 🐍 **init**.py
│ ├── 📁 static
│ │ └── 📁 diary
│ │ ├── 📁 css
│ │ └── 📁 js
│ ├── 📁 templates
│ │ └── 📁 diary
│ │ ├── 🌐 analyze.html
│ │ ├── 🌐 diary_detail.html
│ │ ├── 🌐 index.html
│ │ ├── 🌐 settings.html
│ │ └── 🌐 write_diary.html
│ ├── 🐍 **init**.py
│ ├── 🐍 apps.py
│ ├── 🐍 models.py
│ ├── 🐍 urls.py
│ └── 🐍 views.py
├── 📁 diary_app
│ ├── 🐍 **init**.py
│ ├── 🐍 asgi.py
│ ├── 🐍 settings.py
│ ├── 🐍 urls.py
│ └── 🐍 wsgi.py
├── 📄 db.sqlite3
└── 🐍 manage.py

## 5. Hướng phát triển

- Deploy lên VPS
