const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("api", {
  // Window controls
  close:    () => ipcRenderer.send("win-close"),
  minimize: () => ipcRenderer.send("win-minimize"),
  maximize: () => ipcRenderer.send("win-maximize"),

  // RAG queries
  query:  (question, pipeline) => ipcRenderer.invoke("query", { question, pipeline }),
  ingest: (docsPath)           => ipcRenderer.invoke("ingest", { docsPath }),

  // Streaming callbacks
  onStream:    (cb) => ipcRenderer.on("query-stream",  (_, data) => cb(data)),
  onIngestLog: (cb) => ipcRenderer.on("ingest-log",    (_, data) => cb(data)),
  offStream:   ()   => ipcRenderer.removeAllListeners("query-stream"),
  offIngest:   ()   => ipcRenderer.removeAllListeners("ingest-log"),
});
