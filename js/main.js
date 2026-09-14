/* Savannah Foundation Repair Co – site behavior. Vanilla JS, no dependencies. */
(function () {
  "use strict";

  /* ---------- mobile nav ---------- */
  var toggle = document.querySelector("[data-nav-toggle]");
  var closeBtn = document.querySelector("[data-nav-close]");
  var nav = document.querySelector("[data-nav]");
  var overlay = document.querySelector("[data-nav-overlay]");

  function openNav() {
    nav && nav.classList.add("is-open");
    overlay && overlay.classList.add("is-open");
    document.body.style.overflow = "hidden";
  }
  function closeNav() {
    nav && nav.classList.remove("is-open");
    overlay && overlay.classList.remove("is-open");
    document.body.style.overflow = "";
  }
  toggle && toggle.addEventListener("click", openNav);
  closeBtn && closeBtn.addEventListener("click", closeNav);
  overlay && overlay.addEventListener("click", closeNav);

  /* dropdown nav groups – mobile accordion + desktop hover/click.
     lockedClosed flag: a click while open closes it and locks it closed
     until mouseleave, otherwise the mouseenter that a click also fires
     would silently reopen what was just closed. See Project1's
     web-dev-agent skill for the full writeup of this bug. */
  document.querySelectorAll(".nav-group").forEach(function (group) {
    var label = group.querySelector(".nav-group-label");
    var lockedClosed = false;

    label.addEventListener("click", function () {
      if (window.innerWidth >= 960) {
        var isOpen = group.classList.contains("is-open");
        group.classList.toggle("is-open", !isOpen);
        lockedClosed = isOpen;
      } else {
        group.classList.toggle("is-open");
      }
    });
    group.addEventListener("mouseenter", function () {
      if (window.innerWidth >= 960 && !lockedClosed) group.classList.add("is-open");
    });
    group.addEventListener("mouseleave", function () {
      if (window.innerWidth >= 960) {
        group.classList.remove("is-open");
        lockedClosed = false;
      }
    });
  });

  document.querySelectorAll(".main-nav a").forEach(function (link) {
    link.addEventListener("click", function () {
      if (window.innerWidth < 960) closeNav();
    });
  });

  /* ---------- image placeholder fallback ---------- */
  document.querySelectorAll(".img-slot img").forEach(function (img) {
    img.addEventListener("error", function () {
      img.closest(".img-slot").classList.add("is-empty");
      img.style.display = "none";
    });
    if (img.complete && img.naturalWidth === 0) {
      img.dispatchEvent(new Event("error"));
    }
  });

  /* ---------- quote form ---------- */
  var form = document.querySelector("[data-quote-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      var status = form.querySelector("[data-form-status]");
      var endpointConfigured = form.getAttribute("data-endpoint-ready") === "true";

      if (!endpointConfigured) {
        e.preventDefault();
        var data = new FormData(form);
        var lines = [];
        data.forEach(function (value, key) { lines.push(key + ": " + value); });
        var subject = encodeURIComponent("New inspection request – Savannah Foundation Repair Co");
        var body = encodeURIComponent(lines.join("\n"));
        window.location.href = "mailto:info@savannahfoundationrepairco.com?subject=" + subject + "&body=" + body;
        if (status) {
          status.textContent = "Opening your email app to send the request – or just call/text us instead.";
          status.className = "form-status ok is-visible";
        }
      }
      trackLead("quote_form");
    });
  }

  /* ---------- lead tracking (GA4) ----------
     No-ops silently until a real gtag.js snippet is added to <head>
     (see STATUS.md – waiting on the GA4 property for this site). */
  function trackLead(label, extra) {
    if (typeof gtag !== "function") return;
    var params = { event_category: "lead", event_label: label };
    for (var key in extra) params[key] = extra[key];
    gtag("event", "generate_lead", params);
  }

  document.querySelectorAll('a[href^="tel:"]').forEach(function (link) {
    link.addEventListener("click", function () { trackLead("click_to_call"); });
  });
  document.querySelectorAll('a[href^="sms:"]').forEach(function (link) {
    link.addEventListener("click", function () { trackLead("click_to_text"); });
  });
  document.querySelectorAll('a[href^="mailto:"]').forEach(function (link) {
    link.addEventListener("click", function () { trackLead("click_to_email"); });
  });

  /* ---------- footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
