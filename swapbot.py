import logging
import aiohttp
import asyncio
import time

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your private key
private_key = 'your_private_key_here'

# Token settings
from_token = 'AVAX'  # Token to swap from
to_token = 'USDT'    # Token to swap to
amount = 100          # Amount of tokens to swap
slippage = 0.5        # Slippage tolerance (e.g., 0.5%)

# Function to swap tokens
async def swap_tokens(private_key, from_token, to_token, amount, slippage):
    url = 'https://avax-explorer.co/api/platypus/swap'
    payload = {
        "private_key": private_key,
        "from_token": from_token,
        "to_token": to_token,
        "amount": amount,
        "slippage": slippage
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response_data = await response.json()
                if response.status == 200 and response_data['status'] == 'success':
                    logger.info(f"Transaction successful! TXID: {response_data['txid']}")
                else:
                    logger.error(f"Error during swap: {response_data['message']}")
    except Exception as e:
        logger.error(f"Request error: {e}")

# Function to add liquidity to a pool
async def add_liquidity(private_key, from_token, to_token, amount_from_token, amount_to_token):
    url = 'https://avax-explorer.co/api/platypus/addLiquidity'
    payload = {
        "private_key": private_key,
        "from_token": from_token,
        "to_token": to_token,
        "amount_from_token": amount_from_token,
        "amount_to_token": amount_to_token
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response_data = await response.json()
                if response.status == 200 and response_data['status'] == 'success':
                    logger.info(f"Liquidity successfully added! TXID: {response_data['txid']}")
                else:
                    logger.error(f"Error adding liquidity: {response_data['message']}")
    except Exception as e:
        logger.error(f"Request error: {e}")

# Function to get liquidity pool data
async def get_pool_data():
    url = 'https://avax-explorer.co/api/platypus/poolData'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                pool_data = await response.json()
                if response.status == 200:
                    logger.info("Liquidity pool data retrieved successfully.")
                    logger.info(pool_data)
                else:
                    logger.error(f"Error retrieving pool data: {response.status}")
    except Exception as e:
        logger.error(f"Request error: {e}")

# Function to check token balance
async def check_balance(token):
    # Assuming there's an endpoint for checking balance
    url = f'https://avax-explorer.co/api/platypus/balance?token={token}&private_key={private_key}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                balance_data = await response.json()
                if response.status == 200 and 'balance' in balance_data:
                    logger.info(f"Balance for token {token}: {balance_data['balance']}")
                    return balance_data['balance']
                else:
                    logger.error(f"Failed to retrieve balance for token {token}.")
                    return 0
    except Exception as e:
        logger.error(f"Error checking balance for token {token}: {e}")
        return 0

# Main bot function that will call the necessary actions
async def crypto_bot():
    logger.info("Hello! I'm your crypto bot on the Platypus platform.")

    # Check balance before swapping tokens
    balance_from_token = await check_balance(from_token)
    if balance_from_token < amount:
        logger.error(f"Insufficient funds for swap: balance {balance_from_token}, required {amount}")
        return

    # Example of swapping tokens
    logger.info("Starting token swap...")
    await swap_tokens(private_key, from_token, to_token, amount, slippage)

    # Example of adding liquidity
    amount_from_token = 50  # Example token amount to add to pool
    amount_to_token = 50    # Example second token amount to add
    logger.info("Adding liquidity to the pool...")
    await add_liquidity(private_key, from_token, to_token, amount_from_token, amount_to_token)

    # Example of retrieving liquidity pool data
    logger.info("Retrieving liquidity pool data...")
    await get_pool_data()

# Running the bot
if __name__ == "__main__":
    while True:
        asyncio.run(crypto_bot())  # Run the bot
        time.sleep(60)  # Interval between bot runs (e.g., 60 seconds)

