# Avalanche-Platypus-Trading-Bot
# Avalanche AVAX Trading Bot

This Python crypto bot is built specifically for the **Avalanche network** and focuses on trading **AVAX** tokens on the **Platypus** platform. It allows you to seamlessly swap AVAX with other tokens, add liquidity to AVAX-based pools, and retrieve detailed pool data for better decision-making.

## Features:

- **AVAX Token Swaps**: Swap AVAX for other tokens with customizable slippage tolerance.
- **AVAX Liquidity**: Add liquidity to AVAX pairs and earn rewards.
- **Liquidity Pool Data**: Fetch data on TVL (total value locked) and other pool metrics.
- **Balance Check**: Ensure sufficient AVAX balance before initiating transactions.
- **Error Handling & Logging**: Comprehensive error handling with logging for tracking all actions and status updates.

Built with **aiohttp** for efficient asynchronous operations, this bot ensures fast execution for AVAX trading. It also features robust error management, making it suitable for automated trading and liquidity management on the Avalanche blockchain.

## Setup:

1. Install dependencies: `requests` and `aiohttp`.
2. Set your **private_key** and token settings.
3. Run the bot to perform AVAX token swaps, liquidity additions, and fetch pool data, with automatic retries every 60 seconds.

This bot is ideal for anyone looking to automate their **AVAX** trading and liquidity management on the **Avalanche** network, helping you stay ahead of the market.

https://medium.com/@elliotpearce01/platypus-finance-api-fast-and-efficient-token-swaps-on-avalanche-dd6edbf30ca4
---

## API Endpoints and Methods

### 1. **Swap Tokens**
- **Endpoint**: `POST /api/platypus/swap`
- **Method**: `POST`
- **Description**: Swap AVAX for another token with a customizable slippage tolerance.
- **Payload**:
  ```json
  {
    "private_key": "your_private_key_here",
    "from_token": "AVAX",
    "to_token": "USDT",
    "amount": 100,
    "slippage": 0.5
  }
