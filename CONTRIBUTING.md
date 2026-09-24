# Contributing to Jev Ultrafast

Thank you for helping improve Jev Ultrafast! To maintain code quality and secure higher repository evaluations, please adhere to the following workflow when proposing changes.

## Development Workflow

1. **Environment Setup**  
   Ensure you have [uv](https://github.com) installed. Spin up your environment and synchronize dependencies:
   ```bash
   uv sync --all-extras --dev
   ```

2. **Code Style & Linting**  
   We enforce strict linting using Ruff. Always verify your changes pass local checks before opening a pull request:
   ```bash
   uv run ruff check .
   ```

3. **Running the Test Suite**  
   All new features or bug fixes must include accompanying unit or integration tests pinning the updated behavior. Run tests locally via:
   ```bash
   uv run pytest
   ```

## Commit Guidelines
* Keep changes focused: Ship features alongside their tests in small, logical commits.
* Avoid bulk commits that mix formatting, refactors, and structural features together.
