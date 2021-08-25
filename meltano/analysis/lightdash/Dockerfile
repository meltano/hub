FROM lightdash/lightdash:latest

# TODO: Add any custom image prep here.

ENV PIP=/usr/local/venv/bin/pip

RUN dbt --version
RUN $PIP uninstall -y dbt dbt-core
RUN $PIP install git+https://github.com/Tomme/dbt-athena.git
RUN dbt --version
