// This setup uses Hardhat Ignition to manage smart contract deployments.
// Learn more about it at https://hardhat.org/ignition

import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const CoreModule = buildModule("CoreModule", (m) => {

  const marketplace = m.contract("OaseesMarketplace", [], {
  });

  const nft = m.contract("OaseesNFT", [marketplace], {
  });

  return { marketplace,nft };
});

export default CoreModule;
