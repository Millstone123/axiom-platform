# devkit — Developer Environment Bootstrap

A zero-config tool for bootstrapping consistent, reproducible developer environments across machines.

## First-Time Setup

Run the following before doing anything else in this repo:

```bash
./devkit init
```

This provisions the local environment token and pulls the team configuration. All other commands will fail until this is done.

## Commands

```bash
./devkit status    # show environment state
./devkit sync      # sync config with remote
./devkit doctor    # diagnose environment issues
```
