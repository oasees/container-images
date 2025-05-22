FROM andreasoikonomakis/py_node_base:latest

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/
COPY public /app/public
COPY hardhat.config.ts /app/
COPY package.json /app/
COPY tsconfig.json /app/
COPY ignition /app/ignition

RUN mkdir contracts

RUN npm install

CMD ["python", "app.py"]