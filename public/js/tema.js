document.addEventListener("DOMContentLoaded", () => {
  const lightBtn = document.getElementById("lightBtn");
  const darkBtn = document.getElementById("darkBtn");

  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);

    if (lightBtn && darkBtn) {
      lightBtn.classList.toggle("active", theme === "light");
      darkBtn.classList.toggle("active", theme === "dark");
    }
  }

  if (lightBtn && darkBtn) {
    lightBtn.addEventListener("click", () => setTheme("light"));
    darkBtn.addEventListener("click", () => setTheme("dark"));
  }

  const savedTheme = localStorage.getItem("theme") || "light";
  setTheme(savedTheme);
});