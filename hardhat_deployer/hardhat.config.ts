
import { HardhatUserConfig } from "hardhat/config";
import '@nomicfoundation/hardhat-verify';
import '@nomicfoundation/hardhat-toolbox';
import '@openzeppelin/hardhat-upgrades';

const config: HardhatUserConfig = {
  solidity: "0.8.28", // replace if necessary
  networks: {
    'oasees-blockchain': {
      url: 'http://10.160.3.172:8545/'
    },
  },
  etherscan: {
    apiKey: {
      'oasees-blockchain': 'empty'
    },
    customChains: [
      {
        network: "oasees-blockchain",
        chainId: 31337,
        urls: {
          apiURL: "http://10.160.3.172:8082/api",
          browserURL: "http://10.160.3.172:8082"
        }
      }
    ]
  }
};

export default config;