# 🚀 FastAPI & MongoDB CRUD Application

A production-ready, asynchronous RESTful API built using **FastAPI** and **MongoDB** (Motor / PyMongo). This project demonstrates a complete, modular CRUD (Create, Read, Update, Delete) workflow with structured data validation, environment configuration, and clean folder architecture.

---

## ✨ Features

- ⚡ **High Performance:** Asynchronous endpoints powered by FastAPI and Uvicorn.
- 🍃 **NoSQL Persistence:** Seamless data storage and retrieval with MongoDB.
- 🔄 **Complete CRUD Operations:** Endpoints to Create, Read, Update, and Delete documents.
- 📐 **Modular Architecture:** Clean separation of concerns using `routes`, `models`, `schemas`, `database`, `config`, and `utils`.
- 🛡️ **Data Validation:** Strict request and response schemas using Pydantic.
- 🔐 **Environment Management:** Secure credential management via `.env`.
- 📖 **Interactive API Docs:** Automatic Swagger UI (`/docs`) and ReDoc (`/redoc`) documentation.

---

## 📁 Repository Structure

```text
fastapi_mongodb_rep/
├── config/           # Configuration files & environment variable loaders
├── database/         # Database connection setup & client initialization
├── dependencies/     # Reusable dependency functions (e.g., DB session injection)
├── models/           # MongoDB database models/entities
├── routes/           # API router handlers (CRUD endpoints)
├── schemas/          # Pydantic schemas for data validation & serialization
├── utils/            # Helper functions and utility modules
├── .env              # Environment variables (DB URIs, secrets)
├── .gitignore        # Git ignore rules
└── .python-version   # Python runtime configuration
