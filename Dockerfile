FROM selenium/standalone-chrome

# Install pip
RUN sudo apt-get update && sudo apt-get install -y python3-pip python3-venv

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN python3 -m pip install poetry
RUN python3 -m venv .venv
RUN python3 -m poetry install

# Start notifier service
ENTRYPOINT exec python3 $APP_HOME/foodcollector/main.py --username $USERNAME --password $PASSWORD --phone-number $PHONE
