# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM selenium/standalone-chrome

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install poetry && poetry install

# Start notifier service
CMD exec python foodcollector/main.py --username $USERNAME --password $PASSWORD --phone-number $PHONE
