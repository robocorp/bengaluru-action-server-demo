# Action Server in Action

## Demo @ Bengaluru, 16 Dec 2023

This repository contains setup of a Robocorp Action Server with one action that is able to search a given number of books on a given topic.

## Setup

### Prerequisites
 - Works on Linux/Windows/Mac
 - [install RCC](https://github.com/robocorp/rcc?tab=readme-ov-file#installing-rcc-from-command-line), a Robocorp open-source tool for Python environment management
   - packages are available for `pip install` but RCC greatly simplifies the dependency handling by isolating environments

### Starting Action Server

Note! The actions are exposed on Internet, secured with an API key. This enables connecting the actions easily to ChatGPT. Remove the `--expose` option in `robot.yaml` to offer the service only on `localhost`.

Start action server with `rcc run` in the repository root directory and note the following from its output
  - Local web interface: *Uvicorn running on http://localhost:8080*. Use this to start actions and view runs.
  - Public URL for connecting to e.g. ChatGPT or Remark: *URL: https://a-random-host-name.robocorp.link*
  - API key for authorization: *Add following header api authorization header to run actions: { "Authorization": "Bearer API_KEY_HERE" }*

### Experiment locally

Navigate to URL printed during start (typically http://localhost:8080). `Action Packages` page shows the configured actions and allows to test them locally. `Action Runs` page shows the previous runs and provides a live view to the activity.

