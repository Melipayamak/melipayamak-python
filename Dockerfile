#
# Docker build command:
# docker build --network=host -t witblack/melipayamak-python:latest -f Dockerfile .
#
# Load base image
FROM python:latest

# Install packages
RUN pip install zeep
RUN pip install requests
RUN pip install aiohttp
RUN pip install asyncio

# Copy project
COPY melipayamak-python /root/melipayamak

# Change default working directory
WORKDIR /root/melipayamak
