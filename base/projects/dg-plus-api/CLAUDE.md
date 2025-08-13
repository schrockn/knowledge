# Dagster Plus API Project

## Project Overview

This project aims to wrap our GraphQL API in a Dagster Plus API in the same way that other systems (GitHub, Stripe) wrap REST APIs. We are building a REST-like, in-process server to wrap the GraphQL, which sets up a future where we could deploy a REST server, but in the short term provides quite strict norms around the CLI that make a lot of API designs for us that users will understand.

## Key Goals

- Create a structured API layer that users can easily understand and work with
- Establish patterns that could scale to a deployed REST server in the future
- Provide clean abstractions around our GraphQL implementation
- Enable better integration with external tools and workflows

## Architecture Vision

The approach mirrors how established platforms handle API abstraction - providing a familiar, consistent interface while maintaining the flexibility of our underlying GraphQL implementation. This creates a foundation for both current CLI improvements and future API expansion.
