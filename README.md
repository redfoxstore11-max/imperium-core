# Imperium Core

A lightweight, fault-tolerant execution wrapper for Python automation and API consumer tasks. Imperium Core wraps your core logic inside a resilient monitoring loop, ensuring unexpected errors don't crash your long-running processes.

## Features

- **Resilient Execution Loop**: Automatically catches unexpected exceptions and retries operations without manual intervention.
- **Fail-Safe Delay Windows**: Uses structured delay cooling periods between retries to prevent spamming APIs during downtime.
- **Zero-Dependency Core**: Pure Python with no heavy overhead or complicated database setups required for the base runner.

## How It Works

Imperium Core operates as a robust wrapper around your main task logic. Instead of letting raw network hiccups or temporary API timeouts take down your service, it isolates the failure and safely resets the execution state.

```python
Simplified conceptual view of the runner
while true:
    try:
        execute_core_task()
    except Exception as e:
        log_error(e)
        cooldown_delay()
```
## Installation
git clone https://github.com/redfoxstore11-max/imperium-core.git
cd imperium-core

## Usage
from imperium.runner import CoreRunner

def my_task():
    # Place your scraping, API requests, or automation script here
    pass

if __name__ == "__main__":
    runner = CoreRunner(task=my_task, max_retries=5)
    runner.start()
