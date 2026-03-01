const { app, BrowserWindow, ipcMain, shell } = require("electron");
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");

// ── Paths ────────────────────────────────────────────────────────────
const ROOT      = path.join(__dirname, "..");          // rag_comparison/
const VENV_WIN  = path.join(ROOT, ".venv", "Scripts", "python.exe");
const VENV_UNIX = path.join(ROOT, ".venv", "bin", "python");
const PYTHON    = fs.existsSync(VENV_WIN) ? VENV_WIN
                : fs.existsSync(VENV_UNIX) ? VENV_UNIX
                : "python";                            // fallback: system python

let win;

function createWindow() {
  win = new BrowserWindow({
    width: 960,
    height: 720,
    minWidth: 720,
    minHeight: 500,
    titleBarStyle: process.platform === "darwin" ? "hiddenInset" : "hidden",
    frame: false,
    backgroundColor: "#0d0d0d",
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  win.loadFile(path.join(__dirname, "index.html"));
}

app.whenReady().then(createWindow);
app.on("window-all-closed", () => { if (process.platform !== "darwin") app.quit(); });
app.on("activate", () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); });

// ── Window controls ──────────────────────────────────────────────────
ipcMain.on("win-close",    () => win.close());
ipcMain.on("win-minimize", () => win.minimize());
ipcMain.on("win-maximize", () => win.isMaximized() ? win.unmaximize() : win.maximize());

// ── Python bridge ────────────────────────────────────────────────────
// Runs: python electron_bridge.py <pipeline> <question>
// Streams stdout back line by line via IPC

ipcMain.handle("query", async (event, { question, pipeline }) => {
  return new Promise((resolve, reject) => {
    const script = path.join(ROOT, "electron_bridge.py");
    const args   = [script, pipeline, question];
    const proc   = spawn(PYTHON, args, {
      cwd: ROOT,
      env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONUTF8: "1" },
    });

    let stdout = "";
    let stderr = "";

    proc.stdout.on("data", chunk => { stdout += chunk.toString("utf8"); });
    // stderr carries all log output from Python (LangChain, Loader, etc.)
    proc.stderr.on("data", chunk => { stderr += chunk.toString("utf8"); });

    proc.on("close", code => {
      if (code !== 0) {
        reject(new Error(stderr || `Exit code ${code}`));
      } else {
        const trimmed = stdout.trim();
        try {
          resolve(JSON.parse(trimmed));
        } catch (e) {
          // Debug: show what we actually got
          reject(new Error(`JSON parse failed.\nstdout: ${trimmed.slice(0,300)}\nstderr: ${stderr.slice(0,300)}`));
        }
      }
    });
  });
});

ipcMain.handle("ingest", async (event, { docsPath }) => {
  return new Promise((resolve, reject) => {
    const script = path.join(ROOT, "electron_bridge.py");
    const args   = [script, "--ingest", docsPath || ""];
    const proc   = spawn(PYTHON, args, {
      cwd: ROOT,
      env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONUTF8: "1" },
    });

    let log = "";
    proc.stdout.on("data", chunk => {
      log += chunk.toString();
      win.webContents.send("ingest-log", chunk.toString());
    });
    proc.stderr.on("data", chunk => {
      log += chunk.toString();
      win.webContents.send("ingest-log", chunk.toString());
    });
    proc.on("close", code => {
      code === 0 ? resolve({ ok: true, log }) : reject(new Error(log));
    });
  });
});
