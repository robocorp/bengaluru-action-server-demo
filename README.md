# Action Server in Action

## Demo @ Bengaluru, 16 Dec 2023

This repository contains implementation of a Robocorp Action Server with one action that can search a given number of books on a given topic.

The basic architecture is shown in the following image. All communications happen over standard HTTPS. The Robocorp expose service is a free-to-use reverse proxy service that allows exposing actions securely on the Internet to be consumed by AI applications.

![Action Server Demo architecture](https://github.com/robocorp/bengaluru-action-server-demo/assets/630576/7a40ddc5-ae98-4b31-b763-2a9f0d6a024e)

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

### Connect to ChatGPT

Configure the Action Server as a custom action in ChatGPT as follows. 

  - Navigate to [https://chat.openai.com/gpts/mine](https://chat.openai.com/gpts/mine)
  - Create a new GPT, e.g. BookGPT and go to the `Configure` Tab
    - Give name and description
    - Click on `Create new action`
    - **Authentication**
      - Authentication Type: API Key
      - API Key: copy-paste from Action Server output
      - Auth Type: Bearer
    - **Schema**
      - Click on `Import from URL`
      - Copy-paste URL ending with robocorp.link from Action Server output
    - Save and publish
      
    

