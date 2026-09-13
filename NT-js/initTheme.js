  // --------------------------------------------------------------------------
  // Init Theme Switching
  // --------------------------------------------------------------------------
  const currentTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', currentTheme);
