# Moonshine
**Game during the day, mine cryptocurrencies at night. Automatically and seamlessly.**
 
 The script detects when a game is opened, and will disable your cryptocurrency miner, and set gaming overclocks/fans for an optimal gaming experience. When the game is closed, the miner overclocks/fans are reapplied and the cryptocurrency miner is resumed seamlessly.
 
# I do NOT support buying gaming GPU's to solely mine. This script is meant for gamers who already own GPU's to make a solid income with their silicon. 

# Intro

At current prices, your GPU can generate thousands of dollars of effort-free income every year. 
Though I can only give a rough estimate with cards I have personally tested, you can refer to the chart below for some context.
# 
GPU | "MSRP" | Income (monthly, USD) | Income (yearly, USD) | Return on Investment Yearly (MSRP!)
--- | --- | --- | --- | --- |
RX 580 8GB | "$175" | $77.775 | $933.3 | 433%
RTX 3060ti 8GB | "$399" | $165.92 | $1991.04 | 399%
RTX 3080 10GB | "$699" | $261.385 | $3136.62 | 348%
#
Due to the fact gamers aren't playing video games 24/7, you can start mining automatically with your downtime (even while using your PC for other work/school!) and generate thousands of dollars per year. 

**The more we mine, the more money we take away from huge-scale mining operations that eat GPUs from gamers! And we make cash in the process!**

# Setting up the miner

You will need to setup your miner to run from a batch file. 

If you don't know how to setup a miner, you basically need to find a mining pool, a cryptocurrency mining program, and a wallet to store your payouts.

[Son of a Tech has a great guide](https://www.youtube.com/watch?v=xqny5SSFRTo&ab_channel=SonofaTech) using lolMiner as the mining program, Metamask as the wallet, and Ethermine.org as the pool.


# Overclocking

If you aren't overclocking your card when mining, you're throwing away money through your power bill and profits alike. Advanced guides are easily found online, but for a reference, a list of NVIDIA/AMD cards and their "most common" overclocks with respective expected hashrates are shown below.

# NVIDIA

Model |	Core Clock Delta	| Memory Clock Delta	| Power Limit (W)	| Expected Performance (DaggerHashimoto)
--- | --- | --- | --- | --- |
RTX 3090|-300|+1000|285W|120 MH/s
RTX 3080|-150|+900|220W|98 MH/s
RTX 3070|-500|+1100|130W|60 MH/s
RTX 3060ti|-500|+1200|130W|60 MH/s
RTX 2080ti|-200|+1100|150W|57 MH/s
RTX 2080 Super|-50|+1000|175W|42 MH/s
RTX 2080|-50|+800|155W|42 MH/s
RTX 2070 Super|-50|+800|150W|40 MH/s
RTX 2070|-50|+800|125W|39 MH/s
RTX 2060 Super|-50|+850|125W|39 MH/s
RTX 2060|-50|+700|115W|31 MH/s
GTX 1660ti|-200|+900|70W|30 MH/s
GTX 1660 Super|-200|+900|70W|30 MH/s
GTX 1660|-200|+600|60W|24 MH/s
GTX 1080ti|0|+750|185W|45 MH/s
GTX 1080|0|+700|135W|37 MH/s
GTX 1070ti|0|+500|135W|30 MH/s
GTX 1070|0|+450|115W|30 MH/s
GTX 1060 6GB|0|+900|80W|23 MH/s
 
# AMD

Model |	Core Clock	|	Memory Clock |	Core Voltage (mV)	|	Expected Performance
--- | --- | --- | --- | --- |
RX 6900 XT* |	1300 |	2100 |	850 |	64 MH/s
RX 6800 XT* |	1500 |	2150 |	900 |	64 MH/s
RX 6800* |	1500 |	2100 | 1025 |	63 MH/s
RX 5700 XT |	1300 |	1800 or 900* |	800 |	55 MH/s
RX 5700 |	1300 |	1800 or 900* |	900 |	54 MH/s
RX 5600XT |	1300 |	1850 or 925* |	750 |	39 MH/s
Radeon VII |	1550 |	1050 |	880 |	90 MH/s
RX Vega 64 |	1000 |	1050 |	850 |	47 MH/s
RX Vega 56 |	950 |	900 |	850 |	43 MH/s
RX 580 8GB |	1175 |	2150 |	850 |	31 MH/s
RX 570 8GB |	1150 |	2050 |	870 |	30 MH/s
RX 480 8GB |	1150 |	2150 |	900 |	31 MH/s
RX 470 8GB |	1150 |	2000 |	900 |	30 MH/s

*Enabling Fast timings in AMD Radeon Software for 6000 series is recommended. 

*RX 5000 series values might be x2 in some overclocking tools.

Bios modding is required for most RX series cards to achieve the performance numbers stated in the above table.

#

One you've figured out your **MINING** overclock and fan curves, save it as your **1st profile** on Afterburner. This will automatically set when mining.

Your **GAMING** overclock and fan curves (or stock settings) should be saved as the **2nd profile** on Afterburner.

# Setup

In the [script](Moonshine.py), there are five editable values.

**"MiningBatchFileLocation"** contains the path of the batch file for your cryptocurrency miner. You MUST change this path to your own cryptocurrency miner's batch file path.

**"GameExecutableNames"** contains a list of game executable names. If the script doesn't detect one of your games, add the executable name to this list. Be careful, as the script checks if there is any match between a process on your PC and the entry in the list. If you'd enter a game as "Wizard" instead of a more specific ("WizardyGame") or executable ("WizardyGame.exe") name, some program like an install wizard might interfere and wrongly suspend your miner. Entries are not case-sensitive.

**"AfterburnerExecutableLocation"** contains the path to the Afterburner executable. If you don't have Afterburner installed in the default directory, change this value to the correct path.

**"UseAfterburner"** is set to True by default. Set to False if you don't want the script to use Afterburner.

**"CheckInterval"** is how long seconds to wait between scans. Default is 3, but most computers should be easily able to handle 1 if you don't have an absurd amount of tasks open.

# Usage

1. Download the Python [script](Moonshine.py) and install dependencies from requirements.txt .


2. Ensure your overclock for (profile 1: mining) and (profile 2: gaming) are set in Afterburner. If not using afterburner, set "UseAfterburner = True" to "UseAfterburner = False" in the python script.


3. Ensure all the games you play are listed in "GameExecutableNames". If not, find and add each game's executable name to the list.


4. Copy the Python script over to your startup folder, at 
"C:\Users\YourUserName\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup", replacing "YourUserName" with your PC's user name.


5. Run the script.























