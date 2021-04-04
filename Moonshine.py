import psutil, os, time, subprocess


##############################################################################


GameExecutableNames = ["BlackOpsColdWar", "ModernWarfare", "Fortnite", "Genshin", "VALORANT", "Battlefield", "titanfall", "minecraft", "bfv", "destiny", "pubg", "playerunknown", "flightsimulator", "csgo", "eternal", "tarkov", "apex", "cyberpunk", "ktane.exe", "TOXIKK.exe", "One Finger Death Punch.exe", "battlevschess.exe", "castle.exe", "dirt3_game.exe", "Disco Dodgeball.exe", "dontstarve_steam.exe", "DungeonSouls.exe", "eurotrucks2.exe", "final_exam.exe", "FullMojo.exe", "Guac.exe", "Hammerwatch.exe", "Hero_Siege.exe", "kofxiii.exe", "WizardWarsLauncher.exe", "Not the Robots.exe", "PathOfExileSteam.exe", "quakelive_steam.exe", "sir.exe", "SpeedRunners.exe", "starbound.exe", "starbound_opengl.exe", "Tabletop Simulator.exe", "toribash.exe", "Unturned.exe", "aces.exe", "arma2.exe", "ArmA2OA.exe", "arma3.exe", "maniaplanet.exe", "broforce_beta.exe", "HeroesAndGeneralsDesktop.exe", "hng.exe", "downwell.exe", "RebelGalaxy.exe", "RebelGalaxyGOG.exe", "vermintide.exe", "Star_Trek_Online.exe", "Scrivener.exe", "dfbhd.exe", "Atilla.exe", "Bastion.exe", "BloodBowl2.exe", "BloodBowl2_DX_32.exe", "BloodBowl2_GL_32.exe", "Borderlands.exe", "Borderlands2.exe", "Brothers.exe", "Cities.exe", "Darkest.exe", "Darksiders2.exe", "defcon.exe", "DMC-DevilMayCry.exe", "dontstarve.exe", "DotP_D14.exe", "DragonAgeInquisition.exe", "DungeonoftheEndless.exe", "DustAET.exe", "Dwarf Fortress.exe", "DXHRDC.exe", "ed6_win.exe", "EndlessLegend.exe", "eu4.exe", "FTLGame.exe", "GalCiv2.exe", "GeometryWars.exe", "Hexcells Plus.exe", "Hexcells.exe", "HotlineGL.exe", "HotlineMiami.exe", "Kingdom.exe", "KSP.exe", "MetroLL.exe", "MKKE.exe", "nuclearthrone.exe", "PAC-MAN.exe", "payday2_win32_release.exe", "PlanetSide2_x64.exe", "Polynomial.exe", "Prison Architect.exe", "ProjectZomboid.exe", "Really Big Sky.exe", "ReassemblyRelease.exe", "RebelGalaxyGOG.exe", "RebelGalaxySteam.exe", "reprisaluniverse.exe", "Reus.exe", "Rome2.exe", "SanctumGame-Win32-Shipping.exe", "Scribble.exe", "Se4.exe", "sh4.exe", "shatteredplanet.exe", "Shogun2.exe", "ShooterGame.exe", "Sins of a Solar Empire Rebellion.exe", "SkullGirls.exe", "sots2.exe", "SpaceChem.exe", "StarDrive.exe", "starwarsbattlefront.exe", "Sunless Sea.exe", "superhexagon.exe", "SuperMeatBoy.exe", "Terraria.exe", "They Bleed Pixels PC.exe", "Timberman.exe", "TombRaider.exe", "Torchlight2.exe", "Trine.exe", "Trine2_32bit.exe", "UNDERTALE.exe", "uplink.exe", "v2game.exe", "Waves.exe", "Wildstar.exe", "Windward.exe", "WL2.exe", "WorldOfGoo.exe", "X3AP.exe", "X3AP_n.exe", "X3TC.exe", "XRebirth.exe", "yso_win.exe", "Zigfrak.exe", "Ziggurat.exe", "TmUnitedForever.exe", "EDLaunch.exe", "THUG.exe", "UE4-Win64-Test.exe", "Tales of Zestiria.exe", "FlagAC4BFSP.exe", "AIWar.exe", "Application-x64.exe", "Audiosurf2.exe", "Gnomoria.exe", "NEOScavenger.exe", "oolite.exe", "Overture.exe", "Pandora.exe", "sspace.exe", "SublevelZero.exe", "Tidalis.exe", "X-Plane-32bit.exe", "X-Plane.exe", "WAR.exe", "RobloxPlayerBeta.exe", "RobloxStudioBeta.exe"]

AfterburnerExecutableLocation = r"C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe"

MiningBatchFileLocation = r"C:\\Users\\Admin\\Desktop\\EthereumMining\\mine_ethereum.bat"  #  Change this!!

UseAfterburner = True

CheckInterval = 5

##############################################################################


info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

def resetAfterburner(profile):
	if UseAfterburner:
		print("Set afterburner to profile " + profile)
		os.system("""wmic process where "name='MSIAfterburner.exe'" delete""")
		subprocess.Popen([AfterburnerExecutableLocation, "-" + profile], shell=True)




resetAfterburner("profile1")

process = subprocess.Popen(MiningBatchFileLocation, startupinfo=info)

state = "mining"


 
def check():
	for proc in psutil.process_iter():
		try:
			n = proc.name() 
			for x in GameExecutableNames:
				if x.lower() in n.lower():
					return n
		except:
			a = 1
	return "none"


while True:
	time.sleep(CheckInterval)
	ret = check()

	if ret != "none" and state == "mining":
		state = "gaming"

		print("Swapping to Gaming mode.")

		resetAfterburner("profile2")
		pobj = psutil.Process(process.pid)
		for c in pobj.children(recursive=True):
		    c.kill()
		pobj.kill()

	elif ret == "none" and state == "gaming":
		state = "gaming"

		print("Swapping to Mining mode.")

		resetAfterburner("profile1")
		process = subprocess.Popen(MiningBatchFileLocation, startupinfo=info)
