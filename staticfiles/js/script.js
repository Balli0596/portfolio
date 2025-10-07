document.addEventListener("DOMContentLoaded", () => {
  const intro = document.getElementById("intro");
  const mainContent = document.getElementById("main-content");

  setTimeout(() => {
    intro.style.display = "none";
    document.body.style.overflow = "auto";
    mainContent.classList.remove("hidden");
  }, 3200);
});
