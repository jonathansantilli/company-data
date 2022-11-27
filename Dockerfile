FROM python:3.9 AS builder

WORKDIR /usr/src/app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY . .
RUN pip install --no-cache-dir .
RUN python3 -m pip install aiohttp


FROM python:3.9 AS test_runner
WORKDIR /tmp
COPY --from=builder /venv /venv
COPY --from=builder /usr/src/app/tests tests
ENV PATH=/venv/bin:$PATH

RUN pip install pytest
RUN python3 -m pip install aiohttp

RUN pytest tests

FROM python:3.9 AS service
WORKDIR /root/app/site-packages
COPY --from=test_runner /venv /venv
ENV PATH=/venv/bin:$PATH
