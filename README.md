# 🛠️ JS-Tools

![GitHub license](https://img.shields.io/github/license/MJTech46/JS-Tools?style=flat-square&color=6366f1)
![GitHub stars](https://img.shields.io/github/stars/MJTech46/JS-Tools?style=flat-square&color=6366f1)
![GitHub forks](https://img.shields.io/github/forks/MJTech46/JS-Tools?style=flat-square&color=6366f1)
![GitHub last commit](https://img.shields.io/github/last-commit/MJTech46/JS-Tools?style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

> A lightweight collection of fast, privacy-friendly, browser-based developer utilities built with HTML, CSS, and Vanilla JavaScript.

🌐 **Live:** [tools.mj46.in](https://tools.mj46.in/)

---

## 📖 Overview

**JS-Tools** is a collection of small, focused web utilities designed to make common developer and everyday tasks quicker and simpler.

The project follows a deliberately lightweight architecture: each tool is self-contained, runs directly in the browser, and avoids unnecessary frameworks or backend services.

The main tool directory is driven by a central `tools-config.json` configuration file, allowing tools to be listed and managed without hard-coding every tool into the main interface.

---

## ✨ Features

- 🔒 **Privacy-first** — tools are designed to process data locally in the browser.
- ⚡ **Fast & lightweight** — built with Vanilla JavaScript and minimal dependencies.
- 🧩 **Modular tools** — each utility can live in its own directory and be developed independently.
- 🗂️ **Config-driven directory** — tool metadata is maintained through `tools-config.json`.
- 🔢 **Numeric tool IDs** — tools can be referenced using short numeric paths such as `/103`.
- 🎨 **Modern UI** — responsive layouts with light/dark theme support.
- 📱 **Responsive design** — works across desktop, tablet, and mobile screens.
- 📋 **Convenient output** — tools can provide clipboard and file-export functionality where applicable.
- 🌐 **Static hosting friendly** — the project can be deployed as a static site without a dedicated backend.

---

## 🗂️ Project Structure

```text
JS-Tools/
├── tool-directory/
│   ├── index.html
│   └── ...
├── tools-config.json
├── index.html
├── LICENSE
└── README.md
```

Each individual tool can maintain its own HTML, CSS, and JavaScript files, keeping utilities isolated and easy to maintain.

---

## ⚙️ Tool Configuration

Tool metadata is maintained in:

```text
tools-config.json
```

A configuration entry can associate a numeric ID with a tool and its directory name:

```json
{
  "id": 103,
  "name": "calculator"
}
```

This approach makes it possible to expose short URLs such as:

```text
https://tools.mj46.in/103
```

while keeping the underlying directory structure independent from the public numeric identifier.

> The exact routing behavior depends on the site's current client-side routing configuration.

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| **HTML5** | Structure and semantic markup |
| **CSS3** | Layout, responsive design, and themes |
| **Vanilla JavaScript** | Tool logic and application behavior |
| **JSON** | Tool metadata and configuration |
| **GitHub Pages** | Static site hosting |

---

## 🔐 Privacy

JS-Tools is designed around client-side processing.

Where a tool does not explicitly require an external service, its input and output are handled locally by the browser rather than being sent to a project backend.

This makes the collection suitable for utilities involving text, calculations, transformations, and other tasks that can be performed entirely on the client.

---

## 🚀 Running Locally

Clone the repository:

```bash
git clone https://github.com/MJTech46/JS-Tools.git
cd JS-Tools
```

Because this is a static web project, it can be served using any local static web server.

For example, with Python:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

---

## ➕ Adding a New Tool

A typical workflow is:

1. Create a directory for the new tool.
2. Add its HTML/CSS/JavaScript files.
3. Add the tool's metadata to `tools-config.json`.
4. Assign it a unique numeric ID.
5. Test the tool locally.
6. Commit and push the changes.

Example:

```text
JS-Tools/
└── calculator/
    └── index.html
```

Then register the tool in the configuration file.

---

## 🎯 Design Goals

JS-Tools aims to keep every utility:

- **Simple** — one tool should solve one problem well.
- **Fast** — avoid unnecessary dependencies and processing.
- **Private** — prefer client-side processing whenever practical.
- **Accessible** — usable on different screen sizes and input devices.
- **Maintainable** — tools should remain independently understandable.
- **Extensible** — adding a new utility should require minimal changes to the core project.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the complete license text.

---

## 👨‍💻 Author

**MJTech46**

- GitHub: [github.com/MJTech46](https://github.com/MJTech46)
- Website: [mj46.in](https://www.mj46.in/)

---
<center>

⭐ If you find JS-Tools useful, consider giving the repository a star!
</center>
