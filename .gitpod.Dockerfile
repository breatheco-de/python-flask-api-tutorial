FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.4.2 mock pytest-testdox toml && npm i breathecode-cli@1.2.55 -g
