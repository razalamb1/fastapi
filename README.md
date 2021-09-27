[![Python 3.8](https://github.com/razalamb1/fastapi/actions/workflows/main.yml/badge.svg)](https://github.com/razalamb1/fastapi/actions/workflows/main.yml)
# Password Generator Microservice
This is a FastAPI Microservice that generates a random password when prompted with a length. The password will contain at least one uppercase letter, special character, and number.

This Microservice was developed entirely in Amazon's CloudShell, and was deployed using AWS AppRunner. Promted with the path `generate/{length(int)}`, the Microservice returns a JSON payload containing a randomly generated password. The server is set up to deploy changes on build (Continuous Delivery) and is also continuously integrated with GitHub actions. On every "push," the code is linted and tested before being integrated.
