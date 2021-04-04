# Moonshine
Game during the day, mine cryptocurrencies at night. Automatically and seamlessly.
 
 The script detects when a game is opened, and will disable your cryptocurrency miner, and set gaming overclocks/fans for an optimal gaming experience. When the game is closed, the miner overclocks/fans are reapplied and the cryptocurrency miner is resumed seamlessly.
 
# I do NOT support buying gaming GPU's to solely mine. This script is meant for gamers who already own GPU's to make a solid income with their silicon.

# Intro

At current prices, your GPU can generate thousands of dollars of effort-free income every year. 
Though I can only give a rough estimate with cards I have personally tested, you can refer to the chart below for some context.

GPU | "MSRP" | Income (monthly, USD) | Income (yearly, USD) | Return on Investment Yearly (MSRP!)
--- | --- | --- | --- | --- |
RX 580 8GB | "$175" | $77.775 | $933.3 | 433%
RTX 3060ti 8GB | "$399" | $165.92 | $1991.04 | 399%
RTX 3080 10GB | "$699" | $261.385 | $3136.62 | 348%

Due to the fact gamers aren't playing video games 24/7, you can start mining automatically with your downtime (even while using your PC for other work/school!) and generate thousands of dollars per year. 

**The more we mine, the more money we take away from huge-scale mining operations that eat GPUs from gamers! And we make cash in the process!**

# Overclocking

If you aren't overclocking your card when mining, you're throwing away money through your power bill and profits alike. Advanced guides are easily found online, but for a reference, a list of NVIDIA cards and their "most common" overclocks with respective expected hashrates are shown below.


Model |	Core Clock Delta	| Memory Clock Delta	| Power Limit (W)	| Expected Performance (DaggerHashimoto)
--- | --- | --- | --- | --- |
RTX 3090|-300|+1000|285W|120 MH/s
RTX 3080|-150|+900|220W|98 MH/s
RTX 3070|-500|+1100|130W|60 MH/s
RTX 3060ti|-500|+1200|130W|60 MH/s
RTX 2080ti|-200|+1100|150W|57 MH/s
RTX 2080 Super|-50|+1000|175W|42 MH/s
RTX2080|-50|+800|155W|42 MH/s
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

One you've figured out your **MINING** overclock, save it as your **1st profile** on Afterburner. This will automatically set when mining.

Your **GAMING** overclock (or stock settings) should be saved as the **2nd profile** on Afterburner.

# Usage

1. Download the Python script and install dependencies from requirements.txt

2. Ensure your overclock for (profile 1: mining) and (profile 2: gaming) are set in Afterburner. If not using afterburner, set "UseAfterburner = True" to "UseAfterburner = False" in the python script.

3. Ensure all the games you play are listed in "GameExecutableNames". If not, find and add each game's executable name to the list.

4. Copy the Python script over to your startup folder, at 
"C:\Users\YourUserName\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup", replacing "YourUserName" with your PC's user name.

5. Run the script.























