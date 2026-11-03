// J&F Originals – navigation (mobile menu + dropdowns) and the enquiry form (mailto).
(function () {
  "use strict";
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("mainnav");
  var de = document.documentElement.lang === "de";

  function closeSubs(except) {
    document.querySelectorAll("[data-has-sub].sub-open").forEach(function (li) {
      if (li === except) return;
      li.classList.remove("sub-open");
      var b = li.querySelector(".sub-toggle"); if (b) b.setAttribute("aria-expanded", "false");
    });
  }
  function setNav(open) {
    if (!toggle || !nav) return;
    nav.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? (de ? "Menü schließen" : "Close menu") : (de ? "Menü öffnen" : "Open menu"));
    if (!open) closeSubs();
  }
  if (toggle && nav) {
    toggle.addEventListener("click", function () { setNav(!nav.classList.contains("open")); });
  }
  document.querySelectorAll(".sub-toggle").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var li = btn.closest("[data-has-sub]");
      var open = !li.classList.contains("sub-open");
      closeSubs(li);
      li.classList.toggle("sub-open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
  });
  document.addEventListener("click", function (e) {
    if (header && !header.contains(e.target)) { setNav(false); closeSubs(); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var openSub = document.querySelector("[data-has-sub].sub-open .sub-toggle");
    closeSubs();
    if (nav && nav.classList.contains("open")) { setNav(false); toggle.focus(); }
    else if (openSub) openSub.focus();
  });

  /* ---------- Enquiry form → mailto (Kontakt page) ---------- */
  var form = document.getElementById("contact-form");
  if (!form) return;
  var status = document.getElementById("form-status");
  var TO = "info@jandforiginals.de";
  function fieldOf(input) { return input.closest(".field"); }
  function setStatus(msg, type) { status.textContent = msg; status.className = "form-status field--full" + (type ? " is-" + type : ""); }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var required = ["f-name", "f-company", "f-email"].map(function (id) { return document.getElementById(id); });
    var consent = document.getElementById("f-consent");
    var firstInvalid = null;
    required.forEach(function (input) {
      var ok = input.value.trim() !== "" && input.checkValidity();
      fieldOf(input).classList.toggle("is-invalid", !ok);
      input.setAttribute("aria-invalid", String(!ok));
      if (!ok && !firstInvalid) firstInvalid = input;
    });
    fieldOf(consent).classList.toggle("is-invalid", !consent.checked);
    if (!consent.checked && !firstInvalid) firstInvalid = consent;
    if (firstInvalid) {
      setStatus("Bitte füllen Sie alle Pflichtfelder aus (gültige E-Mail-Adresse) und bestätigen Sie die Datenschutzerklärung.", "error");
      firstInvalid.focus();
      return;
    }
    var v = function (id) { return document.getElementById(id).value.trim(); };
    var interests = Array.prototype.slice.call(form.querySelectorAll('input[name="Interesse"]:checked')).map(function (c) { return c.value; });
    var lines = [
      "Guten Tag,", "", "ich interessiere mich für eine Potenzialanalyse.", "",
      "Name: " + v("f-name"), "Unternehmen: " + v("f-company"), "E-Mail: " + v("f-email"),
      "Telefon: " + (v("f-phone") || "–"), "Art der Fläche: " + (v("f-area") || "–"),
      "Interesse: " + (interests.length ? interests.join(", ") : "–"), "",
      "Nachricht:", v("f-message") || "–", "", "Einwilligung Datenschutz: ja"
    ];
    window.location.href = "mailto:" + TO + "?subject=" + encodeURIComponent("Anfrage Potenzialanalyse – " + v("f-company")) + "&body=" + encodeURIComponent(lines.join("\r\n"));
    setStatus("Vielen Dank! Ihr E-Mail-Programm sollte sich jetzt mit Ihrer Anfrage öffnen – bitte dort auf „Senden“ klicken. Falls nicht, schreiben Sie uns direkt an " + TO + ".", "success");
  });
  form.addEventListener("input", function (e) {
    var f = fieldOf(e.target);
    if (f && f.classList.contains("is-invalid")) { f.classList.remove("is-invalid"); e.target.removeAttribute("aria-invalid"); }
  });
})();
