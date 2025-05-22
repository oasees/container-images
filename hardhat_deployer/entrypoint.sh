#!/bin/sh
npx hardhat ignition deploy ./ignition/modules/Core.ts --network oasees-blockchain --deployment-id oasees-marketplace
sleep 5
npx hardhat ignition verify oasees-marketplace