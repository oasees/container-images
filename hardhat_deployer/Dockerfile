FROM node:22-alpine

WORKDIR /hardhat

COPY hardhat.config.ts /hardhat/
COPY package.json /hardhat/
COPY tsconfig.json /hardhat/
COPY ignition /hardhat/ignition
COPY contracts /hardhat/contracts
RUN npm install

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]