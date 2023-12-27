FROM ubuntu:latest
LABEL authors="artem"

ENTRYPOINT ["top", "-b"]