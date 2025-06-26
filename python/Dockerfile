# ベースイメージ
FROM python:3.9-slim
USER root

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config -y
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y nano less
# pipをアップグレード
RUN pip install --upgrade pip

# Pythonパッケージの要件ファイルをコピー
COPY requirements.txt .

# RUN pip install pandas numpy matplotlib mysql mysql-connector-python flask networkx
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

# 作業ディレクトリ作成
WORKDIR /workdir

# 追加---
RUN apt-get install xxd
# ---

EXPOSE 8080
#CMD /bin/bash 
