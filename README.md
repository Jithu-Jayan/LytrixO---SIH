# LytrixO

### A Digital Platform Connecting Farmers, Buyers & Agricultural Workers

LytrixO is a web-based agricultural platform designed to create a connected ecosystem between **farmers, buyers, and labourers**. The platform provides dedicated interfaces for different user roles while using a centralized backend and database to manage and exchange application data.

The project was developed as part of the **Smart India Hackathon (SIH)** with the goal of building a practical digital solution for improving communication, accessibility, and collaboration within the agricultural ecosystem.

---

## Overview

The agricultural ecosystem often involves multiple stakeholders operating independently. Farmers need access to markets and workers, buyers need access to agricultural products, and labourers need opportunities that match their skills and availability.

LytrixO aims to bring these interactions into a single digital platform.

### The platform provides dedicated experiences for:

* **Farmers** — Manage agricultural activities, explore markets, deals, profiles and relevant services.
* **Buyers** — Interact with available agricultural products and connect with farmers.
* **Labourers** — Discover opportunities, deals and agricultural work.
* **Users** — Access the platform through a centralized authentication interface.

The application follows a layered architecture in which the frontend communicates with the backend, while the backend manages communication with the database.

---

## Key Features

### Farmer Module

* Farmer-focused dashboard
* Market interface
* Deals and opportunities
* Profile management
* Help and support interface

### Buyer Module

* Buyer dashboard
* Product/market interaction
* Farmer-facing marketplace functionality
* User profile and platform interaction

### Labourer Module

* Labourer dashboard
* Market and opportunity interface
* Deals section
* Profile management
* Help and support

### Authentication

* Centralized login interface
* Role-based entry points
* Foundation for user authentication and authorization

### Full-Stack Integration

* Frontend interfaces connected with backend services
* Backend connected with the application database
* Data flow established between the three major application layers
* Database connectivity tested through the backend

---

## System Architecture

```text
                    ┌──────────────────────┐
                    │       USERS          │
                    │                      │
                    │ Farmer | Buyer       │
                    │ Labourer | Admin     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FRONTEND        │
                    │                      │
                    │ HTML / CSS / JS      │
                    │ Role-based Pages     │
                    └──────────┬───────────┘
                               │
                         API / HTTP
                               │
                               ▼
                    ┌──────────────────────┐
                    │       BACKEND        │
                    │                      │
                    │ API Layer            │
                    │ Business Logic       │
                    │ Database Services     │
                    └──────────┬───────────┘
                               │
                        Database Queries
                               │
                               ▼
                    ┌──────────────────────┐
                    │      DATABASE        │
                    │                      │
                    │ Application Data     │
                    │ User Data            │
                    │ Platform Data        │
                    └──────────────────────┘
```

---

## Tech Stack

| Layer             | Technologies                       |
| ----------------- | ---------------------------------- |
| Frontend          | HTML, CSS, JavaScript              |
| Backend           | Python                             |
| Database          | MongoDB                            |
| API / Integration | Backend API layer                  |
| Development       | Git, GitHub                        |
| Testing           | Python database connection testing |

---

## Project Structure

```text
LytrixO---SIH/
│
├── app/
│   └── Backend & database integration
│
├── buyerspage.html
│
├── farmerspage.html
├── farmerspage_deals.html
├── farmerspage_help.html
├── farmerspage_market.html
├── farmerspage_profile.html
│
├── labourerpage.html
├── labourerpage_deals.html
├── labourerpage_help.html
├── labourerpage_market.html
├── labourerpage_profile.html
│
├── login.html
├── teamspage.html
│
├── test_connection.py
│
└── README.md
```

---

## Application Flow

The application is designed around a simple full-stack data flow:

```text
User Interaction
       ↓
Frontend Interface
       ↓
Backend API
       ↓
Database
       ↓
Backend Response
       ↓
Frontend
       ↓
User
```

This architecture allows the frontend interfaces to remain separate from the application's business and data logic while providing a structured way for information to move through the system.

---

## My Role

### Jithu Jayan — Full-Stack Integration

I worked on the **integration layer of the application**, connecting the frontend interfaces with the backend and establishing the connection between the backend and database.

My primary responsibilities included:

* Connecting the frontend interfaces with the backend services.
* Establishing the communication flow between frontend requests and backend processing.
* Integrating the backend with the database.
* Configuring and testing database connectivity.
* Working on the data flow between the frontend, backend, and database.
* Debugging integration issues across different layers of the application.
* Testing the complete **Frontend → Backend → Database** workflow.

The focus of my contribution was to ensure that the independently developed application components could work together as a single full-stack system.

```text
Frontend
   │
   │ Requests
   ▼
Backend
   │
   │ Database Operations
   ▼
Database
   │
   │ Response
   ▼
Backend
   │
   ▼
Frontend
```

---

## Database Connectivity

The repository includes a dedicated database connection test to verify communication between the backend and database layer.

The connection workflow was tested before integrating database-dependent functionality into the application.

This helped establish the foundation for persistent data storage and backend-driven application functionality.

---

## Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.x
* Git
* A MongoDB database
* A modern web browser

### Clone the Repository

```bash
git clone https://github.com/Jithu-Jayan/LytrixO---SIH.git
cd LytrixO---SIH
```

### Backend Setup

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Configure the required database connection settings in the backend environment/configuration.

### Test Database Connection

```bash
python test_connection.py
```

If the connection is configured correctly, the backend should be able to communicate with the database successfully.

### Run the Frontend

Open the required HTML page in a browser or serve the project through a local development server.

---

## Development Workflow

The project was developed using a modular workflow where different parts of the platform could be developed and integrated independently.

```text
UI Development
      ↓
Frontend Integration
      ↓
Backend Integration
      ↓
Database Connection
      ↓
End-to-End Testing
```

This approach allowed the team to identify and resolve integration issues while bringing the different modules together.

---

## Future Improvements

* Implement complete role-based authentication and authorization.
* Expand REST API coverage.
* Implement complete CRUD operations for application data.
* Improve database schema and data validation.
* Add secure environment-variable management.
* Add API documentation.
* Improve frontend responsiveness and accessibility.
* Deploy the complete application to a production environment.
* Add automated testing and CI/CD.

---

## Contributors

Developed as a team project for **Smart India Hackathon (SIH)**.

| Contributor     | Responsibility                                           |
| --------------- | -------------------------------------------------------- |
| **Jithu Jayan** | Frontend–Backend Integration & Database Integration      |
| Team Members    | Frontend, Backend, UI/UX, Research & Project Development |

---

## Project Status

**Prototype / Hackathon Project**

The project is under active development, with the current implementation focused on establishing the core frontend, backend, and database architecture.

---

## License

This project was developed for educational and hackathon purposes as part of the **Smart India Hackathon**.

---

## Acknowledgements

* **Smart India Hackathon** for providing the problem-solving platform.
* **Lovely Professional University** for supporting the project development.
* All team members who contributed to the design, development, research, and integration of LytrixO.
