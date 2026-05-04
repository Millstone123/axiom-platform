# Axiom — Zero-Config Deployment Platform

Deploy containerised applications to your infrastructure with zero config.

## Quick Start

```bash
git clone https://github.com/Millstone123/axiom-platform
cd axiom-platform
pip3 install -r requirements.txt
python -m axiom init
```

## Commands

| Command | Description |
|---|---|
| `python -m axiom init` | First-time setup — initialises the platform |
| `python -m axiom deploy` | Deploy your application |
| `python -m axiom status` | Show deployment status |

## Requirements

- Python 3.11+
- curl
- openssl
