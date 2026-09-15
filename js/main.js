const header = document.getElementById("siteHeader");
const menu = document.querySelector(".menu-toggle");
const nav = document.getElementById("primaryNav");

window.addEventListener(
  "scroll",
  () => {
    header.classList.toggle("scrolled", window.scrollY > 20);
  },
  { passive: true },
);

menu.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  menu.setAttribute("aria-expanded", String(open));
  menu.setAttribute(
    "aria-label",
    open ? "Close navigation" : "Open navigation",
  );
});
nav.querySelectorAll("a").forEach((link) =>
  link.addEventListener("click", () => {
    nav.classList.remove("open");
    menu.setAttribute("aria-expanded", "false");
    menu.setAttribute("aria-label", "Open navigation");
  }),
);

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 },
);
document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));

document.querySelectorAll(".faq-item").forEach((button) => {
  button.addEventListener("click", () => {
    const expanded = button.getAttribute("aria-expanded") === "true";
    document
      .querySelectorAll(".faq-item")
      .forEach((item) => item.setAttribute("aria-expanded", "false"));
    button.setAttribute("aria-expanded", String(!expanded));
  });
});

const form = document.getElementById("admissionForm");
const toast = document.getElementById("toast");
form.addEventListener("submit", (event) => {
  event.preventDefault();
  let valid = true;
  form.querySelectorAll("[required]").forEach((field) => {
    const error = field.parentElement.querySelector(".error");
    let message = "";
    if (!field.value.trim()) message = "This field is required.";
    else if (
      field.type === "email" &&
      !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value)
    )
      message = "Enter a valid email address.";
    error.textContent = message;
    if (message) valid = false;
  });
  if (!valid) return;
  toast.classList.add("show");
  form.reset();
  setTimeout(() => toast.classList.remove("show"), 4500);
});
