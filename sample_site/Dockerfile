# docker for django app running env.

FROM ubuntu:18.04

ENV PYTHONUNBUFFERD 1
ENV PYTHONIOENCODING

ENV HOME /root
ENV DEPLoY_DIR ${HOME}/sample_site

RUN apt update

# set locale
# https://stackoverflow.com/a/28406007
RUN apt install -y locales
RUN sed -i -e "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/" /etc/locale.gen \
    && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install Python 3.9
RUN apt install -y wget \
    build-essential \
    zlib1g-dev \
    # https://stackoverflow.com/a/43923402
    libssl-dev \
    # https://stackoverflow.com/a/29862854
    libsqlite3-dev
WORKDIR ${HOME}
RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz \
    && tar zxf Python-3.9.1.tgz \
    && cd Python-3.9.1 \
    && ./configure --enable-optimizations \
    && make altinstall

# Set alias
RUN update-alternatives --install /usr/local/bin/python3 python3 /usr/local/bin/python3.9 1
RUN update-alternatives --install /usr/local/bin/pip3 pip3 /usr/local/bin/pip3.9 1
RUN pip3 install -U pip

# Install other requisites
RUN apt install -y vim
# MySQL (option)
# https://stackoverflow.com/a/25682993
RUN apt install -y libmysqlclient-dev
# SQLite (option)
RUN apt install -y sqlite3

RUN mkdir -p ${DEPLOY_DIR}
WORKDIR ${DEPLOY_DIR}

# Install packages for project
ADD requirements/base.txt requirements/base.txt
RUN pip3 install -r requirements/base.txt

# Set entrypoint
ENTRYPOINT ["/bin/bash", "scripts/init_mysite.sh"]

