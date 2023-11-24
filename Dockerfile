FROM tensorflow/tensorflow:2.2.0

# Set up the working directory
WORKDIR /rasa_app

# Copy the project files to the working directory
COPY . .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install the project dependencies
RUN pip install -r requirements.txt

# Download the English language model for spaCy
RUN python -m spacy download en

# Install Rasa and Sanic
RUN pip install rasa==2.1.2 sanic==19.9.0
