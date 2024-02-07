# Dummy Order Management CLI Application Example

This repository contains a Python-based CLI (Command-Line Interface) application designed to manage orders within a system, showcasing the implementation of a "Create Order" use case. The application is developed following the principles of Domain-Driven Design (DDD) and the Hexagonal Architecture pattern to ensure clean separation of concerns, flexibility, and ease of maintenance.

## Features

- **Create Order**: Users can create new orders by specifying customer details and product information.
- **Hexagonal Architecture**: Ensures a clean separation between the application's core logic and external concerns like the user interface and data storage.
- **Domain-Driven Design**: Focuses on the core domain logic, making the system more understandable and flexible to changes in business requirements.
- **CLI Interface**: Provides a simple and intuitive command-line interface for interacting with the application.

## Architecture Overview

This application is structured according to Hexagonal Architecture, also known as Ports and Adapters Architecture. The main components are:

- **Domain**: Contains the core business logic and entities such as `Order`, `Customer`, and `Product`.
- **Application**: Houses the application services that orchestrate the execution of domain logic.
- **Adapters**: Includes adapters for the CLI (primary adapter) and for data storage (secondary adapters).

## Project Structure

- `/domain` - Domain entities and logic.
- `/application` - Application services.
- `/adapters` - CLI and database adapters.
- `main.py` - Entry point for the CLI application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hexagonal Architecture and Domain-Driven Design advocates for inspiring the structure and design of this application.

Feel free to modify the README according to the specific details of your project, such as the repository URL, additional features, and detailed usage instructions.