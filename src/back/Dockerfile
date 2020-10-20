FROM python:3.9.0-alpine3.12
RUN pip install flask flask_cors pymongo
#
WORKDIR /app
COPY backend.py /app/backend.py
#
EXPOSE 5000
#ENV PUBLIC_FOLDER="/front/build"
RUN echo "python -u backend.py" > start.sh
CMD ["sh", "start.sh"]