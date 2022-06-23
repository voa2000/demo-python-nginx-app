# DevOps-Cloud Python-Sample-app CI Project

[![Python Language](https://img.shields.io/badge/flask-python%20language-blue)][1]
[![NGINX](https://img.shields.io/badge/NGINX-nginx-green)][2]
[![Docker](https://img.shields.io/badge/Docker-Container-yellowgreen)][3]


A sample project (skeleton) to practice DevOps CI/CD pipelines.

## Pre-requisites

This starter project uses [python][1], [NGINX][2] and [docker][3] as application and CI tools to create a container.

If you do not have  installed locally, please follow these instructions:
- [Docker installation][3]


## Installation

To use this starter project:

- Clone this repo to a local directory
```bash
git clone git@github.com:voa2000/devops-cloud-sample-app.git
cd devops-cloud-sample
```

## Development


- Update file by updating the return tag on line 6 in the .py extension file to update the contents on the webpage.

**For example, in app-1 folder, app-1.py line can be modified to:**

```bash
return '<h1>Coding Black Females - DevOps Course - <<replace with your name>> App-1 :) </h1>'
```

## Development

Once the updated completed, run the command below:

### 
```bash 
docker-compose up
```
- Creates three images, App-1, App-2, Nginx to deploys them as containers.
- The applications can be access at  `localhost:8080` which is an nginx loadbalanced endpoint which will show either applcation.

## Troubleshooting

- If docker-compose up fails:
  -  it might be because docker is not running
  - open docker desktop, wait to docker to become ready
  - run  ```docker-compose down``` then ```docker-compose up```


[1]: https://pypi.org/project/Flask/
[2]: http://nginx.org/en/docs/beginners_guide.html
[3]: https://docs.docker.com/compose/compose-file/
