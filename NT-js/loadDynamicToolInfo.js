// --------------------------------------------------------------------------
// Dynamic Tool Info Loader (/tools-config.json)
// --------------------------------------------------------------------------

async function loadDynamicToolInfo() {
  const currentHost = window.location.host || 'root domain';
  document.querySelectorAll('.dynamic-domain').forEach(el => {
    el.textContent = currentHost;
  });

  const hubPath = window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/')) || '/';
  const hubEl = document.getElementById('openHubPath');
  if (hubEl) hubEl.textContent = currentHost;

  try {
    const response = await fetch('/tools-config.json');
    if (!response.ok) throw new Error('Config file unavailable');
    const config = await response.json();

    const toolName = hubPath.slice(1);
    const tool = config.tools?.find(t => 
      (t.name || t.slug)?.toLowerCase() === toolName
    );

    if (tool) {
      document.getElementById('openSlug').textContent = `/${tool.name}`;
      document.getElementById('openToolId').textContent = `/${tool.id}`;
    } else {
      throw new Error('Tool not found in configuration');
    }
  } catch (err) {
    console.error('Error loading tool info:', err);
    document.getElementById('openSlug').textContent = 'Unavailable';
    document.getElementById('openToolId').textContent = 'Unavailable';
  }
}

// Direct function call
loadDynamicToolInfo();