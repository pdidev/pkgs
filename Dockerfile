FROM debian:stable-slim

RUN apt-get update -qy \
 && apt-get install -qy --no-install-recommends \
    apt-transport-https \
    build-essential \
    ca-certificates \
    curl \
    debian-archive-keyring \
    devscripts \
    equivs \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY local_build obs_data_gen /usr/local/bin/

RUN chmod +x /usr/local/bin/*

VOLUME /src
WORKDIR /src
ENTRYPOINT ["/usr/local/bin/local_build"]
