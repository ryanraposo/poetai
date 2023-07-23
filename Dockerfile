FROM tensorflow/tensorflow:1.6.0
WORKDIR /app
COPY . .

RUN apt update
RUN apt-get install python-tk python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libgtk-3-dev -y

RUN pip install svgwrite
RUN pip install matplotlib
RUN pip install scipy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install awscli
RUN pip install cairosvg==1.0.22
RUN pip install Flask
RUN pip install gunicorn

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

