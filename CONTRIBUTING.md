# Contributing

## Development workflow

1. Create a feature branch.
2. Run checks before opening a PR:
   ```bash
   python -m unittest discover -s tests -p 'test_*.py'
   python -m compileall app tests
   ```

## Pull requests

- Keep PRs focused and small.
- Include tests for behavior changes.
- Update docs when behavior/setup changes.
