import argparse
import asyncio
import json
import os
from playwright.async_api import async_playwright
# pip install playwright
# playwright install chromium

#================================================
# OG Image Generator CLI Tool # use -h
#================================================

# Configuration
CONFIG_FILE = "tools-config.json"
OG_WIDTH = 1200
OG_HEIGHT = 630

# Static Metadata
AUTHOR = "Abin Santhosh"
GITHUB = "MJTech46"
SITE = "tools.mj46.in"

# HTML & CSS Template for 1200x630 OG Image
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      width: {width}px;
      height: {height}px;
      background-color: #080c14;
      background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(59, 130, 246, 0.1) 0px, transparent 50%);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 48px;
      color: #f8fafc;
    }}
    .card {{
      width: 100%;
      height: 100%;
      background: #0f1523;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 24px;
      padding: 48px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6);
      position: relative;
    }}
    .top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .icon-box {{
      width: 72px;
      height: 72px;
      background: #171f33;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #818cf8;
    }}
    .icon-box svg {{
      width: 36px;
      height: 36px;
      stroke: #818cf8;
    }}
    .category-badge {{
      background: #171f33;
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #94a3b8;
      padding: 8px 18px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-family: 'JetBrains Mono', monospace;
    }}
    .content {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 10px;
    }}
    .title {{
      font-size: 52px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.02em;
      line-height: 1.15;
    }}
    .description {{
      font-size: 24px;
      color: #94a3b8;
      line-height: 1.5;
      font-weight: 400;
      max-width: 90%;
    }}
    .divider {{
      width: 100%;
      height: 1px;
      background: rgba(255, 255, 255, 0.08);
      margin-top: auto;
      margin-bottom: 24px;
    }}
    .footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 18px;
      color: #64748b;
    }}
    .meta-info {{
      display: flex;
      align-items: center;
      gap: 20px;
      font-size: 15px;
      color: #94a3b8;
    }}
    .meta-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .meta-item span {{
      color: #6366f1;
      font-weight: 600;
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="top-bar">
      <div class="icon-box">
        {icon}
      </div>
      <div class="category-badge">{category}</div>
    </div>
    
    <div class="content">
      <h1 class="title">{title}</h1>
      <p class="description">{description}</p>
    </div>

    <div class="footer-container">
      <div class="divider"></div>
      <div class="footer">
        <div>{id}: {slug}</div>
        <div class="meta-info">
          <div class="meta-item"><span>{site}</span></div>
          <div>•</div>
          <div class="meta-item">Author: <span>{author}</span></div>
          <div>•</div>
          <div class="meta-item">GitHub: <span>{github}</span></div>
        </div>
        <div>{version}</div>
      </div>
    </div>
  </div>
</body>
</html>
"""

async def generate_og_images(target_id=None, target_name=None, force=False):
    if not os.path.exists(CONFIG_FILE):
        print(f" Error: Config file '{CONFIG_FILE}' not found.")
        return

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    tools = data.get("tools", [])

    # Filter tools based on flags
    filtered_tools = []
    for tool in tools:
        card = tool.get("card", {})
        tool_id = tool.get("tool_id") or card.get("id")
        tool_name = tool.get("name") or card.get("footer", {}).get("slug", "")

        # ID filter check
        if target_id is not None and tool_id != target_id:
            continue

        # Name/Slug filter check
        if target_name is not None:
            query = target_name.strip().lower()
            slug = card.get("footer", {}).get("slug", "").lower()
            name = tool.get("name", "").lower()
            url = card.get("url", "").strip("/").lower()
            
            if query not in [name, slug, url]:
                continue

        filtered_tools.append(tool)

    if not filtered_tools:
        print(" No matching tools found for the given criteria.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": OG_WIDTH, "height": OG_HEIGHT})

        for tool in filtered_tools:
            card = tool.get("card", {})
            folder_name = tool.get("name") or card.get("url", "").rstrip("/")
            
            if not folder_name:
                continue

            os.makedirs(folder_name, exist_ok=True)
            output_path = os.path.join(folder_name, "og-image.png")

            # Skip generation if image exists and --force is not passed
            if os.path.exists(output_path) and not force:
                print(f" [SKIP] {output_path} already exists (use --force or -f to overwrite).")
                continue

            html_content = HTML_TEMPLATE.format(
                width=OG_WIDTH,
                height=OG_HEIGHT,
                icon=card.get("icon", ""),
                category=card.get("category", "UTILITY"),
                title=card.get("title", ""),
                description=card.get("description", ""),
                id=card.get("id", ""),
                slug=card.get("footer", {}).get("slug", folder_name),
                version=card.get("footer", {}).get("version", "v1.0"),
                site=SITE,
                author=AUTHOR,
                github=GITHUB
            )

            await page.set_content(html_content, wait_until="networkidle")
            await page.screenshot(path=output_path, type="png")
            print(f" [DONE] Generated: {output_path}")

        await browser.close()

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to generate Open Graph (OG) images for web tools."
    )
    
    parser.add_argument(
        "-id", "--id", 
        type=int, 
        help="Target a specific tool by its ID (e.g., -id 104)"
    )
    parser.add_argument(
        "-name", "--name", "-slug", "--slug", 
        type=str, 
        help="Target a specific tool by name or slug (e.g., -name calculator)"
    )
    parser.add_argument(
        "-f", "--force", 
        action="store_true", 
        help="Force overwrite/regenerate existing og-image.png files"
    )

    args = parser.parse_args()

    asyncio.run(
        generate_og_images(
            target_id=args.id, 
            target_name=args.name, 
            force=args.force
        )
    )

if __name__ == "__main__":
    main()