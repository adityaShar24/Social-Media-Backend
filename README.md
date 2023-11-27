# Social-Media Flask Application - A Social Networking Platform 

A Flask-based web application for managing user accounts, friend requests, and interactions.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Features

- User Registration and Authentication: Users can create accounts, log in, and securely manage their profiles.

- Friendship System: Users can send friend requests, accept or reject requests, and manage their friends list.

- Post System: Users can create posts and save someone else's posts.

- Comment System: Users can comment on each other's post and reply to thatv comment. 

- Chat Room: Users can create a room to chat and send messages in that room.

- Customizable: SocialBond is highly customizable, allowing you to add new features or modify existing ones to suit your needs.

## Technology Stack
- Backend: Python, Flask, MongoDB

- Database: MongoDB

- Authentication: JSON Web Tokens (JWT)

- Flask-SocketIO: For real-time communication


## Getting Started

These instructions will help you set up and run the SocialBond Flask Application on your local machine.

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- MongoDB (Make sure you have a MongoDB instance running and the connection string configured)

### Installation

To run this project, you'll need to set up a Python environment and install its dependencies. Here's how you can do it:

1. **Clone the Repository**

   ```shell
   https://github.com/adityaShar24/Social-Bond.git

1. **Change Directory**

   ```shell
    cd social-media-flask


### Usage
- To run the Social-Media Flask Application, execute the following command:
- python app.py


### API Endpoints

##### The SocialBond Flask Application provides the following API endpoints:

- Register User: POST /register
- Login User: POST /login
- Make Friend Request: POST /make-request
- Remove Friend Request: DELETE /remove-request
- Accept Friend Request: POST /accept-request
- Reject Friend Request: POST /reject-request
- Create Post: POST /post
- Comment on Post: POST /comment
- Create Chat Room: POST /create-room
- Send Message in Room: POST /send-message


### Contributing

Contributions are welcome! 

If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


