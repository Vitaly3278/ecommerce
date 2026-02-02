# # Один ко многим
# from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
# from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
# from datetime import datetime
#
# class Base(DeclarativeBase):
#     pass
#
# class Author(Base):
#     __tablename__ = "authors"
#     id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
#     name :Mapped [str] = Column(String(100), nullable=False)
#     books = relationship("Book", back_populates="author")
#
# class Book(Base):
#     __tablename__ = "books"
#     id : Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
#     title : Mapped[str] = Column(String(200), nullable=False)
#     author_id : Mapped[int] = Column(Integer, ForeignKey("authors.id"), nullable=False)
#     author = relationship("Author", back_populates="books")

# ------------------------------------------------------------------------------------

# # Один к одному
# from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
# from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
#
#
# class Base(DeclarativeBase):
#     pass
#
# class User(Base):
#     __tablename__ = "users"
#     id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     username: Mapped[str] = mapped_column(String(50), unique=True ,nullable=False)
#     profile: Mapped['Profile'] = relationship("Profile", back_populates="user", uselist=False, cascade='all, delete-orphan')
#
# class Profile(Base):
#     __tablename__ = "profiles"
#     id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
#     bio : Mapped[str] = mapped_column(Text, nullable=True)
#     user : Mapped[User] = relationship("User", back_populates="profile")

#----------------------------------------------------------------------------------------
# Один ко многим
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, Numeric
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy.testing.pickleable import Order


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"
    id : Mapped[int]= mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(50), nullable=False)
    product : Mapped[list['Product']] = relationship("Product", back_populates="category",  cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = "products"
    id : Mapped [int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(150), nullable=False)
    price : Mapped[float] = mapped_column(Numeric(10, 2),nullable=False)
    category_id : Mapped[int] = mapped_column(Integer, ForeignKey(Category.id), nullable=False)
    category : Mapped ['Category'] = relationship("Category", back_populates="product")

# ------------------------------------------------------------------------------------------------
# Один ко многим
# from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, Numeric
# from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
#
#
# class Base(DeclarativeBase):
#     pass
#
# class Customer(Base):
#     __tablename__ = "customers"
#     id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name : Mapped[str] = mapped_column(String(100), nullable=False)
#     email : Mapped[str] = mapped_column(String(120), unique=True, nullable=False )
#     order : Mapped[list['Order']] = relationship("Order", back_populates="customer", cascade="all, delete-orphan")
#
# class Order(Base):
#     __tablename__ = "orders"
#     id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     order_number : Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
#     total_amount : Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
#     customer_id : Mapped[int] = mapped_column(Integer, ForeignKey(Customer.id), nullable=False)
#     customer : Mapped[Customer] = relationship("Customer", back_populates="order")

# ------------------------------------------------------------------------------------------------
# Один ко многим
# from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, Numeric
# from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
#
#
# class Base(DeclarativeBase):
#     pass
#
# class Student(Base):
#     __tablename__ = "students"
#     id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name : Mapped[str] = mapped_column(String(100), nullable=False)
#     student_number : Mapped[str] = mapped_column(String(20),unique=True, nullable=False)
#     grade : Mapped[list['Grade']] = relationship("Grade", back_populates="student", cascade="all, delete-orphan")
#
# class Grade(Base):
#     __tablename__ = "grades"
#     id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     value : Mapped [int] = mapped_column(Integer,nullable=False)
#     subject : Mapped [str] = mapped_column(String(50),nullable=False)
#     student_id : Mapped[int] = mapped_column(Integer, ForeignKey(Student.id), nullable=False)
#     student : Mapped ['Student'] = relationship("Student", back_populates="grade")
 #-----------------------------------------------------------------------------------------

# Многие к многим

# from sqlalchemy import Column, Integer, String, Date, ForeignKey
# from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# class Participation(Base):
#     __tablename__ = "participations"
#
#     project_id: Mapped[int] = mapped_column(
#         ForeignKey("projects.id", ondelete='CASCADE'),
#         primary_key=True
#     )
#     employee_id: Mapped[int] = mapped_column(
#         ForeignKey("employees.id", ondelete='CASCADE'),
#         primary_key=True
#     )
#     role: Mapped[str] = mapped_column(String(50), nullable=False)
#
#     project: Mapped['Project'] = relationship("Project", back_populates="participations")
#     employee: Mapped['Employee'] = relationship("Employee", back_populates="participations")
#
#
# class Project(Base):
#     __tablename__ = "projects"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
#     start_date: Mapped[Date] = mapped_column(Date, nullable=False)
#
#     participations: Mapped[list['Participation']] = relationship(
#         "Participation",
#         back_populates="project",
#         cascade="all, delete-orphan"
#     )
#
#
# class Employee(Base):
#     __tablename__ = "employees"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(100), nullable=False)
#     email: Mapped[str] = mapped_column(
#         String(120),
#         unique=True,
#         nullable=False,
#         index=True
#     )
#
#     participations: Mapped[list['Participation']] = relationship(
#         "Participation",
#         back_populates="employee",
#         cascade="all, delete-orphan"
#     )