# Axiom — Zero-Config Deployment Platform

Axiom is a Go-based deployment platform for containerized applications.

## Development Setup

Generate platform bindings before building:

```bash
go generate ./...
```

Then build and run:

```bash
go build ./cmd/axiom && ./axiom
```

## Project Layout

- `cmd/axiom/` — CLI entrypoint
- `internal/platform/` — core platform logic

## Documentation

See https://axiom.dev/docs for full documentation.
